## Passo 2: Instruções Específicas por Arquivo

Com as instruções gerais do projeto prontas, você percebe que precisa de regras de formatação mais específicas relacionadas apenas às tarefas. Enquanto suas instruções de repositório funcionam bem para padrões gerais de código, você não quer poluí-las com requisitos detalhados de estrutura de tarefas que são incluídos em todas as mensagens de chat.

Você quer garantir que todas as suas tarefas sigam o mesmo padrão e estrutura para que os alunos tenham uma experiência consistente, mas essas regras devem ser aplicadas somente ao trabalhar nos arquivos de tarefas.

### 📖 Teoria: Arquivos de Instruções Personalizadas

Arquivos de instrução (`*.instructions.md`) fornecem ao Copilot orientações direcionadas para arquivos ou diretórios específicos do seu projeto.

Diferente das instruções de repositório que se aplicam em todo lugar, esses arquivos usam o campo `applyTo` no [frontmatter](https://jekyllrb.com/docs/front-matter/) com [sintaxe glob](https://code.visualstudio.com/docs/editor/glob-patterns) para direcionar arquivos específicos. Isso aplica automaticamente as instruções sempre que o Copilot trabalha em arquivos que correspondem a esse padrão. Alternativamente, você pode anexar instruções manualmente usando o botão **Add Context** no Copilot Chat.

O Visual Studio Code procura arquivos `*.instructions.md` no diretório `.github/instructions/` por [padrão](vscode://settings/chat.instructionsFilesLocations).

> [!TIP]
> As instruções devem focar em **COMO** uma tarefa deve ser feita — descrevendo as diretrizes, padrões e convenções usados naquela parte específica do código.

Veja a página [VS Code Docs: Custom Instructions](https://code.visualstudio.com/docs/copilot/copilot-customization#_custom-instructions) para mais informações.

### ⌨️ Atividade: Criar Instruções Específicas para Tarefas

Agora vamos criar instruções direcionadas especificamente para arquivos de tarefas a fim de garantir que sigam uma estrutura e formatação consistentes.

1. Primeiro, vamos examinar o template de tarefas existente. Abra `templates/assignment-template.md` para ver a estrutura que queremos que todas as tarefas sigam.

1. Crie um novo arquivo chamado:

   ```text
   .github/instructions/assignments.instructions.md
   ```


1. Adicione o conteúdo a seguir para definir os padrões de formatação das tarefas. Isso também garantirá que eles sejam aplicados automaticamente para cada requisição de chat em arquivos Markdown (`.md`) na pasta `assignments`.

   ```markdown
   ---
   applyTo: "assignments/**/*.md"
   ---

   # Diretrizes de Estrutura para Markdown de Tarefas

   Todos os arquivos markdown de tarefas devem seguir estas diretrizes:

   ## 1. Uso do Template

   - Os arquivos markdown de tarefas devem seguir a estrutura em [`templates/assignment-template.md`](../../templates/assignment-template.md).
   - A tarefa deve ser criada como um arquivo `README.md`
   - Não remova nem pule seções obrigatórias do template.

   ## 2. Orientação de Seções

   Os cabeçalhos das seções devem refletir a estrutura do template, incluindo o uso exato de ícones.

   - **Título**: Substitua `[Assignment Title]` por um nome curto e descritivo (por exemplo, `Python Basics`, `Loops and Conditionals`, `Functions and Modules`).
   - **Objetivo**: Escreva 1-2 frases resumindo o que o aluno aprenderá ou realizará. Foque nas principais habilidades ou conceitos.
   - **Tarefas**: Para cada tarefa:
      - Use um nome de tarefa específico e orientado à ação
      - Na Descrição, indique claramente o que o aluno deve fazer.
      - Nos Requisitos, use bullets para listar os resultados ou funcionalidades esperadas. Seja específico e mensurável
      - Forneça exemplos de entrada/saída em blocos de código se for útil.

   Não inclua seções extras a menos que seja explicitamente especificado.
   ```

### ⌨️ Atividade: Testar as Instruções de Tarefas

1. Abra o arquivo `assignments/games-in-python/README.md` no VS Code. Esta tarefa não segue todas as convenções que você configurou como professor.

1. Reserve um momento para revisar a estrutura atual desse arquivo de tarefa. Observe como ele difere da estrutura do template que você examinou anteriormente. Você também pode ver como ele aparece na aba **Site Preview**.

1. Com o arquivo de tarefa aberto, peça ao Copilot no modo `Agent` para atualizar a estrutura da tarefa:

   > ![Static Badge](https://img.shields.io/badge/-Prompt-text?style=social&logo=github%20copilot)
   >
   > ```prompt
   > Atualize este arquivo de tarefa para seguir os padrões do projeto e a estrutura do template
   > ```

1. Observe como o Copilot referencia as instruções gerais do projeto e os arquivos de instruções específicos para tarefas.

   <img width="492" height="376" alt="screenshot of Copilot chat showing attached references" src="https://github.com/user-attachments/assets/dbf26be3-5940-4619-af4e-0a4380f16494" />

1. Compare as mudanças sugeridas com a estrutura original do arquivo para ver como o Copilot aplicou suas instruções. Aplique as mudanças sugeridas e verifique como a tarefa atualizada aparece no **Site Preview**.

1. Faça commit dos dois arquivos na branch `main` e envie suas alterações para o GitHub.

   - `.github/instructions/assignments.instructions.md`
   - `assignments/games-in-python/README.md`

1. Aguarde a Mona preparar o próximo passo!

<details>
<summary>Está com problemas? 🤷</summary><br/>

- Verifique se você fez commit dos dois arquivos na branch `main`:
  - `.github/instructions/assignments.instructions.md`
  - `assignments/games-in-python/README.md`

</details>