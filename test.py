#solution 1
n = int(input())
x, y = 1, 1
plans = input().split()

dx = [0,0, -1, 1]
dy = [-1, 1, 0, 0]
move_types = ['L', 'R', 'U', 'D']

for plan in plans:
    for i in range(len(move_types)):
        if plan == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]

    if nx < 1 or ny < 1 or nx > n or nx > y:
        continue

    x, y = nx, ny

print(x,y)


#solution 2
"""
n = int(input())
arr = list(input().split())

x = 1
y = 1

for i in arr:
    if i == 'R':
        if x < n:
            x += 1
    elif i == 'L':
        if x > 1:
            x -= 1
    elif i == 'U':
        if y > 1:
            y -= 1
    elif i == 'D':
        if y < n:
            y += 1

print(y, x)
"""


