from Observer_View import View
from Observer_Model import Model


def Main():
    re = 0
    model = Model()
    view = View()

    while(re != 9):
        print("현재 시간 : {}년 {}월 {}일 {}시 {}분 {}초".format(view.ts.tm_year, view.ts.tm_mon, view.ts.tm_mday, view.ts.tm_hour, view.ts.tm_min, view.ts.tm_sec))
        print("현재 온도 : {}, 현재 습도 : {}".format(view.temp, view.humidity))
        print("날씨 : {}".format(view.weather))
        Model.list() # self 사용이 아니라서 model 말고 Model 사용
        re = int(input("숫자를 입력해주세요. : "))

        if re == 1:
            view.todayReplace(model.replaceDay(view.dateReplace()))

        if re == 2:
            view.weatherReplace(model.replaceWeather())

        if re == 3:
            view.tempHumidityReplace(model.replaceTempHumidity)

        if re == 4:
            view.todayNow()

        if re == 5:
            view.weatherNow()

        if re == 6:
            view.tempHumidityNow()



if __name__ == '__main__':
    Main()