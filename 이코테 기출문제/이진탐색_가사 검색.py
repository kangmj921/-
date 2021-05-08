# 이진 탐색을 이용해서 구하려는데, 정확성 테스트는 통과를 하지만, 효율성 테스트에서
# 문제가 있다. 탐색 부분을 좀 더 최적화를 시켜야할 것 같다.
array = [[] for _ in range(10001)]
reversed_array = [[] for _ in range(10001)]


def search(keyword, word):
    # print(keyword, word)
    start = 0
    end = len(word) - 1
    while start <= end:
        mid = (start + end) // 2
        if keyword[mid] == '?':
            end = mid - 1
        else:
            if keyword[start] == word[start]:
                start += 1
            else:
                return 0
    return 1


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
            for i in array[len(q)]:
                result += search(q, i)
            answer.append(result)
        else:
            for i in reversed_array[len(q)]:
                result += search(q[::-1], i)
            answer.append(result)
    return answer


print(solution(["frodo", "front", "frost", "frozen", "frame", "kakao"],
         ["fro??", "????o", "fr???", "fro???", "pro?"]))
