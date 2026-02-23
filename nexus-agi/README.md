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

## Setup
1. `cd nexus-agi`
2. Create env: `cp .env.example .env`
3. Install backend deps and run API: `uvicorn backend.main:app --reload`
4. Run tests: `pytest`
5. Start infrastructure: `docker compose -f infrastructure/docker-compose.yml up -d`

## Example tasks and traces
1. Goal: "Research and implement anomaly detector" -> researcher->coder->critic pipeline with structured outputs.
2. Goal: "Build SQL report and send to Slack" -> analyst->communicator execution with tool logs.
3. Goal: "Automate website form + archive output" -> browser->filesystem->critic chain with checkpoint.

## Security highlights
- JWT auth helpers and password hashing.
- Sandboxed code execution helper with 30-second timeout.
- Audit event model and recorder.

## Production notes
- Kubernetes manifests under `infrastructure/k8s`.
- Prometheus config under `infrastructure/monitoring`.
- Celery worker and beat schedules included.
