n, m= map(int, input().split())

result = 0

# using min(), max()
for i in range(n):
    data = list(map(int, input().split()))
    min_value = min(data)
    result = max(result, min_value)

print(result)


# without using min(), max()
"""
arr = []
for i in range(n):
    arr.append(list(map(int, input().split())))

for i in arr:
    min = 10001
    max = 0
    for j in i:
        if j < min:
            min = j
    if min > max:
        max = min

print(max)
"""
