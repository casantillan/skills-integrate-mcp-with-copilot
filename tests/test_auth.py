import base64

from fastapi.testclient import TestClient

from src.app import app


client = TestClient(app)


def auth(username, password):
    token = base64.b64encode(f"{username}:{password}".encode()).decode()
    return {"Authorization": f"Basic {token}"}


def test_signup_requires_authentication():
    response = client.post(
        "/activities/Chess Club/signup?email=new@mergington.edu"
    )
    assert response.status_code == 401
    assert response.headers["www-authenticate"] == "Basic"


def test_student_cannot_manage_another_student():
    response = client.post(
        "/activities/Chess Club/signup?email=other@mergington.edu",
        headers=auth("michael@mergington.edu", "student-password"),
    )
    assert response.status_code == 403


def test_teacher_can_manage_registrations():
    email = "new@mergington.edu"
    response = client.post(
        f"/activities/Chess Club/signup?email={email}",
        headers=auth("teacher", "teacher-password"),
    )
    assert response.status_code == 200

    response = client.delete(
        f"/activities/Chess Club/unregister?email={email}",
        headers=auth("teacher", "teacher-password"),
    )
    assert response.status_code == 200