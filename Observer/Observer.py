from Subject import Subject
import View as view
import Subscriber as subscriber

def Main():
    re = 0
    subject = Subject()
    while(re != 9):
        print("==================관리자 화면=====================")
        view.day((subject.ts.tm_year), (subject.ts.tm_mon), (subject.ts.tm_mday), (subject.ts.tm_hour), (subject.ts.tm_min), (subject.ts.tm_sec))
        view.tempHumidity((subject.temp), (subject.humidity))
        view.weather(subject.weather)
        view.menu() # self 사용이 아니라서 model 말고 Model 사용
        re = int(input("숫자를 입력해주세요. : "))

        if re == 1:
            subject.replaceDay()

        if re == 2:
            subject.replaceWeather()

        if re == 3:
            subject.replaceTempHumidity()

        if re == 4:
            subject.todayNow()

        if re == 5:
            subject.weatherNow()

        if re == 6:
            subject.tempHumidityNow()

        subscriber.subData((subject.ts.tm_year), (subject.ts.tm_mon), (subject.ts.tm_mday), (subject.ts.tm_hour), (subject.ts.tm_min), (subject.ts.tm_sec),(subject.temp), (subject.humidity), (subject.weather))



if __name__ == '__main__':
    Main()