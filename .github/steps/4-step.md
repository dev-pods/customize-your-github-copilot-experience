## Passo 4: Criando Modos de Chat Personalizados

Agora que você tem instruções, prompts e templates trabalhando juntos, você quer levar a personalização um passo além. Ao fazer brainstorm de novas tarefas, você gostaria de uma experiência de chat especializada que foca puramente na ideação em vez da implementação.

### 📖 Teoria: Modos de Chat Personalizados

Modos de chat personalizados (`*.chatmode.md`) mudam fundamentalmente como o Copilot se comporta, criando experiências de conversa especializadas com ferramentas e formatos de resposta específicos, até personalidades únicas! Eles são selecionados de uma lista suspensa na interface do Copilot Chat.

O Visual Studio Code procurará arquivos `*.chatmode.md` no diretório `.github/chatmodes/` por [padrão](vscode://settings/chat.modeFilesLocations).

> [!TIP]
> Saiba mais sobre Modos de Chat:
>
> - [VS Code Docs: Custom Chat Modes](https://code.visualstudio.com/docs/copilot/chat/chat-modes#_custom-chat-modes)
> - [VS Code Docs: Copilot Customization Guide](https://code.visualstudio.com/docs/copilot/copilot-customization)


### ⌨️ Atividade: Criar um Modo de Chat de Brainstorm para Tarefas

Agora vamos criar um modo de chat especializado para fazer brainstorm de ideias de tarefas.

1. Crie um novo arquivo chamado `.github/chatmodes/assignment-brainstorming.chatmode.md`

1. Adicione o seguinte conteúdo para criar uma experiência de brainstorm focada:

   ```markdown
   ---
   description: 💡 Assistente de brainstorm de tarefas
   tools: ["codebase", "search"]
   ---

   # 💡 Assistente de Brainstorm de Tarefas

   **MODO BRAINSTORM ATIVADO** 🚀

   Eu sou seu parceiro de brainstorm de tarefas para a Mergington High School! Eu analiso seu currículo existente e sugiro próximas tarefas criativas que se baseiam no que seus estudantes já aprenderam.

   ## Meu Estilo de Resposta

   Toda resposta segue este formato:

   🔍 ESCANEAMENTO RÁPIDO: [Análise breve das tarefas existentes]
   💡 EXPLOSÃO DE IDEIAS: [3-5 sugestões rápidas]
   🎯 PRÓXIMA PERGUNTA: [O que preciso saber para ajudar mais]

   ## Regras

   - ⚡ Mantenha respostas curtas
   - 🎯 Sempre termine com uma pergunta específica
   - 💡 Foque em conceitos, não detalhes
   - 🚫 Nunca escreva especificações de tarefas
   - 📊 Baseie ideias em lacunas do currículo existente
   ```

### ⌨️ Atividade: Testar o Modo de Chat de Brainstorm

1. Abra o Copilot Chat no VS Code.

1. Selecione seu modo de chat personalizado da lista suspensa de modos de chat.

   <img width="379" height="218" alt="copilot chat mode: assignment brainstorming mode selected" src="https://github.com/user-attachments/assets/4effffa7-b8ef-4830-8050-9c777f9f0189" />

1. Teste o modo de chat com perguntas que um professor faria. Note o formato de resposta diferente!

   > ![Static Badge](https://img.shields.io/badge/-Prompt-text?style=social&logo=github%20copilot)
   >
   > ```prompt
   > Que tópicos de tarefas estão faltando no meu currículo atual?
   > ```

   > ![Static Badge](https://img.shields.io/badge/-Prompt-text?style=social&logo=github%20copilot)
   >
   > ```prompt
   > Sugira 3 tarefas avançadas de Python para meus estudantes.
   > ```

   > ![Static Badge](https://img.shields.io/badge/-Prompt-text?style=social&logo=github%20copilot)
   >
   > ```prompt
   > Qual seria uma boa tarefa de acompanhamento após a tarefa de análise de dados?
   > ```

1. Tente fazer perguntas de acompanhamento para ver como o modo de chat mantém sua personalidade durante a conversa.

1. Commit e push suas mudanças para o novo arquivo de modo de chat: `.github/chatmodes/assignment-brainstorming.chatmode.md`

1. Aguarde a Mona dar uma revisão final!

<details>
<summary>Tendo problemas? 🤷</summary><br/>

- Certifique-se de que o arquivo de modo de chat está no diretório `.github/chatmodes/` com a extensão `.chatmode.md`.
- Modos de chat são selecionados da lista suspensa no topo da interface de chat, não com menções `@`.
- Se o modo de chat não aparecer na lista suspensa, reinicie o VS Code ou recarregue a janela.
- O array `tools` no frontmatter controla quais capacidades o modo de chat pode acessar.
- Modos de chat mantêm sua personalidade durante toda a conversa.

</details>
