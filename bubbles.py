import requests
import random

phoneNumber = input("Skriv dit telefon nummer: ").replace(" ", "").replace("+45", "")

url = "https://api.mgame.nu/server-2021-winter-circlek/server.php"

payload = {
    "route": "twofactor_mobile",
    "data": {
        "mobile": phoneNumber,
        "force": True
    }
}

headers = {
    "Accept": "*/*",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "da-DK,da;q=0.9,en-US;q=0.8,en;q=0.7",
    "Bm-Country": "dk",
    "Connection": "keep-alive",
    "Content-Length": "70",
    "Content-Type": "application/json",
    "Host": "api.mgame.nu",
    "Origin": "https://skrab.circlek.one",
    "Referer": "https://skrab.circlek.one/",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "cross-site",
    "Sec-GPC": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36"
}

login = requests.post(url, headers=headers, json=payload)
print(login.json())

loginCode = input("Skriv koden du fik tilsendt af Circle K: ")

payload = {
    "route": "login",
    "data": {
        "mobile": phoneNumber,
        "code": int(loginCode),
        "permission_primary": True,
        "permission_marketing": True,
        "referrer": "direct"
    }
}

login = requests.post(url, headers=headers, json=payload)
print(login.json())

sessionId = login.json()["session"]
print(f"Session ID: {sessionId}")

payload = {
    "route": "profile_update",
    "data": {
        "session": sessionId,
        "profile": {
            "age": 15,
            "gender": 0
        }
    }
}

setAge = requests.post(url, headers=headers, json=payload)
print(setAge.json())

payload = {
    "route": "game_start",
    "data": {
        "type": "bubble",
        "name": "default",
        "session": sessionId
    }
}

getGameId = requests.post(url, headers=headers, json=payload)
print(getGameId.json())
gameId = getGameId.json()["game_id"]

payload = {
    "route": "game_end",
    "data": {
        "type": "bubble",
        "name": "default",
        "session": sessionId,
        "game_id": gameId,
        "point": int(input("Hvor mange point vil du have: ")),
        "data":
            {
                "dVUCYfln": random.randint(3, 9),
                "boWuSnWa": random.randint(3, 9),
                "RSduPLU6": random.randint(3, 9),
                "gLHfg8o6": random.randint(3, 9),
                "lJAeml1t": random.randint(3, 9),
            },
        "playtime": random.randint(90000, 100000)
    }
}

skrab = requests.post(url, headers=headers, json=payload)
print(skrab.json())
