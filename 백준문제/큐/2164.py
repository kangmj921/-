import sys
from collections import deque


if __name__ == '__main__':
    dq = deque()
    N = int(sys.stdin.readline())
    for k in range(1, N+1):
        dq.append(k)
    for _ in range(1, N):
        dq.popleft()
        dq.append(dq.popleft())
    print(dq[0])
