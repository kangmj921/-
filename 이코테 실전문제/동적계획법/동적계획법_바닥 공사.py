# 왼쪽 부터 덮개를 채워나간다고 했을 떄, i 번째에 채우는 경우의 수는
# i - 1 번째까지 채워져 있는 덮개에서 2 x 1 덮개 하나를 추가하는 경우 한 가지,
# i - 2 번째까지 채워져 있는 덮개에서 2 x 2 하나, 1 x 2 두개를 추가하는 경우 두 가지
# 로 전체 경우의 수는 따라서, ai = (ai-1 + ai-2*2)로 나타낼 수 있다.
N = int(input())
result_list = [0] * (N + 1)
result_list[1] = 1
result_list[2] = 3
for i in range(3, N + 1):
    result_list[i] = (result_list[i - 1] + 2 * result_list[i - 2]) % 796796
print(result_list[N])
