class ReActPlanner:
    def build(self, goal: str) -> dict:
        return {
            'strategy': 'react',
            'goal': goal,
            'loop': [
                {'phase': 'reason', 'text': 'assess state and missing data'},
                {'phase': 'act', 'text': 'run best tool/agent action'},
                {'phase': 'observe', 'text': 'inspect output and adjust'},
            ],
        }
