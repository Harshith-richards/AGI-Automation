class TreeOfThoughtsPlanner:
    def build(self, goal: str) -> dict:
        branches = [
            {'path': 'fast', 'score': 0.7, 'steps': ['quick research', 'draft output']},
            {'path': 'thorough', 'score': 0.9, 'steps': ['deep research', 'cross-check', 'draft output']},
        ]
        best = max(branches, key=lambda b: b['score'])
        return {'strategy': 'tree_of_thoughts', 'goal': goal, 'branches': branches, 'selected': best}
