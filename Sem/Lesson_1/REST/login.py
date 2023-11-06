"token - 97b6ad27c4513fada4c582c77ff8994c"

import requests
import yaml

with open("config.yaml", encoding="utf-8") as f:
    data = yaml.safe_load(f)
def login():
    responce = requests.post(url=data.get("url_login"),
                             data={"username": data.get("username"),
                                   "password": data.get("password")})
    if responce.status_code == 200:
        return responce.json()["token"]

def get_post(token):
    print(token)
    responce = requests.post(url=data.get("url_post"),
                             headers={"X-Auth-Token": token},
                             params={"owner": "notMe"})
    print(responce.json())
    return responce.json()

if __name__ == "__main__":
    get_post(login())
