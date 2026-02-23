from __future__ import annotations
import asyncio
from collections import defaultdict, deque
from dataclasses import dataclass
from typing import Any

from .base_agent import AgentResponse
from .researcher import ResearcherAgent
from .coder import CoderAgent
from .analyst import AnalystAgent
from .browser import BrowserAgent
from .filesystem import FilesystemAgent
from .communicator import CommunicatorAgent
from .memory_agent import MemoryAgentAgent
from .critic import CriticAgent
from .tool_builder import ToolBuilderAgent
from .scheduler import SchedulerAgent


@dataclass
class PlanNode:
    id: str
    title: str
    agent: str
    deps: list[str]
    priority: int = 5


class Orchestrator:
    def __init__(self) -> None:
        self.world_state: dict[str, Any] = {'history': []}
        self.agents = {
            'researcher': ResearcherAgent(),
            'coder': CoderAgent(),
            'analyst': AnalystAgent(),
            'browser': BrowserAgent(),
            'filesystem': FilesystemAgent(),
            'communicator': CommunicatorAgent(),
            'memory_agent': MemoryAgentAgent(),
            'critic': CriticAgent(),
            'tool_builder': ToolBuilderAgent(),
            'scheduler': SchedulerAgent(),
        }

    def build_dag(self, goal: str) -> list[PlanNode]:
        return [
            PlanNode('n1', f'Investigate goal: {goal}', 'researcher', []),
            PlanNode('n2', 'Produce implementation artifacts', 'coder', ['n1']),
            PlanNode('n3', 'Run quality critique', 'critic', ['n2']),
        ]

    async def execute(self, goal: str) -> dict[str, Any]:
        dag = self.build_dag(goal)
        graph = {n.id: n for n in dag}
        indegree = defaultdict(int)
        children = defaultdict(list)
        for node in dag:
            for dep in node.deps:
                indegree[node.id] += 1
                children[dep].append(node.id)

        q = deque([n.id for n in dag if indegree[n.id] == 0])
        results: dict[str, AgentResponse] = {}

        while q:
            batch = list(q)
            q.clear()
            tasks = []
            for node_id in batch:
                node = graph[node_id]
                agent = self.agents[node.agent]
                task_payload = {'id': node.id, 'title': node.title, 'goal': goal, 'deps': node.deps}
                tasks.append((node_id, asyncio.create_task(agent.run(task_payload, self.world_state))))

            for node_id, t in tasks:
                resp = await t
                results[node_id] = resp
                self.world_state['history'].append(resp.output)
                for nxt in children[node_id]:
                    indegree[nxt] -= 1
                    if indegree[nxt] == 0:
                        q.append(nxt)

        return {
            'goal': goal,
            'status': 'completed',
            'steps': {k: v.output for k, v in results.items()},
            'world_state': self.world_state,
        }
