Money = int(input())
result = [0] * 9
change_list = [50000, 10000, 5000, 1000, 500, 100, 50, 10, 1]
for i in range(len(change_list)):
    Q, Mod = Money // change_list[i], Money % change_list[i]
    if Q > 0:
        Money = Mod
        result[i] += Q
print(result)
