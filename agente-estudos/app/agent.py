import os
from datetime import datetime
from pathlib import Path

from google.adk import Agent
from google.adk.environment import LocalEnvironment
from google.adk.integrations.gcs import GCSToolset
from google.adk.integrations.gcs.settings import Capabilities, GCSToolSettings
from google.adk.skills import load_skill_from_dir
from google.adk.tools.environment import EnvironmentToolset
from google.adk.tools.skill_toolset import SkillToolset

# Absolute paths calculated relative to agent.py
BASE_DIR = Path(__file__).parent.resolve()
SKILLS_DIR = BASE_DIR / "skills" / "plano-de-estudos"
PLANOS_DIR = (BASE_DIR.parent / "planos").resolve()
PLANOS_DIR.mkdir(parents=True, exist_ok=True)

# GCS Bucket configuration
BUCKET_NAME = os.getenv("GCS_BUCKET_NAME", "agente-estudos")

# Load the study plan skill
skill = load_skill_from_dir(SKILLS_DIR)
skill_toolset = SkillToolset(skills=[skill])


# Filter environment tools to only expose ReadFile and WriteFile
class FerramentasDeArquivo(EnvironmentToolset):
    async def get_tools(self, readonly_context=None):
        tools = await super().get_tools(readonly_context)
        return [t for t in tools if t.name in ("ReadFile", "WriteFile")]


env_toolset = FerramentasDeArquivo(
    environment=LocalEnvironment(working_dir=PLANOS_DIR)
)

# GCS Toolset setup for reading and writing to Google Cloud Storage bucket
gcs_settings = GCSToolSettings(capabilities=[Capabilities.READ_WRITE])
gcs_toolset = GCSToolset(gcs_tool_settings=gcs_settings)

# Model selection from environment variable
MODEL_NAME = os.getenv("MODEL", "gemini-3.8-flash")


# Dynamic instruction provider with today's date
def get_instruction(context=None) -> str:
    hoje = datetime.now().strftime("%d/%m/%Y")
    return (
        f"Hoje é {hoje}.\n"
        "Você é um mentor de estudos amigável, encorajador, direto e sem enrolação, falando sempre em português do Brasil.\n"
        "Sua missão é ajudar o usuário a organizar seus estudos, criando ou ajustando planos de estudo personalizados com a skill 'plano-de-estudos'.\n"
        "Siga rigorosamente a Regra de Ativação (Gating Rule) da skill: sem objetivo, prazo, disponibilidade e nível atual, pergunte APENAS o que falta e NÃO chame `load_skill_resource`.\n"
        f"Quando todas as informações estiverem presentes, siga o workflow da skill e grave a agenda em CSV no bucket GCS '{BUCKET_NAME}' usando `create_object` (com bucket_name='{BUCKET_NAME}' e object_name='plano-de-estudos.csv') e também salve localmente com `WriteFile` no arquivo `plano-de-estudos.csv`."
    )


root_agent = Agent(
    name="app",
    description="Agente mentor de estudos que gera planos personalizados e exporta agenda em CSV no GCS e localmente.",
    model=MODEL_NAME,
    instruction=get_instruction,
    tools=[skill_toolset, env_toolset, gcs_toolset],
)
