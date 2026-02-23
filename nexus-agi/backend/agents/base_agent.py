from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime
from typing import Any


@dataclass
class AgentResponse:
    success: bool
    output: dict[str, Any]
    notes: str = ''
    confidence: float = 0.75
    created_at: datetime = field(default_factory=datetime.utcnow)


class BaseAgent:
    name = 'base'
    system_prompt = (
        'You are an autonomous specialist agent in the NEXUS-AGI platform. '
        'Always transform high-level objectives into explicit actions, track assumptions, '
        'execute tools safely, and produce structured output that upstream orchestrators can parse. '
        'Your reasoning must include: task understanding, decomposition, constraints, evidence, '
        'risk checks, and next actions. Never fabricate tool results. If data is missing, report '
        'uncertainty and suggest verifiable follow-ups. Keep outputs deterministic and machine-readable. '
        'Enforce policy and ethical boundaries, redact sensitive info, and attach confidence estimates '
        'grounded in evidence quality. When revising, compare old and new output and explain deltas.'
    )

    async def run(self, task: dict[str, Any], world_state: dict[str, Any]) -> AgentResponse:
        raise NotImplementedError

    def _base_payload(self, task: dict[str, Any], world_state: dict[str, Any]) -> dict[str, Any]:
        return {
            'agent': self.name,
            'task': task,
            'world_state_keys': sorted(world_state.keys()),
            'timestamp': datetime.utcnow().isoformat(),
        }
