while True:

    n, m, s = map(int, input().split())
    if n+m+s == 0:
        break

    arena = []
    polos = 'NLSO'
    movimentos = [-1, 1, 1, -1]

    for i in range(n):
        linha = input()
        arena.append([0]*m)
        for j in range(m):
            arena[i][j] = linha[j]
            if linha[j].isalpha():
                x = i
                y = j
                orient = arena[i][j]

    instrucoes = input()
    arena[x][y] = '.'

    figurinhas = 0
    for i in instrucoes:
        if i == 'D':
            orient = polos[(polos.find(orient) + 1) % 4]
        elif i == 'E':
            orient = polos[(polos.find(orient) + 3) % 4]
        else:
            mov = movimentos[polos.find(orient)]

            if orient == 'O' or orient == 'L':
                if 0 <= y + mov < m:
                    if arena[x][y+mov] == '.':
                        y += mov
                    elif arena[x][y+mov] == '*':
                        figurinhas += 1
                        arena[x][y+mov] = '.'
                        y += mov
            else:
                if 0 <= x + mov < n:
                    if arena[x+mov][y] == '.':
                        x += mov
                    elif arena[x+mov][y] == '*':
                        figurinhas += 1
                        arena[x+mov][y] = '.'
                        x += mov
    print(figurinhas)
