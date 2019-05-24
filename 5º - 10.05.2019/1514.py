while True:
    n, m = map(int, input().split())
    if n == 0 and m == 0:
        break

    matriz = []
    cont = 0
    # Inicialmente tomamos todas as preposições como verdadeiras
    prop1 = prop2 = prop3 = prop4 = True

    # Preenchimento da matriz
    for i in range(n):
        matriz.append([int(v) for v in input().split()])

        # soma de toda a linha (i) da matriz
        soma = sum(matriz[i])

        # 1. Alguém resolveu todos os problemas
        if soma == m:
            prop1 = False

        # 4. Alguém não resolveu nenhum problema
        if soma == 0:
            prop4 = False

    #Será utilizado para contar a quantidade de vezes que um problema (i) foi resolvido
    problemas = [0] * m

    for j in range(m):
        for i in range(n):
            problemas[j] += matriz[i][j]

    for valor in problemas:
        if valor == 0:  # 2. Algum problema não foi resolvido por ninguém
            prop2 = False
        if valor == n:  # 3. O problema foi resolvido por todos
            prop3 = False

    # Analisando as preposições, se forem verdadeiras, incremento o contador
    if prop1:
        cont += 1

    if prop2:
        cont += 1

    if prop3:
        cont += 1

    if prop4:
        cont += 1

    print(cont)

