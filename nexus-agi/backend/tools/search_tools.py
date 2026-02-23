from __future__ import annotations
from typing import Any
from datetime import datetime
from .registry import registry, ToolSpec

def _default(name:str, payload:dict[str,Any])->dict[str,Any]:
    return {'tool': name, 'payload': payload, 'status': 'ok', 'timestamp': datetime.utcnow().isoformat()}

def web_search(payload: dict[str, Any]) -> dict[str, Any]:
    return _default('web_search', payload)

def news_search(payload: dict[str, Any]) -> dict[str, Any]:
    return _default('news_search', payload)

def academic_search(payload: dict[str, Any]) -> dict[str, Any]:
    return _default('academic_search', payload)

def image_search(payload: dict[str, Any]) -> dict[str, Any]:
    return _default('image_search', payload)

def youtube_search(payload: dict[str, Any]) -> dict[str, Any]:
    return _default('youtube_search', payload)

def reddit_search(payload: dict[str, Any]) -> dict[str, Any]:
    return _default('reddit_search', payload)

def wikipedia_lookup(payload: dict[str, Any]) -> dict[str, Any]:
    return _default('wikipedia_lookup', payload)

def arxiv_search(payload: dict[str, Any]) -> dict[str, Any]:
    return _default('arxiv_search', payload)

def register_tools() -> None:
    registry.register(ToolSpec(name='web_search', description='web search tool', schema={'type':'object','properties':{},'additionalProperties':True}, handler=web_search))
    registry.register(ToolSpec(name='news_search', description='news search tool', schema={'type':'object','properties':{},'additionalProperties':True}, handler=news_search))
    registry.register(ToolSpec(name='academic_search', description='academic search tool', schema={'type':'object','properties':{},'additionalProperties':True}, handler=academic_search))
    registry.register(ToolSpec(name='image_search', description='image search tool', schema={'type':'object','properties':{},'additionalProperties':True}, handler=image_search))
    registry.register(ToolSpec(name='youtube_search', description='youtube search tool', schema={'type':'object','properties':{},'additionalProperties':True}, handler=youtube_search))
    registry.register(ToolSpec(name='reddit_search', description='reddit search tool', schema={'type':'object','properties':{},'additionalProperties':True}, handler=reddit_search))
    registry.register(ToolSpec(name='wikipedia_lookup', description='wikipedia lookup tool', schema={'type':'object','properties':{},'additionalProperties':True}, handler=wikipedia_lookup))
    registry.register(ToolSpec(name='arxiv_search', description='arxiv search tool', schema={'type':'object','properties':{},'additionalProperties':True}, handler=arxiv_search))
