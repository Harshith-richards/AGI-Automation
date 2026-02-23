from datetime import datetime


class EpisodicMemory:
    def __init__(self):
        self._episodes: list[dict] = []

    def add_episode(self, episode: dict):
        enriched = dict(episode)
        enriched['timestamp'] = datetime.utcnow().isoformat()
        self._episodes.append(enriched)

    def list(self) -> list[dict]:
        return self._episodes
