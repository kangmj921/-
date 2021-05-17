# 각 수에 대해 1,2,3의 합으로 나타내는 경우의 수는,
# 1을 뺀 값의 경우의 수, 2를 뺀 값의 경우의 수, 3을 뺀 값의 경우의
# 수를 합친 것과 같다.
# 따라서 점화식으로 나타내게 되면, 다음과 같다.
# ai = ai-1 + ai-2 + ai-3
for _ in range(int(input())):
    n = int(input())
    num_list = [0] * 12
    num_list[1], num_list[2], num_list[3] = 1, 2, 4
    for i in range(4, n + 1):
        num_list[i] = num_list[i - 1] + num_list[i - 2] + num_list[i - 3]
    print(num_list[n])
