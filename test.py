n, m = map(int, input().split())

array = []
d = [10001] * 10001
d[0] = 0

for _ in range(n):
    array.append(int(input()))

for i in range(1, m+1):
    for j in array:
        if i - j >= 0:
            if d[i - j] != 10001:
                d[i] = min(d[i], d[i - j] + 1)


if d[m] == 10001:
    print(-1)
else:
    print(d[m])


