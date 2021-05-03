# 카드의 수를 오름차순으로 정렬한 뒤, 작은 카드 순으로
# 더해 나가면 최소값이 된다 생각해서 제출했는데, 오답이다.
# 단순히 모두 오름차순으로 정렬하는 것의 반례가 무엇이고
# 또 그 반례를 해결할 수 있는 풀이 방법을 고민해야겠다.
# 우선순위 큐를 사용해서 더 해주는 두 묶음의 값이 항상 최소가 될
# 수 있도록 해줘야 한다. 내가 생각했던, 그냥 단순히 오름차순으로 정렬하고
# 앞에서 2개를 고르는 식으로 하게 되면, 앞 2묶음의 합이 다음 카드 2개 보다 크게
# 될 경우가 생기면 문제가 생긴다. 따라서 매번 고르는 두 묶음이 최소가 되도록
# 우선순위 큐를 이용한다.

# card_num = []
# for _ in range(int(input())):
#     card_num.append(int(input()))
# card_num.sort()
# result = 0
# for i in range(1, len(card_num)):
#     card_num[i] += card_num[i - 1]
#     result += card_num[i]
# print(result)
# 오답 풀이
import heapq

card_num = []
result = 0
for _ in range(int(input())):
    heapq.heappush(card_num, int(input()))
while len(card_num) > 1:
    one = heapq.heappop(card_num)
    two = heapq.heappop(card_num)
    answer = one + two
    result += answer
    heapq.heappush(card_num, answer)
print(result)
