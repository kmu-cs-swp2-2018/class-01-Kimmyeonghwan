from math import factorial as fact
roman = {1000: 'M', 900: 'CM', 500: 'D', 400: 'CD', 100:'C', 90:'XC',
                  50:'L', 40:'XL',10:'X', 9:'IX', 5:'V', 4:'IV', 1:'I'}
romans = [(1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'), (100, 'C'), (90, 'XC'),
          (50, 'L'), (40, 'XL'),(10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')]
numBreak = [x[0] for x in romans]

def factorial(numStr):
    try:
        n = int(numStr)
        r = str(fact(n))
    except:
        r = 'Error!'
    return r

def decToBin(numStr):
    try:
        n = int(numStr)
        r = bin(n)[2:]
    except:
        r = 'Error!'
    return r

def binToDec(numStr):
    try:
        n = int(numStr, 2)
        r = str(n)
    except:
        r = 'Error!'
    return r

def decToRoman(numStr):
    try:
        n = int(numStr)
    except:
        return 'Error!'

    if n >= 4000:
        return 'Error!'

    result = ''

    for i in range(len(numBreak)):
        while n >= numBreak[i]:
            result += romans[i][1]
            print(romans[i][1])
            n -= numBreak[i]
            print(result)
    return result


def romanToDec(numStr):
    r = 0
    for i in range (len(numStr)):
        if numStr[i] =='M' and numStr[i-1:i+1] != 'CM':
            r += numBreak[0]

        elif numStr[i:i+2] == 'CM':
            r += numBreak[1]
            i += 1

        elif numStr[i] == 'D' and numStr[i-1:i+1] != 'CD':
            r += numBreak[2]

        elif numStr[i:i+2] == 'CD':
            r += numBreak[3]
            i += 1

        elif numStr[i] == 'C' and numStr[i-1:i+1] != 'XC':
            r += numBreak[4]

        elif numStr[i:i+2] == 'XC':
            r += numBreak[5]
            i += 1

        elif numStr[i] == 'L' and numStr[i-1:i+1] != 'XL':
            r += numBreak[6]

        elif numStr[i:i+2] == 'XL':
            r += numBreak[7]
            i += 1

        elif numStr[i] == 'X' and numStr[i-1:i+1] != 'IX':
            r += numBreak[8]

        elif numStr[i:i+2] == 'IX':
            r += numBreak[9]
            i += 1

        elif numStr[i] == 'V' and numStr[i-1:i+1] != 'IV':
            r += numBreak[10]

        elif numStr[i:i+2] == 'IV':
            r += numBreak[11]
            i += 1

        elif numStr[i] == 'I':
            r += numBreak[12]
    '''
        elif numStr[i] not in roman:
            r = 'Error!'
            break
            '''

    r = str(r)
    return r





'''
     for i in range(len(numStr)):
        if numStr[i] == romans[i][1]:
            r += numBreak[i]
        
        elif numStr[i:i+2] == romans[i][1]:
            r += numBreak[i+1]
            i += 1









    for i in range(len(numStr)):
        for j in range(12):
            try:
                g = 0
                if numStr[i] == romans[j][1] and numStr[i:i + 2] != romans[j + 1][1]:
                    while True:
                        r += numBreak[j]
                        g += 1
                        if numStr[g] != romans[j][1] or numStr[g:g + 2] == romans[j + 1][1]:
                            break
                    continue

                elif numStr[i:i + 2] == romans[j + 1][1]:
                    while True:
                        r += numBreak[j + 1]
                        g += 1
                        if numStr[g:g + 2] != romans[j + 1][1]:
                            i += 1
                            break
                    break


            except:
                pass


                continue

        r = str(r)
        return r
'''


def act(num,numStr):
    if num == 0:
        return factorial(numStr)

    elif num == 1:
        return decToBin(numStr)

    elif num == 2:
        return binToDec(numStr)

    elif num == 3:
        return decToRoman(numStr)

    elif num == 4:
        return romanToDec(numStr)
