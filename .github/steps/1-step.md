## Passo 1: Configurando as Instruções do Copilot

Você é professor(a) na Mergington High School e cria tarefas e exercícios de programação para os alunos. Você mantém um site estático para compartilhar essas tarefas e quer estabelecer padrões gerais para assistentes de IA, garantindo qualidade e estrutura consistentes no código do projeto.

Você ouviu dizer que as Copilot Instructions podem ajudar com isso!

<details>
<summary>Captura de tela do site 📸</summary><br/>

Você vai executar este site na primeira atividade!

<img width="600" alt="screenshot of homework website" src="https://github.com/user-attachments/assets/2383b6e9-64d5-4907-94b3-b67153efb008" />

</details>

### 📖 Teoria: O que são instruções personalizadas de repositório?

As instruções personalizadas de repositório permitem fornecer ao Copilot orientações e preferências específicas do repositório que o ajudam a entender o contexto e os padrões do seu projeto. Ao criar um arquivo `.github/copilot-instructions.md`, você garante que as sugestões do Copilot sigam consistentemente as convenções e padrões de código do seu projeto.

O conjunto completo de instruções será adicionado automaticamente a todas as solicitações que você enviar ao Copilot Chat no seu repositório.

> [!TIP]
> Mantenha as instruções curtas e focadas no "como" do projeto. Isso pode incluir propósito, estrutura de pastas, padrões de código, ferramentas principais, formatos esperados, etc.

Consulte a página [GitHub Docs: Repository Custom Instructions](https://docs.github.com/en/copilot/how-tos/custom-instructions/adding-repository-custom-instructions-for-github-copilot) para mais informações.

### ⌨️ Atividade: Explorar o Projeto do Site Educacional

Para trabalhar com instruções personalizadas, vamos primeiro configurar nosso ambiente de desenvolvimento e explorar a estrutura do projeto.

1. Clique com o botão direito no botão abaixo para abrir a página **Create Codespace** em uma nova aba. Use a configuração padrão.

   [![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/{{full_repo_name}}?quickstart=1)

1. Confirme que o campo **Repository** é a sua cópia do exercício, não o original, e clique no botão verde **Create Codespace**.

   - ✅ Sua cópia: `/{{full_repo_name}}`
   - ❌ Original: `/skills/customize-your-github-copilot-experience`

1. Aguarde um momento para o Visual Studio Code carregar no seu navegador e todas as extensões serem instaladas.

   - Certifique-se de que a extensão **Live Preview** está ativada.
   - Certifique-se de que a extensão **Python** está ativada.

1. Clique com o botão direito em `index.html` e selecione **Show Preview** para ver o site em funcionamento.

   > ❕ **Importante**: Mantenha a aba de preview aberta para ver as atualizações em tempo real. Faremos edições ao longo de todo o exercício.

1. Explore a estrutura do projeto:

   - Navegue pela pasta `assets/` para ver os recursos do site (CSS, JavaScript, imagens).
   - Veja a pasta `assignments/` para entender os formatos de tarefas existentes.
   - Revise o `index.html` no diretório raiz para ver a estrutura principal do site.
   - Revise o `config.json` no diretório raiz para ver como as tarefas estão configuradas.

### ⌨️ Atividade: Criar Instruções de Repositório para o Copilot

Agora que você explorou o projeto, vamos criar instruções personalizadas para ajudar o Copilot a entender seu projeto de site educacional.

1. No VS Code, crie um novo arquivo chamado:

   ```text
   .github/copilot-instructions.md
   ``` 

   > ❕ **Importante:** Certifique-se de que o nome do arquivo está correto. Este nome de arquivo específico é necessário para que o Copilot o reconheça.

1. Adicione o seguinte conteúdo para que o Copilot entenda o propósito, a estrutura e os requisitos do projeto:

   ```markdown
   # Descrição do Projeto

   Este projeto é um site educacional para compartilhar tarefas e exercícios de programação com os alunos. Os alunos podem navegar, visualizar e baixar tarefas diretamente pelo portal.

   ## Estrutura do Projeto

   - [`assignments/`](../assignments/) Cada tarefa é armazenada em sua própria subpasta com uma estrutura consistente.
   - [`templates/`](../templates/) Templates reutilizáveis para novo conteúdo
   - [`assets/`](../assets/) Contém os recursos do site incluindo CSS, JavaScript, imagens e arquivos de configuração
   - [`index.html`](../index.html) A página principal do site que serve como um portal estático para navegar e visualizar tarefas. O conteúdo é configurável via arquivo [`config.json`](../config.json) para gerar dinamicamente listas e detalhes das tarefas.

   ## Diretrizes do Projeto

   - Manter estilo consistente em todas as páginas
   - Manter nomes de arquivos e pastas descritivos e organizados

   ## Padrões Educacionais

   Ao gerar conteúdo para este projeto:

   - **Foco no aprendizado**: Todo conteúdo deve ser elaborado com objetivos de aprendizado claros e níveis de dificuldade apropriados
   - **Amigável ao aluno**: Usar linguagem clara e encorajadora que motive os alunos
   ```

1. Teste suas instruções perguntando ao Copilot sobre o projeto:

   > ![Static Badge](https://img.shields.io/badge/-Prompt-text?style=social&logo=github%20copilot)
   >
   > ```prompt
   > Explique brevemente este projeto para mim
   > ```

1. Observe que o Copilot usa suas instruções personalizadas como referência na resposta.

   <img width="504" height="183" alt="image" src="https://github.com/user-attachments/assets/2214ed9e-c165-4440-a23e-d2d33c0231a9" />

1. Faça o commit do arquivo `.github/copilot-instructions.md` na branch `main` e envie (push) para o GitHub.

1. Aguarde a Mona preparar o próximo passo!

<details>
<summary>Está com problemas? 🤷</summary><br/>

- O arquivo `.github/copilot-instructions.md` deve estar na raiz da pasta `.github`
- Certifique-se de que você fez o commit e o push das alterações.

</details>
