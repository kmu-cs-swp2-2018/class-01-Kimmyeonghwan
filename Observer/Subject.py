import datetime as d
import urllib.request
import json

class Subject:
    def __init__(self):
        self.today = d.datetime.today()
        self.ts = self.today.timetuple()
        self.url = 'http://52.78.1.91/weather?date={}{}{}&time={}{}'.format(self.ts.tm_year, self.ts.tm_mon, self.ts.tm_mday, self.ts.tm_hour - 2, self.ts.tm_min)
        self.u = urllib.request.urlopen(self.url)
        self.data = self.u.read()
        self.j = json.loads(self.data)
        self.temp = self.j["temperature"]
        self.humidity = self.j["humidity"]
        self.weather = "미구현"


    def replaceDay(self):
        today = d.datetime.today()
        replaceYear = int(input("바꿀 년을 입력해주세요 : "))
        replaceMonth = int(input("바꿀 월을 입력해주세요 : "))
        replaceDay = int(input("바꿀 일을 입력해주세요 : "))
        replaceHour = int(input("바꿀 시간을 입력해주세요 : "))
        replaceMinute = int(input("바꿀 분을 입력해주세요 : "))
        replaceSecond = int(input("바꿀 초를 입력해주세요 : "))
        self.today = today.replace(year=replaceYear, month=replaceMonth, day=replaceDay, hour=replaceHour, minute=replaceMinute, second=replaceSecond)
        self.ts = self.today.timetuple()


    def replaceWeather(self):
        self.weather = str(input("날씨를 입력해주세요 : "))
        
        
    # 해당 부분을 json 코드로 구현해서 그런지 int로 수정하려니 에러 발생.
    # 해당 오류 수정하려고 애썼는데 실패.
    # 중요한건 옵저버 패턴이니 옵저버 패턴을 구현하려고 시도한 점에 의의를 가지자.
    def replaceTempHumidity(self):
        self.replaceTemp = int(input("바꿀 온도를 입력해주세요 : "))
        self.replaceHumidity = int(input("바꿀 습도를 입력해주세요 : "))

    def todayNow(self):
        self.today = d.datetime.today()
        self.ts = self.today.timetuple()

    def weatherNow(self):
        self.weather = "미구현"

    def tempHumidityNow(self):
        self.url = 'http://52.78.1.91/weather?date={}{}{}&time={}{}'.format(self.ts.tm_year, self.ts.tm_mon, self.ts.tm_mday, self.ts.tm_hour - 2, self.ts.tm_min)
        self.u = urllib.request.urlopen(self.url)
        self.data = self.u.read()
        self.j = json.loads(self.data)
        self.temp = self.j["temperature"]
        self.humidity = self.j["humidity"]
