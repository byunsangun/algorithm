def binary_search(array, target, start, end):
    if start > end:
        return None

    mid = (start + end) // 2

    if array[mid] == target:
        return mid
    elif array[mid] > target:
        return binary_search(array, target, start, mid - 1)
    else:
        return binary_search(array, target, mid + 1, end)


n = int(input())
array = list(map(int, input().split()))
array.sort()

m = int(input())
require = list(map(int, input().split()))


for item in require:
    temp = binary_search(array, item, 0, len(array)-1)
    if temp == None:
        print("no", end=' ')
    else:
        print("yes", end=' ')