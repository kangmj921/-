import sys


if __name__ == '__main__':
    for C in range(int(input())):
        N = int(input())
        square = 0
        width = 0
        stack = []
        Max = 0
        height = list(map(int, sys.stdin.readline().split()))
        height.append(0)
        for k in range(N+1):
            print("stack1", stack, square, k)
            while stack and height[stack[-1]] >= height[k]:
                last_index = stack.pop()
                print("stack:", stack)
                if not stack:
                    width = k
                else:
                    width = k - stack[-1] - 1
                square = width * height[last_index]
                print(width, square)
                Max = max(Max, square)
                print("Max", Max)
            stack.append(k)
        print(Max)
