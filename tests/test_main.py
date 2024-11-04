import pytest
from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)

def test_add_new_recipe():
    data = {
        "name": "Test Recipe",
        "descr": "Test description",
        "views": 4,
        "cooking_time": 30,
        "ingredients": "Test ingredients",
    }
    response = client.post("/recipe/", json=data)
    assert response.status_code == 200
    assert response.json()["name"] == "Test Recipe"


@pytest.mark.asyncio
def test_get_all_recipes():
    response = client.get("/recipe")
    assert response.status_code == 200
    assert len(response.json()) >= 1

def test_get_recipe_by_id():
    response = client.get("/recipe/1")
    assert response.status_code == 200
    assert response.json()["name"] != ""



