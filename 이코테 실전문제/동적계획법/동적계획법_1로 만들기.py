# 문제에서 요구하는 내용을 점화식으로 표현하면,
# ai = min(ai-1, ai/2, ai/3, ai/5) + 1로 나타낼 수 있다.
# 1을 뺄 때를 빼면 나머지 연산은 해당 수로 나누어 떨어질때만 진행됨.
X = int(input())
result = [0] * (X + 1)
for i in range(2, X + 1):
    result[i] = result[i - 1] + 1
    if i % 2 == 0:
        result[i] = min(result[i], result[i // 2] + 1)
    if i % 3 == 0:
        result[i] = min(result[i], result[i // 3] + 1)
    if i % 5 == 0:
        result[i] = min(result[i], result[i // 5] + 1)
print(result[X])
