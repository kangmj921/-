import sys


def get_LIS(start):
    for next in range(start+1, ):
        pass
    pass


if __name__ == '__main__':
    for Test_Case in range(int(sys.stdin.readline())):
        seq_length = int(sys.stdin.readline())
        seq_numbers = list(map(int, sys.stdin.readline().split()))
        cache_list = [0 for k in range(seq_length)]
        print(seq_numbers, cache_list)
        print(get_LIS(0))