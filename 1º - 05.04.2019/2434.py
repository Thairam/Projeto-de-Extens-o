n, saldo = map(int, input().split())

menor_saldo = saldo
for i in range(n):
    v = int(input())
    saldo += v
    if saldo < menor_saldo:
        menor_saldo = saldo

print(menor_saldo)
