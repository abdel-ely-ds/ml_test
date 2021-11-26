from fastapi.testclient import TestClient

from Python.api.api import app

client = TestClient(app)


def test_clean_string():
    response = client.post(
        "/clean_string", json={"string": "2076,3B,19C,138D,NULL,NULL"}
    )
    assert response.status_code == 200
    assert response.json() == {"processed_string": "138D,19C,3B,2076"}
