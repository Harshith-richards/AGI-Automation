from typing import Any
from .base_agent import BaseAgent, AgentResponse


class CriticAgent(BaseAgent):
    name = 'critic'
    system_prompt = '''You are the critic agent for NEXUS-AGI. Operate autonomously with explicit reasoning, careful tool selection, and robust validation. For each request, restate objective, enumerate constraints, gather evidence, execute deterministic actions, and return structured JSON-friendly output. Evaluate failure modes, confidence, and safety. If unsure, provide bounded uncertainty and recovery steps. Ensure auditability by capturing inputs, actions, observations, and outputs. Optimize for reliability, latency awareness, and cost discipline. Align with policy: avoid harmful instructions, protect secrets, and prefer reversible changes. Collaborate with orchestrator through concise machine-readable messages and improvement notes.'''

    async def run(self, task: dict[str, Any], world_state: dict[str, Any]) -> AgentResponse:
        payload = self._base_payload(task, world_state)
        payload['deliverable'] = 'quality assessment and improvement actions'
        payload['summary'] = f"Executed {self.name} workflow for: {task.get('title', task.get('goal', 'untitled'))}"
        payload['actions'] = [
            'analyze-input',
            'select-tools',
            'execute',
            'validate-output',
            'report'
        ]
        return AgentResponse(success=True, output=payload, notes='completed')
