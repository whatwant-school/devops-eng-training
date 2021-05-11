# TODO(everyone): 웹서버의 healthz가 response code 200 확인
import pytest
import requests


def test_code():
    response = requests.get(url="http://localhost:5000" + "/healthz")
    assert response.status_code == 200