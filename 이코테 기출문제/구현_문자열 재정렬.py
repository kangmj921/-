import sys

input_data = list(sys.stdin.readline().rstrip('\n'))
input_data.sort()
result_num, i = 0, 0
result = ''
for i in range(len(input_data)):
    try:
        result_num += int(input_data[i])
    except:
        result += input_data[i]
    i += 1
print(result + str(result_num))
