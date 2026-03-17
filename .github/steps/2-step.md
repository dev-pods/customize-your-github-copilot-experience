## Passo 2: Instruções Específicas por Arquivo

Com as instruções gerais do projeto prontas, você percebe que precisa de regras de formatação mais específicas relacionadas apenas às tarefas. Embora suas instruções gerais funcionem muito bem para padrões gerais de código, você não quer poluí-las com requisitos detalhados de estrutura de tarefas que são incluídos em todas as mensagens do chat.

Você quer garantir que todas as suas tarefas sigam o mesmo padrão e estrutura para que os alunos tenham uma experiência consistente, mas essas regras devem se aplicar apenas quando se trabalha com arquivos de tarefas.

### 📖 Teoria: Arquivos de Instrução Personalizados

Arquivos de instrução (`*.instructions.md`) fornecem ao Copilot orientações direcionadas para arquivos ou diretórios específicos no seu projeto.

Diferente das instruções de repositório que se aplicam em todo lugar, esses arquivos usam o campo `applyTo` no [frontmatter](https://jekyllrb.com/docs/front-matter/) com [sintaxe glob](https://code.visualstudio.com/docs/editor/glob-patterns) para direcionar arquivos específicos. Isso aplica automaticamente as instruções sempre que o Copilot trabalha em arquivos que correspondem ao padrão. Alternativamente, você pode anexar instruções manualmente usando o botão **Add Context** no Copilot Chat.

O Visual Studio Code procura arquivos `*.instructions.md` no diretório `.github/instructions/` por [padrão](vscode://settings/chat.instructionsFilesLocations).

> [!TIP]
> As instruções devem focar em **COMO** uma tarefa deve ser feita — descrevendo as diretrizes, padrões e convenções usadas naquela parte específica do código.

Consulte a página [VS Code Docs: Custom Instructions](https://code.visualstudio.com/docs/copilot/copilot-customization#_custom-instructions) para mais informações.

### ⌨️ Atividade: Criar Instruções Específicas para Tarefas

Agora vamos criar instruções direcionadas especificamente para arquivos de tarefas, garantindo que sigam uma estrutura e formatação consistentes.

1. Primeiro, vamos examinar o template de tarefas existente. Abra `templates/assignment-template.md` para ver a estrutura que queremos que todas as tarefas sigam.

1. Crie um novo arquivo chamado:

   ```text
   .github/instructions/assignments.instructions.md
   ```


1. Adicione o seguinte conteúdo para definir os padrões de formatação das tarefas. Isso também garantirá que sejam aplicados automaticamente para cada solicitação do chat em arquivos Markdown (`.md`) no diretório `assignments`.

   ```markdown
   ---
   applyTo: "assignments/**/*.md"
   ---

   # Assignment Markdown Structure Guidelines

   All assignment markdown files should follow these guidelines:

   ## 1. Template Usage

   - Assignment markdown files must follow the structure in [`templates/assignment-template.md`](../../templates/assignment-template.md).
   - The assignment must be created as a `README.md` file
   - Do not remove or skip required sections from the template.

   ## 2. Section Guidance

   The section headers should reflect the structure in the template, including the exact icon usage.

   - **Title**: Replace `[Assignment Title]` with a short, descriptive name (e.g., `Python Basics`, `Loops and Conditionals`, `Functions and Modules`).
   - **Objective**: Write 1-2 sentences summarizing what the student will learn or accomplish. Focus on the main skills or concepts.
   - **Tasks**: For each task:
      - Use a specific, action-oriented task name
      - In the Description, clearly state what the student must do.
      - In Requirements, use bullet points to list the expected outcomes or features. Be specific and measurable
      - Provide example input/output in code blocks if helpful.

   Do not include extra sections unless explicitly specified.
   ```

### ⌨️ Atividade: Testar as Instruções de Tarefas

1. Abra o arquivo `assignments/games-in-python/README.md` no VS Code. Esta tarefa não segue todas as convenções que você estabeleceu como professor(a).

1. Reserve um momento para revisar a estrutura atual deste arquivo de tarefa. Observe como ela difere da estrutura do template que você examinou anteriormente. Você também pode ver como ela aparece atualmente na aba **Site Preview**.

1. Com o arquivo de tarefa aberto, peça ao Copilot no modo `Agent` para atualizar a estrutura da tarefa:

   > ![Static Badge](https://img.shields.io/badge/-Prompt-text?style=social&logo=github%20copilot)
   >
   > ```prompt
   > Update this assignment file to follow the project standards and template structure
   > ```

1. Observe como o Copilot referencia as instruções gerais do projeto e os arquivos de instrução específicos para tarefas.

   <img width="492" height="376" alt="screenshot of Copilot chat showing attached references" src="https://github.com/user-attachments/assets/dbf26be3-5940-4619-af4e-0a4380f16494" />

1. Compare as alterações sugeridas com a estrutura original do arquivo para ver como o Copilot aplicou suas instruções. Aplique as alterações sugeridas e verifique como a tarefa atualizada aparece no **Site Preview**.

1. Faça o commit de ambos os arquivos na branch `main` e envie (push) suas alterações para o GitHub.

   - `.github/instructions/assignments.instructions.md`
   - `assignments/games-in-python/README.md`

1. Aguarde a Mona preparar o próximo passo!

<details>
<summary>Está com problemas? 🤷</summary><br/>

- Certifique-se de que fez o commit de ambos os arquivos na branch `main`:
  - `.github/instructions/assignments.instructions.md`
  - `assignments/games-in-python/README.md`

</details>
