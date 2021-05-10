import requests
import json
import time

url = "https://www.oref.org.il/WarningMessages/alert/alerts.json"
headers = {}
headers["Connection"] = "keep-alive"
headers["sec-ch-ua"] = "\" Not A;Brand\";v=\"99\", \"Chromium\";v=\"90\", \"Google Chrome\";v=\"90\""
headers["Accept"] = "text/plain, */*; q=0.01"
headers["X-Requested-With"] = "XMLHttpRequest"
headers["sec-ch-ua-mobile"] = "?0"
headers["User-Agent"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36"
headers["Content-Type"] = "application/x-www-form-urlencoded; charset=UTF-8"
headers["Sec-Fetch-Site"] = "same-origin"
headers["Sec-Fetch-Mode"] = "cors"
headers["Sec-Fetch-Dest"] = "empty"
headers["Referer"] = "https://www.oref.org.il//12481-he/Pakar.aspx"
headers["Accept-Language"] = "en-US,en;q=0.9"
#headers["Cookie"] = "pakar_sound_unmute=0; pakar_last_warning_id=1620664276452; Lastalerts="
headers["If-Modified-Since"] = "Mon, 10 May 2021 16:00:00 GMT"


'''
returns either null or:
{
    "data": ["נתיב העשרה"],
    "id": 1620662353520,
    "title": "התרעות פיקוד העורף"
}
{
    "data": [
        "זיקים",
        "יד מרדכי",
        "נתיב העשרה"
    ],
    "id": 1620667240202,
    "title": "התרעות פיקוד העורף"
}
'''
def check_warning():
    resp = requests.get(url, headers=headers)
    headers["If-Modified-Since"] = time.strftime("%a, %d %b %Y %H:%M:%S GMT", time.gmtime())
    if len(resp.text)==0: return None # no alert. hurray!
    resp = resp.text
    resp = resp.replace("\n","").replace("\t","")
    resp = json.loads(resp)
    headers["Cookie"] = "pakar_last_warning_id="+str(resp['id'])
    return (headers["data"], headers["title"]) # locations, hebrew title tuple


while True:
    print(check_warning())
    time.sleep(2) # oref website checks every 2 secs
