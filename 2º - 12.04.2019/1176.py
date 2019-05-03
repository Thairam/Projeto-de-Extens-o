t = int(input())
while t > 0:
    t -= 1

    n = int(input())
    fib = [0] * (n+2)
    fib[0] = 0
    fib[1] = 1

    for i in range(2, n+1):
        fib[i] = fib[i-1] + fib[i-2]

    print('Fib({}) = {}'.format(n, fib[n]))


