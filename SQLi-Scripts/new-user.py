import requests

url = "http://localhost:8080/users"

def create_user(data):
    print("f")
    r = requests.post(url, json=data)

    print("Status:", r.status_code)
    print("Response:", r.text)

if __name__ == '__main__':
    data = {
        "userName": "kakha1",
        "userFName": "Kakha",
        "userLName": "Kudava",
        "password": "kakhaPassword"
    }

    create_user(data)
