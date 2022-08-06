# N개의 단어로 이루어져있으며, 각 단어는 알파벳 대문자로만
# 각 알파벳 대문자를 0~9 중 하나로 바꿔서 N 개의 수를 합
# 같은 알파벳은 같은 숫자로 바꿔야하고, 두 개 이상의 알파벳이 같은 숫자로 바뀌면 안됨.
# 그 수의 합을 최대로 만드는 프로그램 작성.
# 수의 합이 최대가 되기 위해서는 큰 자리수에 위치한 알파벳에 큰 숫자를 부여해야한다.
# 단어를 입력 받으면서 각 글자가 위치한 자릿수를 모두 기록한다.
# GCF, ACDEB의 경우로 설명하면
# G는 100, C는 1010, F는 1, A는 10000, D는 100, E는 10, B는 1이다.
# D와 G, F와 B는 같은 자리 수를 가지게 되는데 어차피 어떤 문자가 어떤 값을 가지는게
# 중요한게 아니라 최대의 값을 구하는게 목적이므로, 자리 수만 가지고 판단한다.

# 기록한 후, 각 자리수를 정렬하면, 10000, 1010, 100, 100, 1, 1이 나오는데
# 이 자리수 중 큰 수 부터 9~0의 값을 곱해주고 더하면 최대의 값을 구할 수 있다.
#

N = int(input())
word = [list(map(lambda x:ord(x) - 65, input().rstrip())) for _ in range(N)]
alphabet = [0] * 26
answer = 0
n = 9
for i in range(N):
    j = 0
    for w in word[i][::-1]:
        alphabet[w] += (10 ** j)
        j += 1
alphabet.sort(reverse=True)
for i in range(len(alphabet)):
    if alphabet[i]:
        answer += (n * alphabet[i])
        n -= 1
print(answer)
