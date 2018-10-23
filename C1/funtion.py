def avg(* real):
    avg = sum(real) / len(real)
    l = [avg] + [i for i in real if i > avg]
    return tuple(l)

print(avg(1, 2, 3, 4, 5, 6))
