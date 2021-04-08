import sys

input_data = list(map(int, sys.stdin.readline().rstrip('\n')))
middle = int(len(input_data) / 2)
left_data = sum(input_data[:middle])
right_data = sum(input_data[middle:])
if left_data == right_data:
    print('LUCKY')
else:
    print('READY')
