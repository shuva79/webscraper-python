# this is for printing responses when we send a request to the url

import requests as req

headers = {
    'User-Agent' : 
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
}

url = "https://tms07.nepsetms.com.np/tmsapi/dnaApi/exchange/sessionCheck"
response = req.get(url=url, headers = headers)



if response.status_code == 200:
    print(response.text)

else:
    print("Not successful")


def ask_url():
    return url