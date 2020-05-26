bingoboard = list()
for x in range(3):
    bingoboard.append([int(x) for x in input().split()])
trials = int(input())

for t in range(trials):
    bingno = int(input())
    for i in range(3):
        for j in range(3):
            if bingno == bingoboard[i][j]:
                bingoboard[i][j] = 0

bingoBool = False
diag = 0
diag2 = 0
for i in range(3):
    col= 0
    row = 0
    for j in range(3):
        row += bingoboard[i][j]
        col += bingoboard[j][i]
        diag += bingoboard[i][i]
        diag2 += bingoboard[i][2-i]
    if row == 0 or col == 0:
        bingoBool = True
        break

if diag == 0 or diag2 == 0:
    bingoBool = True

if bingoBool:
    print("Yes")
else:
    print("No")
