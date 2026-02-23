class SemanticMemory:
    def __init__(self):
        self._records: list[dict] = []

    def upsert(self, text: str, metadata: dict | None = None):
        self._records.append({'text': text, 'metadata': metadata or {}})

    def search(self, query: str, limit: int = 5) -> list[dict]:
        ranked = sorted(self._records, key=lambda r: query.lower() in r['text'].lower(), reverse=True)
        return ranked[:limit]
