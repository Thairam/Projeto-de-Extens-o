n = int(input())
valores = [0] * 2001
for i in range(n):
    x = int(input())
    valores[x] += 1

for i in range(len(valores)):
    if valores[i] != 0:
        print('{} aparece {} vez(es)'.format(i, valores[i]))
