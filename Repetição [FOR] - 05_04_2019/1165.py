""""
A partir do número 2 até (X-1), procura-se a ocorrência de algum outro número que seja
divisor de X se houver, X não pode ser primo, ou seja, se X tiver algum outro divisor entre 2 e X
X não é um número primo.
"""

n = int(input())

for i in range(n):
    x = int(input())

    eh_primo = True

    for j in range(2, x):
        if x % j == 0:
            eh_primo = False
            break

    if eh_primo:
        print('{} eh primo'.format(x))
    else:
        print('{} nao eh primo'.format(x))
