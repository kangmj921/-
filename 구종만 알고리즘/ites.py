import sys


def generate_input_signal(n):
    a = [0]*n
    a[0] = 1983
    for i in range(1, n):
        a[i] = (a[i-1]*214013 + 2531011) % (2 ** 32)
    for k in range(len(a)):
        a[k] = a[k] % 10000 + 1
    return a


def find_part_series(signal_list, k):
    range_sum = signal_list[0]
    tail = 0
    result = 0
    for head in range(len(signal_list)):
        while range_sum < k and tail + 1 < len(signal_list):
            tail += 1
            range_sum += signal_list[tail]
        if range_sum == k:
            result += 1
        range_sum -= signal_list[head]
    return result


if __name__ == '__main__':
    for Test_Case in range(int(sys.stdin.readline())):
        K, N = map(int, sys.stdin.readline().split())
        A = generate_input_signal(N)
        print(find_part_series(A, K))
