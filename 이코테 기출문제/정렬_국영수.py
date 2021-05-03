student_list = []
for _ in range(int(input())):
    input_data = list(input().split())
    name, korean, english, math = input_data[0], int(input_data[1]), int(input_data[2]), int(input_data[3])
    student_list.append([name, korean, english, math])
student_list.sort(key=lambda x : (-x[1], x[2], -x[3], x[0]))
for i in student_list:
    print(i[0])
