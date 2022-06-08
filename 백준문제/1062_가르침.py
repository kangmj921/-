#  N이 50보다 작거나 같고, 각 단어는 8~15, K는 26보다 작거나 같다.
#  이미 입력 받은 1개의 단어마다 set 자료형으로 만들고, antci를 제외한 중복되지 않은 문자가
#  어떤 것이 있는지 확인한다.
#  모든 중복되지 않은 문자들에 대해서 K - 5 개의 문자로 이루어진 조합을 만들어야 하는데,
#  그냥 모든 조합을 combination을 이용해서 구할 경우 시간초과에 걸릴 가능성이 있다.
#  antci를 제외한 문자들을 DFS를 이용한 백트래킹으로 구현한다.
#  그런데 시간초과가 발생하여 문자끼리 일일히 비교하는 방법 말고, 해당 알파벳을 배웠는지
#  나타내는 배열을 만들어 그 배열에 배운 알파벳 순서들의 정보를 저장하는 식으로 바꾸었다.
import sys


def search(start_temp, n):
    global answer
    if n == 0:
        answer = max(answer, check())
        return
    for i in range(start_temp, len(alpha_list)):
        if not alpha_list[i]:
            alpha_list[i] = True
            search(i + 1, n - 1)
            alpha_list[i] = False


def check():
    result = 0
    for word in temp:
        for w in word:
            if not alpha_list[ord(w) - ord('a')]:
                break
        else:
            result += 1
    return result


N, K = map(int, input().split())
word_list = [sys.stdin.readline().rstrip() for _ in range(N)]
temp, dict_ = [], {}
stack = []
answer = 0
s = ['a', 'n', 't', 'c', 'i']
alpha_list = [False] * 26
for i in s:
    alpha_list[ord(i) - ord('a')] = True
if K < 5:
    print(answer)
elif K == 26:
    print(N)
else:
    target = K - 5
    for i in word_list:
        temp.append(list(set(i)))
    search(0, target)
    # print(temp, target)
    print(answer)
