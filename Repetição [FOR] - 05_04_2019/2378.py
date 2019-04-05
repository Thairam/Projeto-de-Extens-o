n,capacidade = map(int, input().split())
excedeu = False
qtd_pessoas_no_elevador = 0
for i in range(n):
    s,e = map(int, input().split())
    qtd_pessoas_no_elevador -= s
    qtd_pessoas_no_elevador += e

    if qtd_pessoas_no_elevador > capacidade:
        excedeu = True

if excedeu:
    print('S')
else:
    print('N')
