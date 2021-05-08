# 이진 탐색을 이용해서 구하려는데, 정확성 테스트는 통과를 하지만, 효율성 테스트에서
# 문제가 있다. 탐색 부분을 좀 더 최적화를 시켜야할 것 같다.
# 키워드에 따른 단어 부분을 탐색할 때, 반복문이 2중 구조로 되어있는 것이 주요
# 원인인 것 같다. 그리고, 각 키워드에 대해서 맞는 단어들을 찾을 때,
# 키워드의 ?를 a로 바꾼 것을 start, ?를 z로 바꾼 것을 end로 하면서
# 각 단어가 그 사이에 있는 단어인지를 이분탐색으로 탐색하는 것이 훨씬 더 효율적이란
# 것을 알 수 있었다.
from bisect import bisect_right, bisect_left
array = [[] for _ in range(10001)]
reversed_array = [[] for _ in range(10001)]


def search(array, start, end):
    left = bisect_left(array, start)
    right = bisect_right(array, end)
    return right - left


def solution(words, queries):
    answer = []
    for word in words:
        array[len(word)].append(word)
        reversed_array[len(word)].append(word[::-1])
    for i in range(10001):
        array[i].sort()
        reversed_array[i].sort()
    for q in queries:
        result = 0
        if q[0] != '?':     # 접미사에 ?가 있음.
            result = search(array[len(q)], q.replace('?', 'a'), q.replace('?', 'z'))
            answer.append(result)
        else:
            result = search(reversed_array[len(q)], q[::-1].replace('?', 'a'), q[::-1].replace('?', 'z'))
            answer.append(result)
    return answer


print(solution(["frodo", "front", "frost", "frozen", "frame", "kakao"],
         ["fro??", "????o", "fr???", "fro???", "pro?"]))
