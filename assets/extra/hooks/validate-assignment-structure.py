#!/usr/bin/env python3
"""
Hook de Exemplo: Validador de Estrutura de Assignments
======================================================
Este hook é executado ANTES de o Copilot criar qualquer arquivo.
Ele verifica se arquivos criados dentro de `assignments/` seguem
a estrutura esperada do projeto.

Payload de entrada (stdin): JSON com os dados da ferramenta
Saída (stdout): JSON indicando se a ação deve prosseguir ou ser bloqueada

Formato de saída para compatibilidade entre runtimes (VS Code, Copilot CLI e cloud):
- permissionDecision: "allow", "deny" ou "ask"
- permissionDecisionReason: string (obrigatória quando "deny")
- hookSpecificOutput.permissionDecision: formato esperado pelo VS Code
- hookSpecificOutput.permissionDecisionReason: motivo no formato esperado pelo VS Code
"""

import json
import sys
import os

# Arquivos permitidos dentro de uma pasta de assignment
ALLOWED_FILENAMES = {"README.md", "starter-code.py", "data.csv"}

# Prefixo que identifica pastas de assignments
ASSIGNMENTS_PREFIX = "assignments/"


def build_decision(decision: str, reason: str = "") -> dict:
    """Gera saída compatível com VS Code e com runtimes que leem a raiz."""
    result = {"permissionDecision": decision}
    hook_specific_output = {"permissionDecision": decision}

    if reason:
        result["permissionDecisionReason"] = reason
        hook_specific_output["permissionDecisionReason"] = reason

    result["hookSpecificOutput"] = hook_specific_output
    return result


def is_inside_assignments(path: str) -> bool:
    """Retorna True quando o caminho aponta para algo dentro de assignments/."""
    normalized = path.replace("\\", "/")

    # Caso relativo comum: assignments/<nome-da-assignment>/arquivo
    if normalized.startswith(ASSIGNMENTS_PREFIX):
        return True

    # Caso absoluto: /.../assignments/<nome-da-assignment>/arquivo
    return "/assignments/" in normalized


def validate(payload: dict) -> dict:
    """
    Valida o payload recebido pelo Copilot antes de criar um arquivo.

    Retorna um dicionário com:
    - permissionDecision: "allow" para permitir, "deny" para bloquear
    - permissionDecisionReason: mensagem explicando a decisão quando houver bloqueio
    """
    # Executa somente para ferramentas que apontam explicitamente um arquivo de destino.
    # Isso evita depender de variações de nome da ferramenta no runtime.
    tool_name = str(payload.get("toolName") or payload.get("tool_name") or "")
    normalized_tool_name = tool_name.split(".")[-1].lower()

    # Suporta tanto camelCase quanto snake_case no payload.
    # Em alguns runtimes, tool_input pode chegar como string JSON ou outro tipo.
    tool_input = payload.get("toolInput") or payload.get("tool_input") or {}
    if isinstance(tool_input, str):
        try:
            tool_input = json.loads(tool_input)
        except json.JSONDecodeError:
            tool_input = {}
    if not isinstance(tool_input, dict):
        tool_input = {}

    file_path = tool_input.get("filePath") or tool_input.get("file_path") or ""

    # Alguns runtimes podem enviar o caminho em chaves alternativas.
    if not file_path:
        file_path = (
            tool_input.get("path")
            or tool_input.get("target")
            or tool_input.get("target_file")
            or ""
        )

    write_tools = {
        "create",
        "createfile",
        "create_file",
        "edit",
        "replace_string_in_file",
        "insert_edit_into_file",
        "delete_file",
        "move_file",
        "rename_file",
        "write",
        "applypatch",
        "apply_patch",
    }
    # Só valida chamadas de ferramentas claramente de escrita.
    if normalized_tool_name not in write_tools:
        return build_decision("allow")

    # Só valida arquivos dentro da pasta assignments/
    if not is_inside_assignments(file_path):
        return build_decision("allow")

    filename = os.path.basename(file_path)

    if filename not in ALLOWED_FILENAMES:
        return build_decision(
            "deny",
            (
                f"Arquivo bloqueado: '{filename}' não é um arquivo permitido "
                f"em assignments/. "
                f"Arquivos esperados: {', '.join(sorted(ALLOWED_FILENAMES))}."
            ),
        )

    return build_decision("allow")


def main():
    try:
        raw = sys.stdin.read()
        payload = json.loads(raw) if raw.strip() else {}
        result = validate(payload)
    except Exception:
        # Fail-open: erro interno do hook não deve bloquear execução da ferramenta.
        result = build_decision("allow")

    print(json.dumps(result))


if __name__ == "__main__":
    main()
