from fastapi.testclient import TestClient
from main import app
import pytest
import sqlite3

client = TestClient(app)

def test_read_main():
    resposne = client.get("/")
    assert resposne.status_code == 200
    assert resposne.json() == {"message": "Hello world!"}

def test_method():
    response = client.get("/method")
    assert response.status_code == 200
    assert response.json() == {"method": "GET"}

def test_hash_password():
    params = {
        "password": "haslo",
        "password_hash": "013c6889f799cd986a735118e1888727d1435f7f623d05d58c61bf2cd8b49ac90105e5786ceaabd62bbc27336153d0d316b2d13b36804080c44aa6198c533215"
    }
    response = client.get("/auth", params=params)
    assert response.status_code == 204

def test_register():
    params = {
        "name": "Adam",
        "surname": "Nowak"
    }
    response = client.post("/register", json = params)
    print(response.text)
    #assert response.status_code == 201

def test_get_patient_data():
    response = client.post(f"/register/{'1'}")
    print(response.text, response.status_code)


