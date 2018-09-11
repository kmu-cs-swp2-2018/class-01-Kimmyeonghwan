import time


def fibonacci(n):
    if (0 <= n <= 1):
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


def iterfibo(n):
    f = list()
    for i in range(n + 1):
        f.append(fibonacci(i))
    return f


while True:
    nbr = int(input("Enter a number: "))
    if nbr == -1:
        break
    ts = time.time()
    fibonumber = iterfibo(nbr)
    ts = time.time() - ts
    print("IterFibo(", nbr, ")=", fibonumber, ", time %.6f" % (ts))
    ts = time.time()
    fibonumber = fibonacci(nbr)
    ts = time.time() - ts
    print("Fibo(%d)=%d, time %.6f" % (nbr, fibonumber, ts))
