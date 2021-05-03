student_list = []
for _ in range(int(input())):
    input_data = input().split()
    name, score = input_data[0], int(input_data[1])
    student_list.append([name, score])
student_list.sort(key=lambda x: x[1])
for i in student_list:
    print(i[0], end=' ')
