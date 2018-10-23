## 打印 n 皇后 的解

def conflict(status, nextY) -> bool:
    nextX = len(status)
    for i in range(nextX):
        if abs(status[i] - nextY) in (0, nextX - i):
            return True
    return False


def pr(status):
    for i in status:
        print('.' * i + 'X' + '.' * (len(status) - i - 1))

def queens(num, status=[]):
    for i in range(num):
        if not conflict(status, i):
            if len(status) == num - 1:
                pr(status + [i])
                print('# # # # # # # # # #')
            else:
                queens(num,status + [i])

n = 8

queens(n)
print(n)