from math import factorial as fact

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
    return 'dec -> Roman'

def sum(num,numStr):
    if num == 0:
        return factorial(numStr)

    elif num == 1:
        return decToBin(numStr)

    elif num == 2:
        return binToDec(numStr)

    elif num == 3:
        return decToBin(numStr)
