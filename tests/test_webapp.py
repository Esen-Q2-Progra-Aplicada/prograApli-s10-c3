from flask import Flask
from routes.main_routes import MainRoutes
import requests


def test_webapp():
    assert True is True


def test_webapp_site_home():
    app = Flask(__name__)
    MainRoutes.configure_routes(app)
    response = requests.get("http://localhost:5000")
    assert response.status_code == 200
