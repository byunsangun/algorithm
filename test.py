n, m = map(int, input().split())
array = list(map(int,input().split()))

array.sort()


def binary_search(array, target, start ,end):
    if start > end:
        return None

    mid = (start + end) // 2
    sum = 0

    for i in array:
        if i > mid:
            sum += i - mid

    if sum == target:
        return mid
    elif sum > target:
        return binary_search(array, target, mid + 1, end)
    else:
        return binary_search(array, target, start, mid - 1)


result = binary_search(array, m, 0, max(array))
print("result : ", result)





"""
순차 탐색
standard = max(array)

while standard>0:
    sum = 0
    for i in array:
        if (i - standard) > 0:
            sum += i - standard

    if sum >= m:
        break
    else:
        standard -= 1


print("standard : ", standard)
"""

