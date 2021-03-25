import sys


# 지금까지 주유 가격보다 이번 도시에서의 가격이 작으면 지금까지 왔던 거리*가장 작았던 주유 가격을 곱하고
# 결과를 더해준다. 그리고 주유 가격을 제일 작은 각겨으로 바꾼다.
# 마지막 도로에서 넘어갈 때 가격을 계산한다.
N = int(input())
road_list = list(map(int, sys.stdin.readline().split()))
gas_station_list = list(map(int, sys.stdin.readline().split()))
prev = gas_station_list[0]
result = gas_station_list[0] * road_list[0]
distance = 0
for i in range(1, N-1):
    if gas_station_list[i] < prev:
        result += prev * distance
        distance = road_list[i]
        prev = gas_station_list[i]
    else:
        distance += road_list[i]
    if i == N - 2:
        result += prev * distance
print(result)
