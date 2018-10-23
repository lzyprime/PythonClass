## n 皇后解的数量
n = 8
upperlim = (1 << n) - 1
ans = 0


def test(row, ld, rd):
    global upperlim
    global ans
    if row != upperlim:
        pos = upperlim & ~(row | ld | rd)
        while pos:
            p = pos & -pos
            pos -= p
            test(row + p, (ld + p) << 1, (rd + p) >> 1)
    else:
        print(row, ld, rd)
        ans += 1


test(0, 0, 0)

print(ans)