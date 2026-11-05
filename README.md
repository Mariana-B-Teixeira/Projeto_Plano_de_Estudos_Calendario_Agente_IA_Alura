# 📚 Agente especialista em plano de estudos para o Google Agenda

> Projeto desenvolvido por Mariana Branco Teixeira no âmbito da Imersão Engenharia de Software: Dev na Era da IA, realizada em parceria entre a Alura e o Google for Startups.

---

## 😊 Sobre o Projeto
Assistente autónomo e inteligente utilizando o Agent Development Kit (ADK) e a Antigravity CLI. O agente emprega skills especializadas para estruturar planos de estudos personalizados a partir de objetivos e prazos definidos pelo utilizador, gerando documento em CSV para integração com a Google Agenda e garantindo persistência segura de dados na nuvem com o Google Cloud Storage (GCS).

Este repositório contém o código, os recursos e a documentação de um agente de estudos inteligente construído em Python. O sistema foi desenvolvido com o auxílio do Google AI Studio para gestão de chaves e modelos, utilizando o Agent Development Kit (ADK) e a Antigravity CLI para controle de fluxos de agentes generativos. 

O projeto integra-se diretamente ao Google Cloud Storage (GCS) para garantir a persistência segura, automação e armazenamento de cronogramas, relatórios e datasets, sendo operado, testado e gerido através do ADK e da ferramenta de linha de comandos agents-cli.

---

## 🛠️ Tecnologias e Ferramentas Utilizadas
* **Linguagem:** Python
* **Orquestração de Agentes:** Agent Development Kit (ADK) & agents-cli
* **Ambiente de IA & Modelos:** Google AI Studio & Antigravity CLI
* **Armazenamento em Nuvem:** Google Cloud Storage (GCS)
* **Ambiente de Desenvolvimento:** Google Cloud Shell & Cloud Editor
* **Controlo de Versão:** Git & GitHub

---

## 📂 Estrutura do Repositório

```text
📦 Projeto_Plano_de_Estudos_Calendario_Agente_IA_Alura
 ┣ 📂 agente-estudos          # Núcleo do agente inteligente
 ┃  ┣ 📂 app                  # Lógica principal, código do agente e skills
 ┃  ┣ 📂 planos               # Cronogramas e ficheiros de estudo gerados (CSV)
 ┃  ┗ 📂 scripts              # Scripts de automação e configuração do GCS
 ┣ 📂 skills                  # Skills e definições modulares do agente
 ┣ 📂 tests                   # Testes unitários e de integração
 ┣ 📜 Dockerfile              # Configuração de contentorização para o Agent Runtime
 ┗ 📜 README.md               # Documentação principal do projeto
```

---

## ⚙️ Configuração, Testes e Execução

1. **Clonar o repositório:**
   ```bash
   git clone https://github.com/Mariana-B-Teixeira/Projeto_Plano_de_Estudos_Calendario_Agente_IA_Alura.git
   cd Projeto_Plano_de_Estudos_Calendario_Agente_IA_Alura
   ```

2. **Configurar as variáveis de ambiente:**
   Defina a sua chave de API gerada no Google AI Studio e ajuste as configurações:
   ```bash
   export GEMINI_API_KEY="a_sua_chave_aqui"
   export GOOGLE_GENAI_USE_VERTEXAI=FALSE
   ```

3. **Testar e executar o Agente:**

   * **Opção A — Via linha de comandos (`agents-cli`):**
     Para testar e correr o agente rapidamente pelo terminal, utilize o comando:
     ```bash
     agents-cli run "O seu pedido para o agente"
     ```

   * **Opção B — Via interface de desenvolvimento do ADK:**
     Para testar e interagir de forma visual e interativa com o agente:
     1. Inicie o ambiente visual do ADK no terminal do seu ambiente de trabalho:
        ```bash
        adk web
        ```
     2. Abra o link gerado para aceder à interface interativa no navegador.
     3. Utilize o painel para iniciar uma nova sessão, enviar prompts de teste, acompanhar eventos em tempo real e inspecionar o comportamento das skills do agente de estudos.

---

**Este projeto faz parte das entregas práticas da Imersão Engenharia de Software: Dev na Era da IA (Alura & Google for Startups), consolidando competências avançadas em desenvolvimento com Inteligência Artificial, engenharia de prompts, integração com a cloud e arquitetura de agentes autônomos.**

---

⭐***Desenvolvido por Mariana Branco Teixeira.***
