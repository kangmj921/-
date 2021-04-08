import sys


n_list = list(map(int, sys.stdin.readline().rstrip('\n')))

result = 0
for i in n_list:
    if result == 0 or i <= 1:
        result += i
    else:
        result *= i
print(result)
