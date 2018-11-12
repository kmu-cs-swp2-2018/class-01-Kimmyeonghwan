import datetime as d
class Model:

    def list():
        print("================================================")
        print("1. 날짜 수정")
        print("2. 날씨 수정")
        print("3. 온도 수정")
        print("4. 날짜 갱신")
        print("5. 날씨 갱신")
        print("6. 온도 갱신")
        print("9. 프로그램 종료")
        print("================================================")

    def __init__(self):
        pass


    def replaceDay(self,Date):
        today = d.datetime.today()
        self.today = today.replace(year=Date[0], month=Date[1], day=Date[2], hour=Date[3], minute=Date[4], second=Date[5])
        return self.today



    def replaceWeather(self):
        self.weather = str(input("날씨를 입력해주세요 : "))
        return self.weather

    def replaceTempHumidity(self):
        self.replaceTemp = int(input("바꿀 온도를 입력해주세요 : "))
        self.replaceHumidity = int(input("바꿀 습도를 입력해주세요 : "))
        return self.replaceTemp, self.replaceHumidity
