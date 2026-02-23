from __future__ import annotations
from typing import Any
from datetime import datetime
from .registry import registry, ToolSpec

def _default(name:str, payload:dict[str,Any])->dict[str,Any]:
    return {'tool': name, 'payload': payload, 'status': 'ok', 'timestamp': datetime.utcnow().isoformat()}

def query_database(payload: dict[str, Any]) -> dict[str, Any]:
    return _default('query_database', payload)

def analyze_csv(payload: dict[str, Any]) -> dict[str, Any]:
    return _default('analyze_csv', payload)

def plot_chart(payload: dict[str, Any]) -> dict[str, Any]:
    return _default('plot_chart', payload)

def run_regression(payload: dict[str, Any]) -> dict[str, Any]:
    return _default('run_regression', payload)

def train_classifier(payload: dict[str, Any]) -> dict[str, Any]:
    return _default('train_classifier', payload)

def evaluate_model(payload: dict[str, Any]) -> dict[str, Any]:
    return _default('evaluate_model', payload)

def merge_datasets(payload: dict[str, Any]) -> dict[str, Any]:
    return _default('merge_datasets', payload)

def clean_data(payload: dict[str, Any]) -> dict[str, Any]:
    return _default('clean_data', payload)

def register_tools() -> None:
    registry.register(ToolSpec(name='query_database', description='query database tool', schema={'type':'object','properties':{},'additionalProperties':True}, handler=query_database))
    registry.register(ToolSpec(name='analyze_csv', description='analyze csv tool', schema={'type':'object','properties':{},'additionalProperties':True}, handler=analyze_csv))
    registry.register(ToolSpec(name='plot_chart', description='plot chart tool', schema={'type':'object','properties':{},'additionalProperties':True}, handler=plot_chart))
    registry.register(ToolSpec(name='run_regression', description='run regression tool', schema={'type':'object','properties':{},'additionalProperties':True}, handler=run_regression))
    registry.register(ToolSpec(name='train_classifier', description='train classifier tool', schema={'type':'object','properties':{},'additionalProperties':True}, handler=train_classifier))
    registry.register(ToolSpec(name='evaluate_model', description='evaluate model tool', schema={'type':'object','properties':{},'additionalProperties':True}, handler=evaluate_model))
    registry.register(ToolSpec(name='merge_datasets', description='merge datasets tool', schema={'type':'object','properties':{},'additionalProperties':True}, handler=merge_datasets))
    registry.register(ToolSpec(name='clean_data', description='clean data tool', schema={'type':'object','properties':{},'additionalProperties':True}, handler=clean_data))
