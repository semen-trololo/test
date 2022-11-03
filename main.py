import requests
import time

def send_telegram(data):
    pass

def get_status():
    try:
        r = requests.get('https://xn--90aeniddllys.xn--p1ai')
        return r.status_code == requests.codes.ok
    except:
        return False

def send_status_code(data):
    len_data = len(data)
    print(len_data)
    print(sum(data))
    rezult = sum(data) / len_data * 100
    send_telegram('Up time website in dey' + str(rezult) + ' %')

flag = 0
tmp = []
while True:
    for i in range(0, 3):
        status = get_status()
        if status:
            tmp.append(status)
            break
        time.sleep(30)
    else:
        send_telegram('Website not request 200')
        tmp.append(False)
    flag += 1
    if flag == 100:
        send_status_code(tmp)
        tmp = []
        flag = 0
        break
    time.sleep(300)
