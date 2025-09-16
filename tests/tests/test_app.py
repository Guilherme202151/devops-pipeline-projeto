from app import app as flask_app


def test_home_status_code():
    client = flask_app.test_client()
    response = client.get("/")
    assert response.status_code == 200


def test_home_content():
    client = flask_app.test_client()
    res = client.get("/")
    assert b"Hello, DevOps World!" in res.data
