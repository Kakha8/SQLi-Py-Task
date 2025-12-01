import requests

BASE_URL = "http://localhost:8080/users"


def check_user(username):
    response = requests.get(BASE_URL, params={"username": username})

    print("Status code:", response.status_code)
    print("Response JSON:", response.json())

if __name__ == '__main__':
    user = "admin"
    check_user(user)