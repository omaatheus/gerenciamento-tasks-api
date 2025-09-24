import pytest
import requests

BASE_URL = "http://127.0.0.1:5000"
tasks = []

#Create
def testCreateTask():
    newTaskData = {
        "title": "New Task",
        "description": "New Task Description",
    }
    res = requests.post(f"{BASE_URL}/tasks", json=newTaskData)
    assert res.status_code == 200 #estamos validando que se nao ser certo, vai retornar o erro
    resJson = res.json()
    assert "message" in resJson
    assert "id" in resJson
    tasks.append(resJson["id"])

def testGetTasks():
    res = requests.get(f"{BASE_URL}/tasks")
    assert res.status_code == 200
    resJson = res.json()
    assert "tasks" in resJson
    assert "totalTasks" in resJson

def testGetTask():
    if tasks:
        taskId = tasks[0]
        res = requests.get(f"{BASE_URL}/tasks/{taskId}")
        assert res.status_code == 200
        resJson = res.json()
        assert taskId == resJson['task']['id']

def testUpdateTask():
    if tasks:
        taskId = tasks[0]
        payload = {
            "title": "Task Updated",
            "description": "Task Description updated",
            "completed": False,
        }
        res = requests.put(f"{BASE_URL}/tasks/{taskId}", json=payload)
        assert res.status_code == 200
        resJson = res.json()
        print(resJson)
        assert "message" in resJson
        assert taskId == resJson['id']

def testDeleteTask():
    if tasks:
        taskId = tasks[0]
        res = requests.delete(f"{BASE_URL}/tasks/{taskId}")
        assert res.status_code == 200
        resJson = res.json()
        assert "message" in resJson