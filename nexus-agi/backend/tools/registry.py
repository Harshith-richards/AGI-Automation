from __future__ import annotations
from dataclasses import dataclass
from typing import Any, Callable


@dataclass
class ToolSpec:
    name: str
    description: str
    schema: dict[str, Any]
    handler: Callable[[dict[str, Any]], Any]
    version: str = '1.0.0'
    success: int = 0
    failure: int = 0


class ToolRegistry:
    def __init__(self) -> None:
        self.tools: dict[str, ToolSpec] = {}

    def register(self, spec: ToolSpec) -> None:
        self.tools[spec.name] = spec

    def list(self) -> list[dict[str, Any]]:
        return [
            {
                'name': t.name,
                'description': t.description,
                'schema': t.schema,
                'version': t.version,
                'success_rate': t.success / (t.success + t.failure) if (t.success + t.failure) else 1.0,
            }
            for t in self.tools.values()
        ]

    def execute(self, name: str, payload: dict[str, Any]) -> Any:
        if name not in self.tools:
            raise KeyError(f'Unknown tool: {name}')
        spec = self.tools[name]
        try:
            out = spec.handler(payload)
            spec.success += 1
            return out
        except Exception:
            spec.failure += 1
            raise


registry = ToolRegistry()
