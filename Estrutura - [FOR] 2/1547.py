n = int(input())
while n > 0:
    n -= 1

    qt, s = map(int,input().split())
    valores = [int(x) for x in input().split()]

    menor = 101
    pos = 0
    for i in range(qt):
        if abs(s - valores[i]) < menor:
            menor = abs(s - valores[i])
            pos = i + 1

    print(pos)
