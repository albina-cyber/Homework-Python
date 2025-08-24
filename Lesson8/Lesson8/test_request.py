import requests


def test_simple_req():
    resp = requests.get('https://httpbin.org/basic-auth/user/pass')
    assert resp.status_code == 200
