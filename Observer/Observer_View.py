import datetime as d
import urllib.request
import json

class View:

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


    def dateReplace(self):
        '''
        replaceDate = input("바꿀 년, 월, 일, 시간, 분, 초를 순서대로 입력해주세요 : ")
        splitDate = [[int(y) for y in x.split()] for x in replaceDate]
        return splitDate
        '''
        # 해당 부분을 .split를 이용해서 줄일 수 없나? 시도해봤지만 실패
        replaceYear = int(input("바꿀 년을 입력해주세요 : "))
        replaceMonth = int(input("바꿀 월을 입력해주세요 : "))
        replaceDay = int(input("바꿀 일을 입력해주세요 : "))
        replaceHour = int(input("바꿀 시간을 입력해주세요 : "))
        replaceMinute = int(input("바꿀 분을 입력해주세요 : "))
        replaceSecond = int(input("바꿀 초를 입력해주세요 : "))
        return replaceYear, replaceMonth, replaceDay, replaceHour, replaceMinute, replaceSecond




    def weatherReplace(self, weather):
        self.weather = weather

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

    def todayReplace(self, today):
        self.today = today
        self.ts = today.timetuple()

    # 해당 부분을 json 코드로 구현해서 그런지 int로 수정하려니 에러 발생.
    # 해당 오류 수정하려고 애썼는데 실패.
    # 중요한건 옵저버 패턴이니 옵저버 패턴을 구현하려고 시도한 점에 의의를 가지자.
    def tempHumidityReplace(self, tempHumidityData):
        self.temp = tempHumidityData[0]
        self.humidity = tempHumidityData[1]
