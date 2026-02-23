from __future__ import annotations
from typing import Any
from datetime import datetime
from .registry import registry, ToolSpec

def _default(name:str, payload:dict[str,Any])->dict[str,Any]:
    return {'tool': name, 'payload': payload, 'status': 'ok', 'timestamp': datetime.utcnow().isoformat()}

def run_python(payload: dict[str, Any]) -> dict[str, Any]:
    return _default('run_python', payload)

def run_javascript(payload: dict[str, Any]) -> dict[str, Any]:
    return _default('run_javascript', payload)

def run_bash(payload: dict[str, Any]) -> dict[str, Any]:
    return _default('run_bash', payload)

def run_sql(payload: dict[str, Any]) -> dict[str, Any]:
    return _default('run_sql', payload)

def lint_code(payload: dict[str, Any]) -> dict[str, Any]:
    return _default('lint_code', payload)

def format_code(payload: dict[str, Any]) -> dict[str, Any]:
    return _default('format_code', payload)

def write_file(payload: dict[str, Any]) -> dict[str, Any]:
    return _default('write_file', payload)

def read_file(payload: dict[str, Any]) -> dict[str, Any]:
    return _default('read_file', payload)

def git_commit(payload: dict[str, Any]) -> dict[str, Any]:
    return _default('git_commit', payload)

def git_push(payload: dict[str, Any]) -> dict[str, Any]:
    return _default('git_push', payload)

def create_repo(payload: dict[str, Any]) -> dict[str, Any]:
    return _default('create_repo', payload)

def register_tools() -> None:
    registry.register(ToolSpec(name='run_python', description='run python tool', schema={'type':'object','properties':{},'additionalProperties':True}, handler=run_python))
    registry.register(ToolSpec(name='run_javascript', description='run javascript tool', schema={'type':'object','properties':{},'additionalProperties':True}, handler=run_javascript))
    registry.register(ToolSpec(name='run_bash', description='run bash tool', schema={'type':'object','properties':{},'additionalProperties':True}, handler=run_bash))
    registry.register(ToolSpec(name='run_sql', description='run sql tool', schema={'type':'object','properties':{},'additionalProperties':True}, handler=run_sql))
    registry.register(ToolSpec(name='lint_code', description='lint code tool', schema={'type':'object','properties':{},'additionalProperties':True}, handler=lint_code))
    registry.register(ToolSpec(name='format_code', description='format code tool', schema={'type':'object','properties':{},'additionalProperties':True}, handler=format_code))
    registry.register(ToolSpec(name='write_file', description='write file tool', schema={'type':'object','properties':{},'additionalProperties':True}, handler=write_file))
    registry.register(ToolSpec(name='read_file', description='read file tool', schema={'type':'object','properties':{},'additionalProperties':True}, handler=read_file))
    registry.register(ToolSpec(name='git_commit', description='git commit tool', schema={'type':'object','properties':{},'additionalProperties':True}, handler=git_commit))
    registry.register(ToolSpec(name='git_push', description='git push tool', schema={'type':'object','properties':{},'additionalProperties':True}, handler=git_push))
    registry.register(ToolSpec(name='create_repo', description='create repo tool', schema={'type':'object','properties':{},'additionalProperties':True}, handler=create_repo))
