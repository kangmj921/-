M = int(input())
N = int(input())
prime_number = list()
j = 0
for k in range(M, N + 1):
    prime_number.append(k)
try:
    prime_number.remove(1)
except:
    pass
for i in range(len(prime_number)):
    check_number = prime_number[j]
    for m in range(2, check_number + 1):
        if check_number % m == 0 and check_number != m:
            try:
                prime_number.remove(check_number)
                break
            except:
                pass
        elif m == check_number:
            j += 1
            break
if len(prime_number) == 0:
    print(-1)
else:
    print(sum(prime_number[:]))
    print(min(prime_number))
