## Passo 3: Criando Prompts Reutilizáveis

Agora que você estabeleceu instruções para as tarefas, você quer agilizar a criação de novas tarefas.

Criar tarefas é um processo repetitivo que envolve múltiplos passos — um cenário perfeito para um prompt reutilizável!

- Criar a tarefa
- Atualizar a configuração do site para carregar a nova tarefa

### 📖 Teoria: Arquivos de Prompt

Arquivos de prompt (`*.prompt.md`) são prompts reutilizáveis para simplificar tarefas comuns e úteis no seu projeto. Eles são selecionados no Copilot Chat usando comandos slash (`/`).

Eles podem referenciar outros arquivos do workspace, arquivos de prompt ou arquivos de instrução usando links no estilo Markdown relativos à localização do arquivo de prompt.

O Visual Studio Code procura arquivos `*.prompt.md` no diretório `.github/prompts/` por [padrão](vscode://settings/chat.promptFilesLocations).

> [!TIP]
> Use arquivos de prompt para definir tarefas e fluxos de trabalho repetíveis.
>
> Ao escrever prompts, foque no **QUE** precisa ser feito. Você pode referenciar instruções para o **COMO**.

Consulte a página [VS Code Docs: Prompt Files](https://code.visualstudio.com/docs/copilot/copilot-customization#_prompt-files-experimental) para mais informações.

### ⌨️ Atividade: Criar um Prompt para Tarefas

Agora vamos criar um prompt reutilizável que automatiza todo o processo de criação de tarefas. Este é um caso perfeito para um arquivo de prompt, pois criar tarefas envolve múltiplos passos repetitivos que seguem o mesmo padrão toda vez — exatamente o tipo de fluxo de trabalho que se beneficia da automação.

1. Crie um novo arquivo chamado:

   ```text
   .github/prompts/new-assignment.prompt.md
   ```

1. Adicione o seguinte conteúdo para criar um prompt abrangente de geração de tarefas:

   ```markdown
   ---
   agent: agent
   description: Criar uma nova tarefa de programação
   argument-hint: Forneça os detalhes da tarefa
   ---

   # Criar Nova Tarefa de Programação

   Seu objetivo é gerar uma nova tarefa para os alunos da Mergington High School.

   ## Passo 1: Coletar Informações da Tarefa

   Se ainda não fornecido pelo usuário, pergunte sobre o que será a tarefa.

   ## Passo 2: Criar a Estrutura da Tarefa

   1. Crie um novo diretório na pasta `assignments` com um nome único baseado no tema da tarefa
   1. Crie um novo arquivo no diretório chamado `README.md` com a estrutura do arquivo [assignment-template.md](../../templates/assignment-template.md)
   1. Preencha os detalhes da tarefa no arquivo README
   1. (Opcional) Adicione código inicial ou anexos se a tarefa precisar — adicione esses arquivos na mesma pasta da tarefa

   ## Passo 3: Atualizar a Configuração do Site

   Atualize a lista de tarefas no arquivo de configuração do site [config.json](../../config.json) para incluir a nova tarefa. Para o campo dueDate, use a data atual mais 7 dias, a menos que especificado de outra forma.
   ```

### ⌨️ Atividade: Testar o Prompt de Tarefas

1. Abra o Copilot Chat no VS Code e certifique-se de estar no modo `Agent`.

1. Execute seu prompt digitando `/new-assignment` no campo de entrada do chat. Há 2 opções:

   - Digite apenas `/new-assignment` sem descrição. O Copilot perguntará sobre o que a tarefa deve ser.
   - Inclua o tema diretamente: `/new-assignment Construindo APIs REST com o framework FastAPI`

      <details>
      <summary>💡 Ideias de Temas para Tarefas</summary>

      ```text
      Processamento de Texto com Python - trabalhando com strings, I/O de arquivos e manipulação de texto
      ```

      ```text
      Estruturas de Dados em Python - listas, dicionários, sets e tuplas
      ```

      ```text
      Visualização de Dados com Python - usando matplotlib ou plotly para gráficos
      ```

      ```text
      Construindo APIs REST com o framework FastAPI
      ```

      ```text
      Estatística com Python - análise de dados e cálculos estatísticos usando pandas e numpy
      ```

      </details>

1. Verifique se a nova tarefa aparece na lista de tarefas no preview do site.

   <details>
   <summary>A tarefa não apareceu? 🔍</summary>

   Verifique os seguintes itens:

   - Atualize a página.
   - Um novo diretório foi criado em `assignments/`.
   - O arquivo `config.json` foi atualizado com a nova tarefa.

   </details>

1. Revise o conteúdo da tarefa gerada para garantir que corresponde às convenções estabelecidas.

1. Faça o commit e envie (push) suas alterações:

   - O novo arquivo de prompt: `.github/prompts/new-assignment.prompt.md`
   - O diretório e arquivos da tarefa gerada.
   - O `config.json` atualizado.

1. Aguarde a Mona preparar o próximo passo!

<details>
<summary>Está com problemas? 🤷</summary><br/>

- Certifique-se de que o arquivo de prompt está no diretório `.github/prompts/` com a extensão `.prompt.md`.

</details>
