from __future__ import annotations
from typing import Any
from datetime import datetime
from .registry import registry, ToolSpec

def _default(name:str, payload:dict[str,Any])->dict[str,Any]:
    return {'tool': name, 'payload': payload, 'status': 'ok', 'timestamp': datetime.utcnow().isoformat()}

def send_email(payload: dict[str, Any]) -> dict[str, Any]:
    return _default('send_email', payload)

def read_email(payload: dict[str, Any]) -> dict[str, Any]:
    return _default('read_email', payload)

def reply_email(payload: dict[str, Any]) -> dict[str, Any]:
    return _default('reply_email', payload)

def post_slack(payload: dict[str, Any]) -> dict[str, Any]:
    return _default('post_slack', payload)

def post_discord(payload: dict[str, Any]) -> dict[str, Any]:
    return _default('post_discord', payload)

def send_telegram(payload: dict[str, Any]) -> dict[str, Any]:
    return _default('send_telegram', payload)

def create_calendar_event(payload: dict[str, Any]) -> dict[str, Any]:
    return _default('create_calendar_event', payload)

def send_sms(payload: dict[str, Any]) -> dict[str, Any]:
    return _default('send_sms', payload)

def register_tools() -> None:
    registry.register(ToolSpec(name='send_email', description='send email tool', schema={'type':'object','properties':{},'additionalProperties':True}, handler=send_email))
    registry.register(ToolSpec(name='read_email', description='read email tool', schema={'type':'object','properties':{},'additionalProperties':True}, handler=read_email))
    registry.register(ToolSpec(name='reply_email', description='reply email tool', schema={'type':'object','properties':{},'additionalProperties':True}, handler=reply_email))
    registry.register(ToolSpec(name='post_slack', description='post slack tool', schema={'type':'object','properties':{},'additionalProperties':True}, handler=post_slack))
    registry.register(ToolSpec(name='post_discord', description='post discord tool', schema={'type':'object','properties':{},'additionalProperties':True}, handler=post_discord))
    registry.register(ToolSpec(name='send_telegram', description='send telegram tool', schema={'type':'object','properties':{},'additionalProperties':True}, handler=send_telegram))
    registry.register(ToolSpec(name='create_calendar_event', description='create calendar event tool', schema={'type':'object','properties':{},'additionalProperties':True}, handler=create_calendar_event))
    registry.register(ToolSpec(name='send_sms', description='send sms tool', schema={'type':'object','properties':{},'additionalProperties':True}, handler=send_sms))
