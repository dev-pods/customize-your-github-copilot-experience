## Passo 4: Criando Agentes Personalizados

Agora que você tem instructions, skills e templates trabalhando juntos, é hora de levar a customização um passo além. Ao fazer brainstorming de novas assignments, você quer uma experiência de chat especializada e focada puramente em ideação, para depois fazer handoff para o Agent Mode implementar de fato a criação da assignment usando a skill que você criou no Passo 3.

### 📖 Teoria: Agentes Personalizados

Agentes personalizados (`*.agent.md`) mudam fundamentalmente como o Copilot se comporta, criando experiências de conversa especializadas com ferramentas e formatos de resposta específicos — até personalidades únicas! Eles são selecionados em uma lista na interface do Copilot Chat.

O Visual Studio Code procura arquivos `*.agent.md` no diretório `.github/agents/`.

> [!TIP]
> Saiba mais sobre Agentes Personalizados:
>
> - [VS Code Docs: Custom Agents](https://code.visualstudio.com/docs/copilot/customization/custom-agents)
> - [GitHub Docs: Custom Agents Configuration](https://docs.github.com/en/copilot/reference/custom-agents-configuration)

### ⌨️ Atividade: Criar um Agente Personalizado para Brainstorming de Assignments

Agora vamos criar um agente personalizado especializado que ajuda no brainstorming de ideias de assignment e depois faz handoff para o Agent Mode implementar de fato a criação da assignment usando a skill que você criou no Passo 3.

1. Crie um novo arquivo chamado:

   ```text
   .github/agents/assignment-brainstorming.agent.md
   ```

1. Adicione o seguinte conteúdo para criar uma experiência de brainstorming focada:

   ```markdown
   ---
   name: Assignment Brainstorming
   description: Faça brainstorming da próxima assignment de programação para estudantes da Mergington High School
   tools: ["search", "vscode/askQuestions"]
   handoffs:
     - label: "Create this assignment"
       agent: agent
       prompt: "Crie uma nova assignment com base na recomendação da sessão de brainstorming acima."
       send: true
   ---

   # Assignment Brainstorming Assistant

   Ajude o professor a decidir a próxima assignment, analisando o currículo existente e sugerindo uma ideia focada.

   ## Workflow

   1. Escaneie o diretório `assignments/` e `config.json` para entender quais tópicos já estão cobertos.
   2. Use a tool `askQuestions` para coletar as preferências do professor: nível de dificuldade, área temática e eventuais restrições.
   3. Recomende **uma** assignment: um título, o conceito central e uma frase explicando por que ela preenche uma lacuna no currículo.
   4. Sugira usar o botão **Create this assignment** para criá-la.

   ## Regras

   - Mantenha as respostas curtas, no máximo algumas frases por seção.
   - Nunca escreva especificações completas de assignment. Esse é o papel da skill.
   - Baseie as recomendações em lacunas do currículo existente.
   - Sempre termine com um próximo passo claro.
   ```

   Vamos detalhar as partes principais:
   - **`tools: ["search", "vscode/askQuestions"]`**: dá ao agente a capacidade de pesquisar na base de código e apresentar perguntas estruturadas com opções selecionáveis, em vez de depender de uma troca livre em texto.
   - **`handoffs`**: define um botão "Create this assignment". Ao clicar, ele alterna para o modo padrão do Copilot Agent e envia automaticamente um prompt referenciando a recomendação do brainstorming. Isso deve acionar a skill `new-assignment` do Passo 3 para que a assignment seja realmente criada com base na ideia sugerida.
   - **Instruções do corpo**: definem a personalidade e o fluxo de trabalho do agente. Note que ele está focado apenas em _ideação_ e delega explicitamente a implementação para a skill.

### ⌨️ Atividade: Testar o Agente Personalizado de Brainstorming

1. Abra o Copilot Chat no VS Code.

1. Selecione seu agente personalizado na lista suspensa de agentes.

   <img width="379" height="218" alt="copilot agent: assignment brainstorming agent selected" src="https://github.com/gabrielhartog-invillia/skills-customize-your-github-copilot-experience/blob/main/.github/images/custom-agent-dropdown-selection.png?raw=true" />

1. Inicie uma sessão de brainstorming:

   > ![Static Badge](https://img.shields.io/badge/-Prompt-text?style=social&logo=github%20copilot)
   >
   > ```prompt
   > O que eu devo ensinar em seguida?
   > ```

1. O agente vai escanear suas assignments existentes e, em seguida, fazer perguntas estruturadas sobre dificuldade e preferências de tópico. Responda para refinar a recomendação.

1. Quando o agente recomendar uma assignment, clique no botão **Create this assignment** para fazer handoff para o Agent Mode implementar.

   <img width="380" alt="Create this assignment handoff button" src="https://github.com/gabrielhartog-invillia/skills-customize-your-github-copilot-experience/blob/main/.github/images/handoff-button.png?raw=true" />

1. Faça commit e push das suas alterações para a branch `main`.

1. Aguarde a Mona dar a revisão final!

<details>
<summary>Está com problemas? 🤷</summary><br/>

- Certifique-se de que o arquivo do agente personalizado está no diretório `.github/agents/` com a extensão `.agent.md`.
- Agentes personalizados são selecionados na lista suspensa na parte inferior da interface do chat, não com menções `@`.
- Se o agente personalizado não aparecer na lista suspensa, reinicie o VS Code ou recarregue a janela.

</details>
