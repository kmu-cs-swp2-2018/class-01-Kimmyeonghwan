def day(year, mon, mday, hour, minute, sec):
    print("현재 시간 : {}년 {}월 {}일 {}시 {}분 {}초".format(year, mon, mday, hour, minute, sec))


def tempHumidity(temp, humidity):
    print("현재 온도 : {}, 현재 습도 : {}".format(temp, humidity))


def weather(weather):
    print("날씨 : {}".format(weather))

def menu():
    print("==================관리자 메뉴=====================")
    print("1. 날짜 수정")
    print("2. 날씨 수정")
    print("3. 온도 수정")
    print("4. 날짜 갱신")
    print("5. 날씨 갱신")
    print("6. 온도 갱신")
    print("9. 프로그램 종료")
    print("================================================")