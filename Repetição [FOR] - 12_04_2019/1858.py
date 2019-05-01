n = int(input())
pessoas = [int(p) for p in input().split()]

menor = 101
pos = 0
for i in range(n):
    if pessoas[i] < menor:
        menor = pessoas[i]
        pos = i

print(pos+1)
