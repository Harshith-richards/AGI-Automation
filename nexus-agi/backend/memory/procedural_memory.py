class ProceduralMemory:
    def __init__(self):
        self._procedures: dict[str, dict] = {}

    def save(self, key: str, procedure: dict):
        self._procedures[key] = procedure

    def find(self, key: str) -> dict | None:
        return self._procedures.get(key)
