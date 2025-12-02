import hashlib

import requests

url = "http://localhost:8080/users"

def create_user(data):
    print("f")
    r = requests.post(url, json=data)

    print("Status:", r.status_code)
    print("Response:", r.text)

def sha1_hash(salt, password):
    h = hashlib.sha1()
    h.update((salt + password).encode())

    print(h.hexdigest())

def get_salt():
    with open("salt.txt", "r") as file:
        salt_value = file.read()

    return salt_value


if __name__ == '__main__':
    salt = get_salt()
    password = "kakhaPassword";
    data = {
        "userName": "kakha1",
        "userFName": "Kakha",
        "userLName": "Kudava",
        "password": f"{salt + password}"
    }

    create_user(data)
