from fastapi.testclient import TestClient
from incagent.main import app

client = TestClient(app)


def test_runs_and_refuses_a_write():
    payload = client.post("/agent/run", json={"goal": 'why is the pod restarting', **{'payload': {'logs': ['container oom killed']}}}).json()
    assert payload["refused"] is False
    assert payload["applied"] is False
    assert payload["hypothesis"] == "memory"
    refused = client.post("/agent/run", json={"goal": 'page the oncall and confirm root cause'}).json()
    assert refused["refused"] is True
