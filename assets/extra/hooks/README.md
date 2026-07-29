# 🪝 Hooks do Copilot — Guia para Desenvolvedores

Hooks são scripts que o GitHub Copilot executa **automaticamente** em momentos específicos do seu fluxo de trabalho, sem que você precise lembrar de rodá-los manualmente. Pense neles como "guardiões" que monitoram as ações do Copilot e podem aprovar, avisar ou bloquear uma ação antes que ela aconteça.

---

## 📂 Estrutura desta pasta

```
.github/hooks/
├── validate-assignment-structure.py   ← Script do hook (lógica de validação)
├── validate-assignment-structure.json ← Configuração (quando e como ativar o hook)
└── README.md                          ← Esta documentação
```

---

## 🔍 O que o hook de exemplo faz?

O hook **`validate-assignment-structure`** intercepta toda tentativa do Copilot de **criar um arquivo** (`create_file`) e verifica se ele está seguindo a estrutura correta do projeto.

**Regra validada:**
> Qualquer arquivo criado dentro da pasta `assignments/` deve ser um dos seguintes:
> `README.md`, `starter-code.py` ou `data.csv`.

**Exemplos de comportamento:**

| Arquivo que o Copilot tenta criar | Resultado |
|---|---|
| `assignments/minha-tarefa/README.md` | ✅ Aprovado |
| `assignments/minha-tarefa/starter-code.py` | ✅ Aprovado |
| `assignments/minha-tarefa/solucao.py` | ❌ Bloqueado com mensagem explicativa |
| `assets/css/styles.css` | ✅ Aprovado (fora de `assignments/`) |

---

## ⚡ Como o hook é ativado?

A ativação é definida no arquivo JSON de configuração:

```json
{
  "hooks": {
    "PreToolUse": [
      {
        "type": "command",
        "command": "python3 .github/hooks/validate-assignment-structure.py",
        "timeout": 8
      }
    ]
  }
}
```

- **`type: "PreToolUse"`** — o hook roda **antes** de a ferramenta ser executada.  
  Existe também `"PostToolUse"` para rodar **depois**.
- No schema acima, o filtro por ferramenta pode ser feito dentro do script, lendo `toolName` no payload.

O Copilot detecta automaticamente todos os arquivos `.json` nesta pasta e registra os hooks sem necessidade de configuração adicional.

---

## 🔄 Como o hook se comunica com o Copilot?

O fluxo de dados funciona assim:

```
Copilot tenta criar um arquivo
        ↓
Copilot envia o payload (JSON) via stdin para o script Python
        ↓
O script valida e imprime o resultado via stdout (JSON)
        ↓
Copilot lê o resultado e decide: prosseguir ou abortar
```

**Payload de entrada (recebido pelo script):**
```json
{
  "toolName": "create_file",
  "toolInput": {
    "filePath": "assignments/minha-tarefa/solucao.py",
    "content": "..."
  }
}
```

**Respostas possíveis do script:**

```json
{ "decision": "approve" }
```
```json
{ "decision": "approve", "message": "✅ Estrutura válida!" }
```
```json
{
  "decision": "block",
  "message": "❌ Arquivo bloqueado: 'solucao.py' não é um arquivo permitido em assignments/."
}
```

---

## 🛠️ Como criar seu próprio hook

1. **Crie o script** (Python, Node.js, shell, etc.):
   - Leia o payload do `stdin`
   - Implemente sua lógica de validação
   - Imprima o resultado em JSON para o `stdout`

2. **Crie o arquivo de configuração** `.json` na mesma pasta:
   ```json
   {
     "version": 1,
     "hooks": {
       "PreToolUse": [
         {
           "type": "command",
           "command": "python3 .github/hooks/meu-hook.py",
           "timeout": 8
         }
       ]
     }
   }
   ```

3. **Teste localmente** passando um payload de exemplo:
   ```bash
   echo '{"toolInput": {"filePath": "assignments/teste/solucao.py"}}' \
     | python3 .github/hooks/validate-assignment-structure.py
   ```

---

## 💡 Como hooks ajudam desenvolvedores?

| Problema comum | Como o hook ajuda |
|---|---|
| Copilot cria arquivos com nomes fora do padrão | Hook bloqueia e explica a convenção |
| Desenvolvedor esquece de seguir a estrutura do projeto | Hook lembra automaticamente, sem depender de revisão manual |
| Times com convenções diferentes | Hook documenta e aplica as regras de forma consistente |
| Code review lento por problemas triviais de estrutura | Hook elimina essa categoria de problema antes do commit |

> **Dica:** Hooks não substituem code review, mas eliminam erros simples e repetitivos antes que eles cheguem ao repositório.

---

## 📚 Saiba mais

- [Documentação oficial: Copilot Customization](https://docs.github.com/en/copilot)
- Explore também: `.github/instructions/` para instruções contextuais e `.github/agents/` para agentes customizados.

## Exemplo

Faça o prompt: "Crie o arquivo assignments/teste/solucao.py com uma função de exemplo."