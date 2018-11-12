Subscriber = ["홍길동", "콩쥐", "팥쥐"]

def subData(year, mon, mday, hour, minute, sec, temp, humidity, weather):
    for i in range (len(Subscriber)):
        print("==============={}님의 화면입니다.================".format(Subscriber[i]))
        print("현재 시간 : {}년 {}월 {}일 {}시 {}분 {}초".format(year, mon, mday, hour, minute, sec))
        print("현재 온도 : {}, 현재 습도 : {}".format(temp, humidity))
        print("날씨 : {}".format(weather))
        print("================================================")