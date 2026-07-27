## Passo 3: Construindo Reusable Skills

Agora que você definiu instruções para as tarefas, você quer agilizar a criação de novas tarefas.

Criar assignments é uma tarefa repetitiva e envolve várias etapas, um cenário perfeito para uma reusable skill!

- Criar o conteúdo da assignment
- Registrar no config do website
- Anexar starter code ou data files

### 📖 Teoria: Agent Skills

Agent Skills são um [open standard](https://agentskills.io/) para dar aos AI agents capacidades e workflows especializados. Uma skill é uma pasta contendo um arquivo `SKILL.md` com metadata e instruções, além de scripts, references e outros recursos opcionais.

```text
skill-name/
├── SKILL.md          # Required: metadata + instructions
├── scripts/          # Optional: executable code
├── references/       # Optional: documentation
```

Agents descobrem skills automaticamente por meio de **progressive disclosure**:

1. **Discovery**: Na inicialização, os agents carregam apenas `name` e `description` da skill.
1. **Activation**: Quando uma tarefa corresponde à descrição da skill, o agent lê as instruções completas de `SKILL.md`.
1. **Resources**: Arquivos adicionais (references, scripts) são carregados somente quando necessário.

Isso significa que você pode ter muitas skills instaladas sem deixar tudo mais lento: apenas o que for relevante é carregado no contexto.

As skills são ativadas de duas formas: **automaticamente**, quando o Copilot relaciona sua solicitação à descrição de uma skill, ou **explicitamente** via slash command (`/skill-name`). Como os agents dependem de `name` e `description` para decidir quais skills ativar, escrever uma descrição clara e específica é essencial.

Por padrão, o Visual Studio Code descobre skills no diretório `.github/skills/`.

> [!TIP]
> Escreva uma `description` clara no frontmatter para que o agent saiba **quando** usar a skill. Referencie arquivos adicionais para templates, exemplos e documentação detalhada.

Consulte o [VS Code Docs: Agent Skills](https://code.visualstudio.com/docs/copilot/customization/agent-skills) para mais informações.

### ⌨️ Atividade: Criar o Skill Skeleton

Vamos começar criando a estrutura completa de diretórios da skill e seu arquivo principal `SKILL.md`. Vamos criar todos os diretórios desde já, incluindo `references/` e `scripts/`, para que tudo esteja pronto à medida que adicionarmos arquivos nas próximas atividades.

1. Crie a estrutura de diretórios da skill com todos os subdiretórios:

   ```text
   .github/skills/new-assignment/
   .github/skills/new-assignment/references/
   .github/skills/new-assignment/scripts/
   ```

1. Crie o arquivo principal da skill:

   ```text
   .github/skills/new-assignment/SKILL.md
   ```

1. Adicione o conteúdo abaixo. O frontmatter `name` e `description` é o que o agent vê no momento de discovery para decidir se deve ativar a skill. O corpo fornece o workflow que o agent segue após a ativação.

   ```markdown
   ---
   name: new-assignment
   description: Crie uma nova programming homework assignment para estudantes da Mergington High School. Use esta skill sempre que o usuário quiser criar, adicionar, scaffoldar ou gerar uma nova assignment, exercise ou homework, mesmo que não use explicitamente a palavra "assignment".
   ---

   # Criar Nova Tarefa de Programação

   Assignments ficam em `assignments/<id>/`, e o website lê `config.json` para exibi-las. Siga estas etapas para criar ambos.

   ## Etapa 1: Coletar Requisitos

   Se o usuário não tiver especificado, pergunte qual conceito de programação a assignment deve cobrir.

   > 📖 Leia [references/assignment-guide.md](references/assignment-guide.md) para guidance sobre dificuldade, escopo e quando incluir starter code.

   ## Etapa 2: Criar a Assignment

   1. Crie `assignments/<kebab-case-id>/README.md` seguindo o [assignment template](../../../templates/assignment-template.md)
   2. (Opcional) Adicione starter code ou data files no mesmo diretório

   ## Etapa 3: Registrar no Website

   Use os bundled scripts, NÃO edite `config.json` manualmente.

   **Registrar a assignment:**

       node .github/skills/new-assignment/scripts/update-config.js <id> "<title>" "<description>"

   **Registrar cada arquivo como attachment** (starter code, data files etc.):

       node .github/skills/new-assignment/scripts/add-attachment.js <id> "<display-name>" <filename> <type>

   Tipos comuns: `python`, `csv`, `json`, `txt`, `html`

   ## Etapa 4: Verificar

   Confirme que a assignment foi registrada corretamente: verifique se `config.json` contém a nova entrada e se todos os arquivos criados existem em disco.
   ```

   Note como `SKILL.md` referencia dois outros diretórios, `references/` e `scripts/`, que ainda não criamos. Esse é o padrão de progressive disclosure em ação: o agent só carrega esses arquivos quando chega a uma etapa que precisa deles.

### ⌨️ Atividade: Adicionar um Reference Guide

Vamos preencher o diretório `references/` com domain knowledge que o agent pode consultar quando necessário. O `SKILL.md` aponta para `references/assignment-guide.md` para que o agent possa ler quando decidir dificuldade e escopo, mas somente quando realmente precisar desse contexto.

1. Crie o arquivo de referência:

   ```text
   .github/skills/new-assignment/references/assignment-guide.md
   ```

1. Adicione o conteúdo abaixo para fornecer orientação pedagógica ao agent:

   ```markdown
   # Assignment Design Guide

   Orientações para desenhar conteúdo de assignment: o que ensinar e como definir o escopo. Para formatação e estrutura markdown, os instruction files do projeto já tratam isso automaticamente.

   ## Difficulty & Scope

   - Defina 2–4 tasks por assignment que evoluam entre si
   - Comece com algo que um aluno consiga terminar em menos de 10 minutos e depois aumente a complexidade
   - A última task pode ser um stretch goal, mas as anteriores devem construir confiança
   - Foque em um core concept por assignment (ex.: "loops", não "loops + file I/O + error handling")

   ## Starter Code

   Inclua starter code quando:

   - The assignment needs boilerplate the student shouldn't write from scratch
   - You want students to follow a specific function signature or structure

   Evite quando o objetivo for escrever algo do zero (ex.: "write a script that...").

   ## Exemplos de Tópicos por Dificuldade

   - **Beginner**: variables, conditionals, loops, string formatting
   - **Intermediate**: functions, lists/dicts, file I/O, basic classes
   - **Advanced**: APIs, data analysis, testing, web frameworks
   ```

   Ao separar isso de `SKILL.md`, mantemos as instruções principais focadas em _workflow_, enquanto este arquivo fornece _domain knowledge_. O agent só lê esse conteúdo quando chega à etapa de gather requirements.

### ⌨️ Atividade: Adicionar Bundled Scripts

Skills podem incluir scripts para tarefas determinísticas que são tratadas melhor por código do que por AI. Nossa skill precisa de dois scripts: um para registrar a assignment em `config.json` e outro para anexar arquivos (starter code, datasets etc.) a ela. Fazer o agent executar esses scripts garante updates de config consistentes e sem erro sempre.

1. Crie o primeiro script, que registra uma nova assignment:

   ```text
   .github/skills/new-assignment/scripts/update-config.js
   ```

   Adicione o conteúdo abaixo:

   ```javascript
   const fs = require("fs");
   const path = require("path");

   const [id, title, description] = process.argv.slice(2);
   const configPath = path.resolve(__dirname, "../../../../config.json");
   const config = JSON.parse(fs.readFileSync(configPath, "utf8"));

   if (!id || !title || !description) {
     console.error(
       'Usage: node .github/skills/new-assignment/scripts/update-config.js <id> "<title>" "<description>"',
     );
     process.exit(1);
   }

   const dueDate = new Date(Date.now() + 7 * 24 * 60 * 60 * 1000).toISOString().split("T")[0];

   config.assignments.push({
     id,
     title,
     description,
     path: `assignments/${id}`,
     dueDate,
   });

   fs.writeFileSync(configPath, JSON.stringify(config, null, 2) + "\n");
   console.log(`Added "${title}" (due ${dueDate})`);
   ```

   Esse script cuida do cálculo da due date e da estrutura exata do JSON, pontos que são tediosos e propensos a erro para uma AI acertar sempre.

1. Crie um segundo script para anexar arquivos a uma assignment existente:

   ```text
   .github/skills/new-assignment/scripts/add-attachment.js
   ```

   Adicione o conteúdo abaixo:

   ```javascript
   const fs = require("fs");
   const path = require("path");

   const [assignmentId, displayName, filename, type] = process.argv.slice(2);

   if (!assignmentId || !displayName || !filename || !type) {
     console.error(
       'Usage: node add-attachment.js <assignment-id> "<display-name>" <filename> <type>',
     );
     console.error(
       'Example: node add-attachment.js python-basics "Starter Code" starter-code.py python',
     );
     process.exit(1);
   }

   const repoRoot = path.resolve(__dirname, "../../../../");
   const configPath = path.join(repoRoot, "config.json");
   const filePath = path.join(repoRoot, "assignments", assignmentId, filename);

   // Verify the file exists on disk
   if (!fs.existsSync(filePath)) {
     console.error(`Error: File not found: assignments/${assignmentId}/${filename}`);
     process.exit(1);
   }

   const config = JSON.parse(fs.readFileSync(configPath, "utf8"));
   const assignment = config.assignments.find((a) => a.id === assignmentId);

   if (!assignment) {
     console.error(`Error: Assignment "${assignmentId}" not found in config.json`);
     console.error("Available IDs:", config.assignments.map((a) => a.id).join(", "));
     process.exit(1);
   }

   // Create attachments array if it doesn't exist
   if (!assignment.attachments) {
     assignment.attachments = [];
   }

   // Skip if an attachment with the same filename already exists
   const existing = assignment.attachments.find((a) => a.file === filename);
   if (existing) {
     console.log(`Skipped: "${filename}" is already attached to "${assignmentId}"`);
     process.exit(0);
   }

   assignment.attachments.push({
     name: displayName,
     file: filename,
     type: type,
   });

   fs.writeFileSync(configPath, JSON.stringify(config, null, 2) + "\n");
   console.log(`Added "${displayName}" (${filename}) to assignment "${assignmentId}"`);
   ```

   Esse segundo script valida se o arquivo realmente existe, evita attachments duplicados e produz error messages claras, tudo isso deixa a skill mais robusta quando o agent a executa.

1. Revise a estrutura final da skill. Ela deve ficar assim:

   ```text
   .github/skills/new-assignment/
   ├── SKILL.md                          # Workflow the agent follows
   ├── references/
   │   └── assignment-guide.md           # Domain knowledge (loaded on demand)
   └── scripts/
       ├── update-config.js              # Registers new assignments
       └── add-attachment.js             # Attaches files to assignments
   ```

   Cada parte da skill tem um papel claro:
   - **`SKILL.md`** — o playbook do agent: quais etapas seguir e quando carregar outros recursos
   - **`references/`** — background knowledge que ajuda o agent a tomar melhores decisões
   - **`scripts/`** — operações determinísticas tratadas por código em vez de geração por AI

### ⌨️ Atividade: Testar a Assignment Skill

1. Abra o Copilot Chat no VS Code e certifique-se de estar no modo `Agent`.

1. Peça ao Copilot para criar uma nova assignment usando um prompt em linguagem natural. Como a skill tem uma `description` clara, o Copilot vai associar automaticamente sua solicitação e ativá-la.

   > ![Static Badge](https://img.shields.io/badge/-Prompt-text?style=social&logo=github%20copilot)
   >
   > ```prompt
   > Crie uma nova assignment sobre Building REST APIs com FastAPI framework
   > ```

   > 💡 **Tip:** Você também pode invocar a skill explicitamente com o slash command `/new-assignment` no input do chat.

      <details>
      <summary>💡 Ideias de Temas para Tarefas</summary>

   ```text
   Python Text Processing - working with strings, file I/O, and text manipulation
   ```

   ```text
   Data Structures in Python - lists, dictionaries, sets, and tuples
   ```

   ```text
   Python Data Visualization - using matplotlib or plotly for charts and graphs
   ```

   ```text
   Building REST APIs with FastAPI framework
   ```

   ```text
   Statistics with Python - data analysis and statistical calculations using pandas and numpy
   ```

      </details>

1. O Copilot vai ler a skill, criar a assignment e executar os bundled scripts.

   <img width="380" alt="Copilot reading the new-assignment SKILL.md file" src="https://github.com/gabrielhartog-invillia/skills-customize-your-github-copilot-experience/blob/main/.github/images/skill-being-used.png?raw=true" />

   Aceite os prompts de confirmação para permitir que ele continue.

   <img width="380" alt="Copilot asking for confirmation to run node scripts" src="https://github.com/gabrielhartog-invillia/skills-customize-your-github-copilot-experience/blob/main/.github/images/node-confirmation.png?raw=true" />

1. Verifique se a nova assignment aparece na lista de assignments no preview do website.

   <details>
   <summary>A tarefa não apareceu? 🔍</summary>

   Verifique estes itens:
   - Faça refresh da página.
   - Um novo diretório foi criado em `assignments/`.
   - O arquivo `config.json` foi atualizado com a nova assignment.

   </details>

1. Revise o conteúdo da tarefa gerada para garantir que corresponde às convenções estabelecidas.

1. Faça commit e push das suas alterações:
   - O novo diretório da skill: `.github/skills/new-assignment/` (incluindo `SKILL.md`, `references/` e `scripts/`)
   - O diretório e os arquivos da assignment gerada.
   - A configuração atualizada de `config.json`.

1. Aguarde a Mona preparar o próximo passo!

<details>
<summary>Está com problemas? 🤷</summary><br/>

- Verifique se a skill está no diretório `.github/skills/new-assignment/` com o arquivo `SKILL.md`.
- O campo `name` no frontmatter de `SKILL.md` precisa corresponder ao nome do diretório pai (`new-assignment`).
- Se a skill não aparecer no menu `/`, recarregue a janela do VS Code.

</details>
