def d(n):
    if n < 10:
        next_num = n + n
        return next_num
    elif 10 <= n & n < 100:
        next_num = n + (n // 10) + (n % 10)
        return next_num
    elif 100 <= n & n < 1000:
        next_num = n + (n // 100) + ((n // 10) % 10) + (n % 10)
        return next_num
    elif 1000 <= n & n < 10000:
        next_num = n + (n // 1000) + ((n // 100) % 10) + ((n // 10) % 10) + (n % 10)
        return next_num
    else:
        return


list_a = []
for p in range(1, 10001):
    k = d(p)
    list_a.append(k)

for b in range(1, 10001):
    if b in list_a:
        pass
    else:
        print(b)
