n, m = map(int, input().split())

d = [[0] * m for _ in range(n)]

x, y, direction = map(int, input().split())
d[x][y] = 1

game_map = []
move = [[-1,0], [0,1], [1, 0], [0, -1]]
count = 1
turn_time = 0

for i in range(n):
    game_map.append(list(map(int, input().split())))


def turn_left():
    global direction

    if direction == 0:
        direction = 3
    else:
        direction -= 1


while True:

    turn_left()

    temp_x = x + move[direction][0]
    temp_y = y + move[direction][1]

    if d[temp_x][temp_y] == 0 and game_map[temp_x][temp_y] == 0:

        x = temp_x
        y = temp_y

        d[x][y] = 1
        count += 1
        turn_time = 0
        print("count : ", count)
        continue

    else:
        print("turn!!!")
        turn_time += 1

    if turn_time == 4:
        temp_x = x - move[direction][0]
        temp_y = y - move[direction][1]

        if game_map[temp_x][temp_y] == 0:
            x = temp_x
            y = temp_y

        else:
            break

        turn_time = 0


print(count)

