## Passo 3: Construindo Prompts Reutilizáveis

Agora que você estabeleceu instruções para tarefas, você quer simplificar a criação de novas tarefas.

Criar tarefas é uma tarefa repetitiva que envolve múltiplos passos, um cenário perfeito para um prompt reutilizável!

- Criar a tarefa
- Atualizar a configuração do site para carregar a nova tarefa

### 📖 Teoria: Arquivos de Prompt

Arquivos de prompt (`*.prompt.md`) são prompts reutilizáveis para simplificar tarefas comuns e úteis em seu projeto. Eles são selecionados no Copilot Chat usando comandos de barra (`/`).

Eles podem referenciar outros arquivos do workspace, arquivos de prompt ou arquivos de instruções usando links estilo Markdown relativos à localização do arquivo de prompt.

O Visual Studio Code procurará arquivos `*.prompt.md` no diretório `.github/prompts/` por [padrão](vscode://settings/chat.promptFilesLocations).

> [!TIP]
> Use arquivos de prompt para definir tarefas e fluxos de trabalho repetitivos.
>
> Ao escrever prompts, foque em **O QUE** precisa ser feito. Você pode referenciar instruções para o **COMO**.

Veja a página [VS Code Docs: Prompt Files](https://code.visualstudio.com/docs/copilot/copilot-customization#_prompt-files-experimental) para mais informações.

### ⌨️ Atividade: Criar um Prompt de Tarefa

Agora vamos criar um prompt reutilizável que automatiza todo o processo de criação de tarefas. Isso é perfeito para um arquivo de prompt porque criar tarefas envolve múltiplos passos repetitivos que seguem o mesmo padrão toda vez - exatamente o tipo de fluxo de trabalho que se beneficia da automação.

1. Crie um novo arquivo chamado `.github/prompts/new-assignment.prompt.md`

1. Adicione o seguinte conteúdo para criar um prompt abrangente de geração de tarefas:

   ```markdown
   ---
   mode: agent
   description: Criar uma nova tarefa de programação
   ---

   # Criar Nova Tarefa de Programação

   Seu objetivo é gerar uma nova tarefa de casa para os estudantes da Mergington High School.

   ## Passo 1: Coletar Informações da Tarefa

   Se não for já fornecido pelo usuário, pergunte sobre o que será a tarefa.

   ## Passo 2: Criar Estrutura da Tarefa

   1. Crie um novo diretório na pasta `assignments` com um nome único baseado no tópico da tarefa
   1. Crie um novo arquivo no diretório chamado `README.md` com a estrutura do arquivo [assignment-template.md](../../templates/assignment-template.md)
   1. Preencha os detalhes da tarefa no arquivo README
   1. (Opcional) Adicione código inicial ou anexos se a tarefa precisar deles - adicione esses arquivos à mesma pasta da tarefa

   ## Passo 3: Atualizar Configuração do Site

   Atualize a lista de tarefas no arquivo de configuração do site [config.json](../../config.json) para incluir a nova tarefa. Para o campo dueDate, use a data atual mais 7 dias a menos que especificado de outra forma.
   ```

### ⌨️ Atividade: Testar o Prompt de Tarefa

1. Abra o Copilot Chat no VS Code e certifique-se de que está no modo `Agent`.

1. Execute seu prompt digitando `/new-assignment` no input do chat. Há 2 opções:

   - Digite apenas `/new-assignment` sem uma descrição. O Copilot perguntará sobre o que a tarefa deve ser.
   - Inclua o tópico diretamente: `/new-assignment Construindo APIs REST com framework FastAPI`

      <details>
      <summary>💡 Ideias de Tópicos de Tarefas</summary>

      ```text
      Processamento de Texto em Python - trabalhando com strings, I/O de arquivos e manipulação de texto
      ```

      ```text
      Estruturas de Dados em Python - listas, dicionários, conjuntos e tuplas
      ```

      ```text
      Visualização de Dados em Python - usando matplotlib ou plotly para gráficos e diagramas
      ```

      ```text
      Construindo APIs REST com framework FastAPI
      ```

      ```text
      Estatística com Python - análise de dados e cálculos estatísticos usando pandas e numpy
      ```

      </details>

1. Verifique se a nova tarefa aparece na lista de tarefas no preview do site.

   <details>
   <summary>Tarefa não aparecendo? 🔍</summary>

   Verifique estes itens:

   - Atualize a página.
   - Um novo diretório foi criado em `assignments/`.
   - O arquivo `config.json` foi atualizado com a nova tarefa.

   </details>

1. Revise o conteúdo da tarefa gerada para garantir que corresponde às suas convenções estabelecidas.

1. Commit e push suas mudanças:

   - O novo arquivo de prompt: `.github/prompts/new-assignment.prompt.md`
   - O diretório e arquivos da tarefa gerada.
   - `config.json` atualizado.

1. Aguarde a Mona preparar o próximo passo!

<details>
<summary>Tendo problemas? 🤷</summary><br/>

- Certifique-se de que o arquivo de prompt está no diretório `.github/prompts/` com a extensão `.prompt.md`.

</details>
