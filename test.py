position = input()

move_x = [-2, -2, -1, 1, 2, 2, -1, 1]
move_y = [-1, 1, 2, 2, 1, -1, -2, -2]

count = 0

for i in range(8):
    x = chr(ord(position[0]) - move_x[i])
    y = int(position[1]) - move_y[i]

    if x >= 'a' and x <= 'h' and y >= 1 and y <= 8:
        count += 1

print(count)