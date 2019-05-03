n = int(input())
for i in range(n):
    x, y = map(int, input().split())

    sum_impar = 0
    if x < y:
        for v in range(x+1, y):
            if v % 2 != 0:
                sum_impar += v

    elif x > y:
        for v in range(x-1, y, -1):
            if v % 2 != 0:
                sum_impar += v

    print(sum_impar)
