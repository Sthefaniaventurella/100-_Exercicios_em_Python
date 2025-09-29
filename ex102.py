def fatorial(num=1, s=False):
    f = 1
    for c in range(num, 0, -1):
        f *= c
    if s:
        for c in range(num, 0, -1):
            print(c, end='')
            if c > 1:
                print(' x ', end='')
        print(' =',f)
    else:
        return f
print(fatorial(5))
