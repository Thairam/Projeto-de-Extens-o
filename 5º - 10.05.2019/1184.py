op = input()
matriz = [[0] * 12] * 12

soma = 0
for i in range(12):
    for j in range(12):
        matriz[i][j] = float(input())
        if j < i:
            soma += matriz[i][j]

if op == 'S':
    print('{:.1f}'.format(soma))
else:
    print('{:.1f}'.format(soma/66))
