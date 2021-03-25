def fibonacci(N):
    if num_list[N].count(0) != 2:
        return num_list[N]
    else:
        if N == 0:
            return [1, 0]
        elif N == 1:
            return [0, 1]
        else:
            num_list[N] = [x+y for x, y in zip(fibonacci(N-1), fibonacci(N-2))]
            #두 리스트간의 원소 합치기
            return num_list[N]


if __name__=='__main__':
    num_list = [[0, 0] for i in range(41)]
    num_list[0] = [1, 0]
    num_list[1] = [0, 1]
    for N in range(int(input())):
        number = int(input())
        fibonacci(number)
        print(num_list[number][0], num_list[number][1])