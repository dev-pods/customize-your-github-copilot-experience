## Passo 2: Instruções Específicas para Arquivos

Com as instruções gerais do projeto prontas, você percebe que precisa de regras de formatação mais específicas relacionadas apenas às tarefas. Embora suas instruções gerais do repositório funcionem bem para padrões gerais de codificação, você não quer sobrecarregá-las com requisitos detalhados de estrutura de tarefas que são incluídos em todas as mensagens de chat.

Você quer garantir que todas as suas tarefas sigam o mesmo padrão e estrutura para que os estudantes tenham uma experiência consistente, mas essas regras devem se aplicar apenas quando trabalhando em arquivos de tarefas.

### 📖 Teoria: Arquivos de Instruções Personalizadas

Arquivos de instruções (`*.instructions.md`) fornecem ao Copilot orientações direcionadas para arquivos ou diretórios específicos em seu projeto.

Diferentemente das instruções gerais do repositório que se aplicam em todos os lugares, esses arquivos usam o campo `applyTo` no [frontmatter](https://jekyllrb.com/docs/front-matter/) usando [sintaxe glob](https://code.visualstudio.com/docs/editor/glob-patterns) para direcionar arquivos específicos. Isso aplica automaticamente as instruções sempre que o Copilot trabalha em arquivos que correspondem a esse padrão. Alternativamente, você pode anexar instruções manualmente usando o botão **Add Context** no Copilot Chat.

O Visual Studio Code procurará arquivos `*.instructions.md` no diretório `.github/instructions/` por [padrão](vscode://settings/chat.instructionsFilesLocations).

> [!TIP]
> As instruções devem focar em **COMO** uma tarefa deve ser feita - descrevendo as diretrizes, padrões e convenções usadas naquela parte específica do código

Veja a página [VS Code Docs: Custom Instructions](https://code.visualstudio.com/docs/copilot/copilot-customization#_custom-instructions) para mais informações.

### ⌨️ Atividade: Criar Instruções Específicas para Tarefas

Agora vamos criar instruções direcionadas especificamente para arquivos de tarefas para garantir que elas sigam estrutura e formatação consistentes.

1. Primeiro, vamos examinar o template de tarefa existente. Abra `templates/assignment-template.md` para ver a estrutura que queremos que todas as tarefas sigam.

1. Crie um novo arquivo chamado `.github/instructions/assignments.instructions.md`

1. Adicione o seguinte conteúdo para definir padrões de formatação de tarefas. Isso também garantirá que sejam aplicados automaticamente para cada solicitação de chat para arquivos Markdown (`.md`) no diretório `assignments`.

   ```markdown
   ---
   applyTo: "assignments/**/*.md"
   ---

   # Diretrizes de Estrutura Markdown para Tarefas

   Todos os arquivos markdown de tarefas devem seguir estas diretrizes:

   ## 1. Uso de Template

   - Arquivos markdown de tarefas devem seguir a estrutura em [`templates/assignment-template.md`](../../templates/assignment-template.md).
   - A tarefa deve ser criada como um arquivo `README.md`
   - Não remova ou pule seções obrigatórias do template.

   ## 2. Orientação de Seções

   Os cabeçalhos das seções devem refletir a estrutura no template, incluindo o uso exato de ícones.

   - **Título**: Substitua `[Assignment Title]` com um nome curto e descritivo (ex: `Python Básico`, `Loops e Condicionais`, `Funções e Módulos`).
   - **Objetivo**: Escreva 1-2 frases resumindo o que o estudante aprenderá ou realizará. Foque nas principais habilidades ou conceitos.
   - **Tarefas**: Para cada tarefa:
      - Use um nome de tarefa específico e orientado à ação
      - Na Descrição, declare claramente o que o estudante deve fazer.
      - Nos Requisitos, use pontos para listar os resultados ou recursos esperados. Seja específico e mensurável
      - Forneça exemplo de entrada/saída em blocos de código se útil.

   Não inclua seções extras a menos que explicitamente especificado.
   ```

### ⌨️ Atividade: Testar as Instruções de Tarefa

1. Abra o arquivo `assignments/games-in-python/README.md` no VS Code. Esta tarefa não corresponde a todas as convenções que você configurou como professor.

1. Reserve um momento para revisar a estrutura atual deste arquivo de tarefa. Note como ela difere da estrutura do template que você examinou anteriormente. Você também pode ver como ela aparece atualmente na aba **Site Preview**.

1. Com o arquivo de tarefa aberto, pergunte ao Copilot no modo `Agent` para atualizar a estrutura da tarefa:

   > ![Static Badge](https://img.shields.io/badge/-Prompt-text?style=social&logo=github%20copilot)
   >
   > ```prompt
   > Atualize este arquivo de tarefa para seguir os padrões do projeto e estrutura do template
   > ```

1. Observe como o Copilot referencia as instruções gerais do projeto e os arquivos de instruções específicos de tarefas.

   <img width="492" height="376" alt="screenshot of Copilot chat showing attached references" src="https://github.com/user-attachments/assets/dbf26be3-5940-4619-af4e-0a4380f16494" />

1. Compare as mudanças sugeridas com a estrutura do arquivo original para ver como o Copilot aplicou suas instruções. Aplique as mudanças sugeridas e verifique como a tarefa atualizada agora aparece no **Site Preview**.

1. Commit ambos os arquivos para a branch `main` e push suas mudanças para o GitHub.

   - `.github/instructions/assignments.instructions.md`
   - `assignments/games-in-python/README.md`

1. Aguarde a Mona preparar o próximo passo!

<details>
<summary>Tendo problemas? 🤷</summary><br/>

- Certifique-se de que você fez commit de ambos os arquivos para a branch `main`:
  - `.github/instructions/assignments.instructions.md`
  - `assignments/games-in-python/README.md`

</details>
