import requests


def test_connection():
    try:
        response = requests.get("https://leetcode.com")
        if response.status_code == 200:
            print("leetcode reachable")
        else:
            return f"status_code:{response.status_code}"
    except Exception as e:
        return str(e)
