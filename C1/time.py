import time
year, month, day = time.localtime()[:3]

months = [31,28,31,30,31,30,31,31,30,31,30,31]

if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
    months[1] = 29

ans = sum(months[:month - 1]) + day

print(ans)