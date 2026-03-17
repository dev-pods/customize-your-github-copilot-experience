## Passo 4: Criando Agentes Personalizados

Agora que você tem instruções, prompts e templates trabalhando juntos, você quer levar a personalização um passo além. Ao fazer brainstorming de novas tarefas, você gostaria de ter uma experiência de chat especializada que foque puramente na ideação, em vez da implementação.

### 📖 Teoria: Agentes Personalizados

Agentes personalizados (`*.agent.md`) mudam fundamentalmente como o Copilot se comporta, criando experiências de conversa especializadas com ferramentas e formatos de resposta específicos — até personalidades únicas! Eles são selecionados em uma lista suspensa na interface do Copilot Chat.

O Visual Studio Code procura arquivos `*.agent.md` no diretório `.github/agents/`.

> [!TIP]
> Saiba mais sobre Agentes Personalizados:
>
> - [VS Code Docs: Custom Agents](https://code.visualstudio.com/docs/copilot/customization/custom-agents)
> - [GitHub Docs: Custom Agents Configuration](https://docs.github.com/en/copilot/reference/custom-agents-configuration)


### ⌨️ Atividade: Criar um Agente Personalizado para Brainstorming de Tarefas

Agora vamos criar um agente personalizado especializado em brainstorming de ideias para tarefas.

1. Crie um novo arquivo chamado:

   ```text
   .github/agents/assignment-brainstorming.agent.md
   ```

1. Adicione o seguinte conteúdo para criar uma experiência de brainstorming focada:

   ```markdown
   ---
   name: assignment-brainstorming
   description: Assignment brainstorming assistant
   tools: ["search", "web"]
   ---

   # 💡 Assignment Brainstorming Assistant

   **BRAINSTORM MODE ACTIVATED** 🚀

   I'm your assignment brainstorming partner for Mergington High School! I analyze your existing curriculum and suggest creative next assignments that build on what your students have already learned.

   ## My Response Style

   Every response follows this format:

   🔍 QUICK SCAN: [Brief analysis of existing assignments]
   💡 IDEA BURST: [3-5 rapid-fire suggestions]
   🎯 NEXT QUESTION: [What I need to know to help more]

   ## Rules

   - ⚡ Keep responses short
   - 🎯 Always end with a specific question
   - 💡 Focus on concepts, not details
   - 🚫 Never write assignment specs
   - 📊 Base ideas on existing curriculum gaps
   ```

### ⌨️ Atividade: Testar o Agente Personalizado de Brainstorming

1. Abra o Copilot Chat no VS Code.

1. Selecione seu agente personalizado na lista suspensa de agentes.

   <img width="379" height="218" alt="copilot agent: assignment brainstorming agent selected" src="https://github.com/user-attachments/assets/4effffa7-b8ef-4830-8050-9c777f9f0189" />

1. Teste o agente personalizado com perguntas que um professor faria. Observe o formato de resposta diferente!

   > ![Static Badge](https://img.shields.io/badge/-Prompt-text?style=social&logo=github%20copilot)
   >
   > ```prompt
   > Quais tópicos de tarefas estão faltando no meu currículo atual?
   > ```

   > ![Static Badge](https://img.shields.io/badge/-Prompt-text?style=social&logo=github%20copilot)
   >
   > ```prompt
   > Sugira 3 tarefas avançadas de Python para meus alunos.
   > ```

   > ![Static Badge](https://img.shields.io/badge/-Prompt-text?style=social&logo=github%20copilot)
   >
   > ```prompt
   > Qual seria uma boa tarefa de acompanhamento após a tarefa de análise de dados?
   > ```

1. Tente fazer perguntas de acompanhamento para ver como o agente personalizado mantém sua personalidade ao longo da conversa.

1. Faça o commit e envie (push) suas alterações para o arquivo do novo agente personalizado: `.github/agents/assignment-brainstorming.agent.md`

1. Aguarde a Mona dar a revisão final!

<details>
<summary>Está com problemas? 🤷</summary><br/>

- Certifique-se de que o arquivo do agente personalizado está no diretório `.github/agents/` com a extensão `.agent.md`.
- Agentes personalizados são selecionados na lista suspensa na parte inferior da interface do chat, não com menções `@`.
- Se o agente personalizado não aparecer na lista suspensa, reinicie o VS Code ou recarregue a janela.

</details>
