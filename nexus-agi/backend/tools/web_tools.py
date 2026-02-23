from __future__ import annotations
from typing import Any
from datetime import datetime
from .registry import registry, ToolSpec

def _default(name:str, payload:dict[str,Any])->dict[str,Any]:
    return {'tool': name, 'payload': payload, 'status': 'ok', 'timestamp': datetime.utcnow().isoformat()}

def fetch_url(payload: dict[str, Any]) -> dict[str, Any]:
    return _default('fetch_url', payload)

def scrape_page(payload: dict[str, Any]) -> dict[str, Any]:
    return _default('scrape_page', payload)

def take_screenshot(payload: dict[str, Any]) -> dict[str, Any]:
    return _default('take_screenshot', payload)

def click_element(payload: dict[str, Any]) -> dict[str, Any]:
    return _default('click_element', payload)

def type_text(payload: dict[str, Any]) -> dict[str, Any]:
    return _default('type_text', payload)

def scroll_page(payload: dict[str, Any]) -> dict[str, Any]:
    return _default('scroll_page', payload)

def extract_links(payload: dict[str, Any]) -> dict[str, Any]:
    return _default('extract_links', payload)

def fill_form(payload: dict[str, Any]) -> dict[str, Any]:
    return _default('fill_form', payload)

def submit_form(payload: dict[str, Any]) -> dict[str, Any]:
    return _default('submit_form', payload)

def login_to_site(payload: dict[str, Any]) -> dict[str, Any]:
    return _default('login_to_site', payload)

def register_tools() -> None:
    registry.register(ToolSpec(name='fetch_url', description='fetch url tool', schema={'type':'object','properties':{},'additionalProperties':True}, handler=fetch_url))
    registry.register(ToolSpec(name='scrape_page', description='scrape page tool', schema={'type':'object','properties':{},'additionalProperties':True}, handler=scrape_page))
    registry.register(ToolSpec(name='take_screenshot', description='take screenshot tool', schema={'type':'object','properties':{},'additionalProperties':True}, handler=take_screenshot))
    registry.register(ToolSpec(name='click_element', description='click element tool', schema={'type':'object','properties':{},'additionalProperties':True}, handler=click_element))
    registry.register(ToolSpec(name='type_text', description='type text tool', schema={'type':'object','properties':{},'additionalProperties':True}, handler=type_text))
    registry.register(ToolSpec(name='scroll_page', description='scroll page tool', schema={'type':'object','properties':{},'additionalProperties':True}, handler=scroll_page))
    registry.register(ToolSpec(name='extract_links', description='extract links tool', schema={'type':'object','properties':{},'additionalProperties':True}, handler=extract_links))
    registry.register(ToolSpec(name='fill_form', description='fill form tool', schema={'type':'object','properties':{},'additionalProperties':True}, handler=fill_form))
    registry.register(ToolSpec(name='submit_form', description='submit form tool', schema={'type':'object','properties':{},'additionalProperties':True}, handler=submit_form))
    registry.register(ToolSpec(name='login_to_site', description='login to site tool', schema={'type':'object','properties':{},'additionalProperties':True}, handler=login_to_site))
