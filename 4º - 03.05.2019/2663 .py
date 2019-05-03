n = int(input())
k = int(input())

pontuacoes = []
for i in range(n):
    p = int(input())
    pontuacoes.append(p)

pontuacoes.sort(reverse=True)

classificados = k
for i in range(k, len(pontuacoes)):
    if pontuacoes[i-1] == pontuacoes[i]:
        classificados += 1
    else:
        break

print(classificados)
