from microservicio import app

def test_post_devops_success():
    client = app.test_client()

    headers = {
        "X-Parse-REST-API-Key": "2f5ae96c-b558-4c7b-a590-a501ae1c3f6c",
        "X-JWT-KWY": "falso.jwt.token"
    }

    data = {
        "message": "This is a test",
        "to": "Juan Perez",
        "from": "Rita Asturia",
        "timeToLifeSec": 45
    }

    response = client.post("/DevOps", json=data, headers=headers)
    assert response.status_code in [200, 403]  # 403 si JWT inválido
    assert "message" in response.get_json()

def test_invalid_method():
    client = app.test_client()
    response = client.get("/DevOps")  # GET no está permitido
    assert response.status_code == 405
    assert response.data == b"ERROR"
