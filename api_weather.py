# coding:utf-8
import json
import requests

params = {"version":"1", "city": "부산", "county":"수영구", "village":"광안동"}
headers = {"appKey":"5ab7433a-57e5-3c64-89a4-1ee1fbd12546"}
r = requests.get("http://apis.skplanetx.com/weather/current/hourly",params=params, headers=headers)

#print (r.json())

data = json.loads(r.text)
weather = data["weather"]["hourly"]
cTime = weather[0]["timeRelease"]
cSky = weather[0]["sky"]["name"]
cWind = weather[0]["wind"]["wspd"]
cTemp = weather[0]["temperature"]["tc"]

cWeather = "오늘의 날씨 "+cTime+"기준하늘은 "+cSky+"이고 풍속은"+cWind+"이고 기온은 "+cTemp+"입니다."
print(cWeather)
