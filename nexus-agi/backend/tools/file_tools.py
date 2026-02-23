from __future__ import annotations
from typing import Any
from datetime import datetime
from .registry import registry, ToolSpec

def _default(name:str, payload:dict[str,Any])->dict[str,Any]:
    return {'tool': name, 'payload': payload, 'status': 'ok', 'timestamp': datetime.utcnow().isoformat()}

def read_pdf(payload: dict[str, Any]) -> dict[str, Any]:
    return _default('read_pdf', payload)

def read_docx(payload: dict[str, Any]) -> dict[str, Any]:
    return _default('read_docx', payload)

def read_xlsx(payload: dict[str, Any]) -> dict[str, Any]:
    return _default('read_xlsx', payload)

def convert_to_pdf(payload: dict[str, Any]) -> dict[str, Any]:
    return _default('convert_to_pdf', payload)

def compress_files(payload: dict[str, Any]) -> dict[str, Any]:
    return _default('compress_files', payload)

def extract_zip(payload: dict[str, Any]) -> dict[str, Any]:
    return _default('extract_zip', payload)

def encrypt_file(payload: dict[str, Any]) -> dict[str, Any]:
    return _default('encrypt_file', payload)

def upload_to_s3(payload: dict[str, Any]) -> dict[str, Any]:
    return _default('upload_to_s3', payload)

def download_from_s3(payload: dict[str, Any]) -> dict[str, Any]:
    return _default('download_from_s3', payload)

def register_tools() -> None:
    registry.register(ToolSpec(name='read_pdf', description='read pdf tool', schema={'type':'object','properties':{},'additionalProperties':True}, handler=read_pdf))
    registry.register(ToolSpec(name='read_docx', description='read docx tool', schema={'type':'object','properties':{},'additionalProperties':True}, handler=read_docx))
    registry.register(ToolSpec(name='read_xlsx', description='read xlsx tool', schema={'type':'object','properties':{},'additionalProperties':True}, handler=read_xlsx))
    registry.register(ToolSpec(name='convert_to_pdf', description='convert to pdf tool', schema={'type':'object','properties':{},'additionalProperties':True}, handler=convert_to_pdf))
    registry.register(ToolSpec(name='compress_files', description='compress files tool', schema={'type':'object','properties':{},'additionalProperties':True}, handler=compress_files))
    registry.register(ToolSpec(name='extract_zip', description='extract zip tool', schema={'type':'object','properties':{},'additionalProperties':True}, handler=extract_zip))
    registry.register(ToolSpec(name='encrypt_file', description='encrypt file tool', schema={'type':'object','properties':{},'additionalProperties':True}, handler=encrypt_file))
    registry.register(ToolSpec(name='upload_to_s3', description='upload to s3 tool', schema={'type':'object','properties':{},'additionalProperties':True}, handler=upload_to_s3))
    registry.register(ToolSpec(name='download_from_s3', description='download from s3 tool', schema={'type':'object','properties':{},'additionalProperties':True}, handler=download_from_s3))
