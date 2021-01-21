n, k = map(int, input().split())
result = 0

# solution 1
while True:
    target = (n // k) * k
    result += (n - target)
    n = target

    if n < k:
        break
    result += 1
    n //= k

result += (n - 1)
print(result)


# solution 2
"""
n, k = map(int, input().split())

count = 0
while True:
    if n == 1:
        break
    elif n % k == 0:
        n = n // k
        count += 1
    else:
        n = n - 1
        count += 1


print(count)
"""
