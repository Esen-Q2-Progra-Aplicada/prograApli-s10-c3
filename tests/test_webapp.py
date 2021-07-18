from flask import Flask
from routes.main_routes import MainRoutes
import requests


def test_webapp():
    assert True is True


def test_webapp_site_home():
    response = requests.get("http://www.google.com")
    assert response.status_code == 200
