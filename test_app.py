import json
from app import app

def test_get_tasks():
    client = app.test_client()
    response = client.get('/tasks')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert "tasks" in data
    print("✅ Test 1 passed: GET /tasks")

def test_get_single_task():
    client = app.test_client()
    response = client.get('/tasks/1')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data["id"] == 1
    print("✅ Test 2 passed: GET /tasks/1")

def test_create_task():
    client = app.test_client()
    response = client.post('/tasks',
        data=json.dumps({"title": "New Task"}),
        content_type='application/json')
    assert response.status_code == 201
    data = json.loads(response.data)
    assert data["title"] == "New Task"
    print("✅ Test 3 passed: POST /tasks")

def test_task_not_found():
    client = app.test_client()
    response = client.get('/tasks/999')
    assert response.status_code == 404
    print("✅ Test 4 passed: 404 on missing task")

if __name__ == "__main__":
    print("Running API tests...\n")
    test_get_tasks()
    test_get_single_task()
    test_create_task()
    test_task_not_found()
    print("\n🎉 All tests passed!")
