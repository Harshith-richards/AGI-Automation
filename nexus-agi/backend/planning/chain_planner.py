class ChainPlanner:
    def build(self, goal: str) -> dict:
        return {'strategy': 'chain', 'steps': [f'Understand goal: {goal}', 'Execute sequentially', 'Validate output']}
