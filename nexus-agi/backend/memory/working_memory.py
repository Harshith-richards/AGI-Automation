from collections import deque


class WorkingMemory:
    def __init__(self, size: int = 20):
        self._buffer = deque(maxlen=size)

    def add(self, item: dict):
        self._buffer.append(item)

    def list(self) -> list[dict]:
        return list(self._buffer)
