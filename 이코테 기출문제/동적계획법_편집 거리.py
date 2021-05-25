A = input().rstrip('\n')
B = input().rstrip('\n')
dp_list = [1e9] * 5000
for i in range(len(B)):
    if A[i] != B[i]:
        dp_list[i] = min(dp_list[i], 1 + dp_list[i - 1])
    else:
        dp_list[i] = 0
print(A, B, dp_list)
