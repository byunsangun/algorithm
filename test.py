n, m, k = map(int, input().split())
arr = list(map(int,input().split()))
arr.sort()


""" 1st way by using loop
first = arr[n-1]
second = arr[n-2]
temp = 0
sum = 0

for i in range(m):
    if temp < k:
        sum = sum + first
        temp = temp + 1
    else:
        temp = 0
        sum = sum + second

print(sum)
"""


# 2nd way which is better than first one
first = arr[n-1]
second = arr[n-2]

total_first = int(m / (k+1)) * k
total_second = int(m / (k+1))
remain_first = int(m % (k+1))


result = (first * (total_first + remain_first)) + (second * total_second)
print(result)







