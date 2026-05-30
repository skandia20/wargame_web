import requests
import base64
import re

BLOCK_SIZE = 16
host = "http://127.0.0.1:8080"
session = requests.session()

req = requests.get(host+"/gb/1",).json()
e_data = base64.b64decode(req['result']['article']['enc_data'])
b_data = [e_data[i:i+16] for i in range(0, len(e_data), 16)]
result = ""

for index, b_d in enumerate(b_data):
    mid_text = bytearray([0x00] * 16)
    if index == 0:
        IV = bytearray([0x00] * 16)
    else:
        IV = bytearray(b_data[index - 1]) # 확실하게 bytearray로 형변환

    for i in range(16)[::-1]:
        pad_size = BLOCK_SIZE - i
        tmp_iv = bytearray([0x00] * 16)
        
        for k in range(i + 1, 16):
            tmp_iv[k] = mid_text[k] ^ pad_size

        for char in range(256):
            tmp_iv[i] = char

            sub_data = dict(token="sups", sig="sups", e_data=base64.b64encode(tmp_iv + b_d).decode())
            req = session.get(host + "/secure/decrypt", params=sub_data, timeout=5.0).json()

            if req['result']['message'] != "ValueError":
                mid_text[i] = char ^ pad_size
                break
    
    plain_text = bytearray([0x00] * 16)
    for i in range(16):
        plain_text[i] = mid_text[i] ^ IV[i]

    result += plain_text.decode('latin-1')
    
    print(f"현재 평문 : {result}")
    
print(f"최종결과 : {result}\n")

pattern = r'(?<=is: ).*?(?=")'
result = re.search(pattern, result)

params = {"password" : result.group()}
req = requests.get(host+"/secure/secret", params=params).json()

print(f"FLAG IS {req['result']['secret']}")