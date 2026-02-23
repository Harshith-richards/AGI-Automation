class KnowledgeGraph:
    def __init__(self):
        self.nodes: set[str] = set()
        self.edges: list[tuple[str, str, str]] = []

    def add_fact(self, src: str, relation: str, dst: str):
        self.nodes.update([src, dst])
        self.edges.append((src, relation, dst))

    def query(self, entity: str):
        return [e for e in self.edges if entity in (e[0], e[2])]
