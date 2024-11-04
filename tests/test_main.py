from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)

def test_get_all_recipes():
    response = client.get("/recipe/")
    assert response.status_code == 200
    assert len(response.json()) >= 1

def test_get_recipe_by_id():
    response = client.get("/recipe/1")
    assert response.status_code == 200
    assert response.json()["name"] != ""

def test_add_new_recipe():
    data = {
        "name": "Test Recipe",
        "views": 0,
        "cooking_time": 30,
        "ingredients": "Test ingredients",
        "descr": "Test description"
    }
    response = client.post("/recipe/", json=data)
    assert response.status_code == 200
    assert response.json()["name"] == "Test Recipe"

def test_add_new_recipe_with_empty_fields():
    data = {
        "views": 0,
        "cooking_time": 30,
        "ingredients": "Test ingredients",
        "descr": "Test description"
    }
    response = client.post("/recipe/", json=data)
    assert response.status_code == 422

def test_get_nonexistent_recipe():
    response = client.get("/recipe/1000000")
    assert response.status_code == 404
