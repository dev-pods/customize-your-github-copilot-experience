## Passo 1: Configurando Instruções do Copilot

Você é um professor na Mergington High School que cria tarefas de casa e exercícios de programação para estudantes. Você mantém um site estático para compartilhar essas tarefas e deseja estabelecer padrões gerais para assistentes de IA para garantir qualidade de código consistente e estrutura de projeto.

Você ouviu que as Instruções do Copilot podem ajudar com isso!

<details>
<summary>Screenshot do site 📸</summary><br/>

Você executará este site na primeira atividade!

<img width="600" alt="screenshot of homework website" src="https://github.com/user-attachments/assets/2383b6e9-64d5-4907-94b3-b67153efb008" />

</details>

### 📖 Teoria: O que são instruções personalizadas de repositório?

As instruções personalizadas de repositório permitem que você forneça ao Copilot orientações e preferências específicas do repositório que o ajudam a entender o contexto e padrões do seu projeto. Ao criar um arquivo `.github/copilot-instructions.md`, você pode garantir que as sugestões do Copilot sigam consistentemente as convenções e padrões de codificação do seu projeto.

O conjunto completo de instruções será automaticamente adicionado a todas as solicitações que você enviar ao Copilot Chat em seu repositório.

> [!TIP]
> Mantenha as instruções curtas e focadas no "como" do projeto. Isso pode incluir propósito, estrutura de pastas, padrões de codificação, ferramentas principais, formatos esperados, etc.

Veja a página [GitHub Docs: Repository Custom Instructions](https://docs.github.com/en/copilot/how-tos/custom-instructions/adding-repository-custom-instructions-for-github-copilot) para mais informações.

### ⌨️ Atividade: Explore o Projeto de Site Educacional

Para trabalhar com instruções personalizadas, vamos primeiro configurar nosso ambiente de desenvolvimento e explorar a estrutura do projeto.

1. Clique com o botão direito no botão abaixo para abrir a página **Create Codespace** em uma nova aba. Use a configuração padrão.

   [![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/{{full_repo_name}}?quickstart=1)

1. Confirme se o campo **Repository** é a sua cópia do exercício, não a original, então clique no botão verde **Create Codespace**.

   - ✅ Sua cópia: `/{{full_repo_name}}`
   - ❌ Original: `/skills/customize-your-github-copilot-experience`

1. Aguarde um momento para o Visual Studio Code carregar no seu navegador e para todas as extensões serem instaladas.

   - Certifique-se de que a extensão **Live Preview** está ativada.
   - Certifique-se de que a extensão **Python** está ativada.

1. Clique com o botão direito em `index.html` e selecione **Show Preview** para ver o site em ação.

   > ❕ **Importante**: Mantenha a aba de preview aberta para ver as atualizações ao vivo. Faremos edições durante todo o exercício.

1. Explore a estrutura do projeto:

   - Navegue pela pasta `assets/` para ver os recursos do site (CSS, JavaScript, imagens).
   - Olhe a pasta `assignments/` para entender os formatos de tarefas existentes.
   - Revise o `index.html` no diretório raiz para ver a estrutura principal do site.
   - Revise o `config.json` no diretório raiz para ver como as tarefas são configuradas.

### ⌨️ Atividade: Criar Instruções do Copilot para o Repositório

Agora que você explorou o projeto, vamos criar instruções personalizadas para ajudar o Copilot a entender seu projeto de site educacional.

1. No VS Code, crie um novo arquivo chamado `.github/copilot-instructions.md`

   > ❕ **Importante:** Certifique-se de que o nome do arquivo está correto. Este nome específico é necessário para o Copilot reconhecê-lo.

1. Adicione o seguinte conteúdo para que o Copilot entenda o propósito, estrutura e requisitos do projeto:

   ```markdown
   # Descrição do Projeto

   Este projeto é um site educacional para compartilhar tarefas de casa e exercícios de programação com estudantes. Os estudantes podem navegar, visualizar e baixar tarefas diretamente do portal.

   ## Estrutura do Projeto

   - [`assignments/`](../assignments/) Cada tarefa de casa é armazenada em sua própria subpasta com uma estrutura consistente.
   - [`templates/`](../templates/) Templates reutilizáveis para novo conteúdo
   - [`assets/`](../assets/) Contém os recursos do site incluindo CSS, JavaScript, imagens e arquivos de configuração
   - [`index.html`](../index.html) A página principal do site que serve como um portal estático para navegar e visualizar tarefas. O conteúdo é configurável através do arquivo [`config.json`](../config.json) para gerar dinamicamente listas e detalhes de tarefas.

   ## Diretrizes do Projeto

   - Manter estilo consistente em todas as páginas
   - Manter nomes de arquivos e pastas descritivos e organizados

   ## Padrões Educacionais

   Ao gerar conteúdo para este projeto:

   - **Focado em aprendizado**: Todo conteúdo deve ser projetado com objetivos de aprendizado claros e níveis de dificuldade apropriados
   - **Amigável para estudantes**: Use linguagem clara e encorajadora que motiva os estudantes
   ```

1. Teste suas instruções perguntando ao Copilot sobre o projeto:

   > ![Static Badge](https://img.shields.io/badge/-Prompt-text?style=social&logo=github%20copilot)
   >
   > ```prompt
   > Explique brevemente este projeto para mim
   > ```

1. Note que o Copilot usa suas instruções personalizadas como referência na resposta.

   <img width="504" height="183" alt="image" src="https://github.com/user-attachments/assets/2214ed9e-c165-4440-a23e-d2d33c0231a9" />

1. Commit o arquivo `.github/copilot-instructions.md` para a branch `main` e push para o GitHub.

1. Aguarde a Mona preparar o próximo passo!

<details>
<summary>Tendo problemas? 🤷</summary><br/>

- O arquivo `.github/copilot-instructions.md` deve estar na raiz da pasta `.github`
- Certifique-se de que você fez commit e push das mudanças.

</details>
