array = [[] for _ in range(10001)]
reversed_array = [[] for _ in range(10001)]


def solution(words, queries):
    answer = []
    for word in words:
        array[len(word)].append(word)
        reversed_array[len(word)].append(word[::-1])
    for i in range(10001):
        array[i].sort()
        reversed_array[i].sort()
    for q in queries:
        if q[0] != '?':
            pass
    return answer


solution(["frodo", "front", "frost", "frozen", "frame", "kakao"],
         ["fro??", "????o", "fr???", "fro???", "pro?"])