def test_health_endpoint_returns_200(client):
    resp = client.get("/")
    assert resp.status_code == 200
