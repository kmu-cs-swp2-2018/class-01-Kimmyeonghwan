#DB파일 열기

import pickle

dbfilename = 'assignment3.dat'

def readScoreDB():
    try:
        fH = open(dbfilename, 'rb')
    except FileNotFoundError as e:
        print("New DB: ", dbfilename)
        return []

    scdb = []
    try:
        scdb =  pickle.load(fH)
    except:
        print("Empty DB: ", dbfilename)
    else:
        print("Open DB: ", dbfilename)
    fH.close()
    return scdb


# write the data into person db
def writeScoreDB(scdb):
    fH = open(dbfilename, 'wb')
    pickle.dump(scdb, fH)
    fH.close()


def doScoreDB(scdb):
    while(True):
        inputstr = (input("Score DB > "))
        if inputstr == "": continue
        parse = inputstr.split(" ")
        if parse[0] == 'add':
            try:
                record = {'Age':parse[2], 'Name':parse[1], 'Score':parse[3]}
                scdb += [record]
                print("정상적으로 추가되었습니다.")
            except:
                print("이름, 나이, 점수순으로 적어주세요.")
                continue

        elif parse[0] == 'del':
                try:
                    for i in range(len(scdb)):
                        for j in scdb:
                            if j['Name'] == parse[1]:
                                scdb.remove(j)
                                break
                except:
                    print("삭제할 이름을 적어주세요.")
                    continue
                else:
                    print("삭제가 완료되었습니다.")
                    continue

        elif parse[0] == 'show':
            sortKey ='Name' if len(parse) == 1 else parse[1]
            showScoreDB(scdb, sortKey)
        elif parse[0] == 'quit':
            break

        elif parse[0] == 'find':
            try:
                for j in scdb:
                    if j['Name'] == parse[1]:
                        print(j)
                        continue
            except:
                print("검색할 이름을 적어주세요.")
                continue
            else:
                print("검색이 완료되었습니다.")
                continue


        elif parse[0] == 'inc':
            try:
                for i in range(len(scdb)):
                    for j in scdb:
                        if j['Name'] in parse[1]:
                            j['Score'] = int(j['Score'])
                            j['Score'] += int(parse[2])
                            j['Score'] = str(j['Score'])
                    break
            except:
                print("검색할 이름과 추가할 점수를 적어주세요.")
                continue
            else:
                print("추가가 완료되었습니다.")
                continue

        elif parse[0] == 'exc':
            try:
                for i in range(len(scdb)):
                    for j in scdb:
                        if j['Name'] in parse[1]:
                            j['Score'] = int(j['Score'])
                            j['Score'] -= int(parse[2])
                            j['Score'] = str(j['Score'])
                    break
            except:
                print("검색할 이름과 뺄 점수를 적어주세요.")
                continue
            else:
                print("빼기가 완료되었습니다.")
                continue


        else:
            print("Invalid command: " + parse[0])


def showScoreDB(scdb, keyname):
    for p in sorted(scdb, key=lambda person: person[keyname]):
        for attr in sorted(p):
            print(attr + "=" + p[attr], end=' ')
        print()



scoredb = readScoreDB()
doScoreDB(scoredb)
writeScoreDB(scoredb)
