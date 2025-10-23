from app import app

def test_home():
    response = app.test_client().get('/')
    assert response.status_code == 200

def test_health():
    response = app.test_client().get('/health')
    assert b"OK" in response.data

def test_post_data():
    client = app.test_client()
    res = client.post('/data', json={"hello": "world"})
    assert res.status_code == 200
    json_data = res.get_json()
    assert json_data.get("received", {}).get("hello") == "world"
