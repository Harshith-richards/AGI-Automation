class MCTSPlanner:
    def build(self, goal: str) -> dict:
        candidates = [
            {'plan': ['research', 'implement'], 'expected_value': 0.78},
            {'plan': ['implement', 'test', 'revise'], 'expected_value': 0.86},
        ]
        best = max(candidates, key=lambda c: c['expected_value'])
        return {'strategy': 'mcts', 'goal': goal, 'simulations': candidates, 'selected': best}
