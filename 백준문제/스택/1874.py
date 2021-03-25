import sys
sys.setrecursionlimit(10**6)


def make_serial(serial, st, i):
    a = serial[i]
    if st[-1] != a:
        global j
        k = 0
        for k in range(j, a + 1):
            st.append(k)
            output_stack.append('+')
        j = k + 1
    b = st.pop()
    if b == a:
        output_stack.append('-')
    else:
        print('NO')
        return
    if i + 1 < len(serial):
        make_serial(serial, st, i + 1)
    else:
        for p in range(len(output_stack)):
            print(output_stack[p])
        return


if __name__ == '__main__':
    serial_int = list()
    for N in range(int(sys.stdin.readline())):
        serial_int.append(int(sys.stdin.readline()))
    stack = [0]
    output_stack = []
    j = 1
    make_serial(serial_int, stack, 0)
