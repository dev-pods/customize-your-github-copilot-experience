# `copilot-instructions.md` vs Copilot Memory

## `copilot-instructions.md`
- Arquivo versionado **no repositório** (`.github/copilot-instructions.md`)
- Escopo: **projeto/repositório** — aplica a todos que usam o repo
- Define contexto do projeto, padrões de código, convenções, arquitetura
- Carregado automaticamente em toda conversa dentro do workspace
- Ideal para: stack do projeto, estrutura de pastas, padrões de commit, regras de negócio

## Copilot Memory (`/memories/`)
- Armazenado **localmente na máquina do usuário**, fora do repositório
- Escopo: **pessoal** — só você vê, não é versionado nem compartilhado
- Persiste entre conversas e workspaces diferentes
- Subescopos:
  - `/memories/` — preferências pessoais globais (ex: `code-preferences.md`)
  - `/memories/repo/` — notas sobre o repositório atual
  - `/memories/session/` — contexto temporário da conversa atual

## Resumo

| | `copilot-instructions.md` | Memory |
|---|---|---|
| Versionado no Git | Sim | Não |
| Compartilhado com o time | Sim | Não |
| Persiste entre sessões | Sim | Sim (exceto `session/`) |
| Escopo | Repositório | Pessoal / Máquina |

**Regra geral:** use `copilot-instructions.md` para regras do projeto e memory para preferências pessoais de trabalho.
