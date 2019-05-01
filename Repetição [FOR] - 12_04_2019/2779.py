n = int(input())
m = int(input())
album = [0] * n

for i in range(m):
    fig = int(input())
    album[fig-1] = True

faltam = 0
for figurinha in album:
    if not figurinha:
        faltam += 1

print(faltam)
