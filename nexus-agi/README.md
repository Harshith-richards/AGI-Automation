# NEXUS-AGI

## Architecture overview

```text
+----------------------+       +------------------------+
| React Frontend       |<----->| FastAPI Control Plane  |
| Dashboard/Tasks/UI   |  WS   | REST + WebSocket APIs  |
+----------+-----------+       +-----------+------------+
           |                                   |
           v                                   v
+----------+-----------+         +------------+-------------+
| Orchestrator Agent   |-------->| Tool Registry + 50+ tools|
| DAG + ReAct + Planner|         +------------+-------------+
+-----+------+---------+                      |
      |      |                                v
      |      +-------> Specialized Agents  (research/coder/...)
      |
      v
+-----+-----------------------------------------------+
| Memory Fabric: Working + Episodic + Semantic + Proc |
+-----+-----------------------------------------------+
      |
      v
+-----+------------------+  +------------------+
| Qdrant / Neo4j / Redis |  | Postgres / Celery|
+------------------------+  +------------------+
```

## Local preview (quick start)

### 1) Backend API
```bash
cd nexus-agi
python -m venv .venv
source .venv/bin/activate
pip install -r backend/requirements.txt
uvicorn backend.main:app --reload --host 0.0.0.0 --port 8000
```

Check health:
```bash
curl http://127.0.0.1:8000/health
```

### 2) Frontend UI
In a second terminal:
```bash
cd nexus-agi/frontend
npm install
npm run dev -- --host 0.0.0.0 --port 5173
```

Open `http://127.0.0.1:5173`.

### 3) Full stack with Docker Compose
```bash
cd nexus-agi
docker compose -f infrastructure/docker-compose.yml up --build
```

## Example task API request
```bash
curl -X POST http://127.0.0.1:8000/api/task \
  -H 'Content-Type: application/json' \
  -d '{"id":"demo-1","goal":"Research and implement anomaly detector"}'
```

## Example tasks and traces
1. Goal: "Research and implement anomaly detector" -> researcher -> coder -> critic pipeline with structured outputs.
2. Goal: "Build SQL report and send to Slack" -> analyst -> communicator execution with tool logs.
3. Goal: "Automate website form + archive output" -> browser -> filesystem -> critic chain with checkpoint.

## Security highlights
- JWT auth helpers and password hashing.
- Sandboxed code execution helper with 30-second timeout.
- Audit event model and recorder.

## Production notes
- Kubernetes manifests under `infrastructure/k8s`.
- Prometheus config under `infrastructure/monitoring`.
- Celery worker and beat schedules included.
