
h = int(input())
count = 0

for i in range(h+1):
    for j in range(60):
        for k in range(60):
            if '3' in str(i) + str(j) + str(k):
                count += 1

print(count)


"""
n = int(input())
result = 0

for hour in range(0, n+1):
    first_hour = hour // 10
    second_hour = hour % 10
    if first_hour == 3 or second_hour == 3:
        result += 3600
        print("Time : ", hour, minute, second, " HOUR result : ", result)
    else:
        for minute in range(0, 60):
            first_minute = minute // 10
            second_minute = minute % 10
            if first_minute == 3 or second_minute == 3:
                result += 60
                print("Time : ", hour, minute, second, " MINUTE result : ", result)
            else:
                for second in range(0,60):
                    first_second = second // 10
                    second_second = second % 10
                    if first_second == 3 or second_second == 3:
                        result += 1
                        print("Time : ", hour, minute, second, " SECOND result : ", result)

print(result)
"""