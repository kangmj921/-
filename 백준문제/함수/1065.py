N = int(input())


def find_hansu(N):
    result = 0
    for k in range(1, N+1):
        arr = list(map(int, str(k)))
        if len(arr) == 1 or len(arr) == 2:
            result += 1
        else:
            if (arr[0] + arr[len(arr) - 1]) == (2 * (arr[len(arr) // 2])) and len(arr) % 2 == 1:
                result += 1
            elif (arr[0] + arr[len(arr) - 1]) == (arr[(len(arr) // 2) - 1] + arr[len(arr) // 2]) and len(arr) % 2 == 0:
                result += 1
            else:
                result += 0
    return result


print(find_hansu(N))
