l, c = map(int, input().split())
matriz = [0] * l

a, b = map(int, input().split())

for i in range(l):
    matriz[i] = [int(v) for v in input().split()]


# Decremento o valor de a e b pois computacionalmente, os arrays são indexados a partir da posição 0.
a -= 1
b -= 1
matriz[a][b] = 0
# Sempre que uma posição for visitada, marque-a como um ladrinho branco (0) para que a visita não se repita.

while True:
    # Verifica se a posição acima da atual é válida e o ladrilho é preto.
    if a-1 >= 0 and matriz[a-1][b] == 1:
        matriz[a-1][b] = 0 # Marca o ladrilho como visitado (0).
        a -= 1 # Atualiza a posição.

    # Verifica se a posição abaixo da atual é válida e o ladrilho é preto.
    elif a+1 < l and matriz[a+1][b] == 1:
        matriz[a+1][b] = 0
        a += 1

    # Verifica se a posição a esquerda da atual é válida e o ladrilho é preto.
    elif b-1 >= 0 and matriz[a][b-1] == 1:
        matriz[a][b-1] = 0
        b -= 1

    # Verifica se a posição a direita da atual é válida e o ladrilho é preto.
    elif b+1 < c and matriz[a][b+1] == 1:
        matriz[a][b+1] = 0
        b += 1
    else:
        break

# Incremento a e b, pois o problema enxerga os arrays como indexados a partir da posição 1 e não em 0 como computacionalmente.
print('{} {}'.format(a+1, b+1))
