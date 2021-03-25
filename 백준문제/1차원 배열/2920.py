import sys
arr = list()
arr = list(sys.stdin.readline().split())
arr = list(map(int, arr))
arr2 = list()
arr2 = arr[:] #이렇게 index를 정해 주지 않으면 주소 값이 같은걸로 됨.
if arr2 == sorted(arr):
    print("ascending")
else:
    arr.sort(reverse=True)
    if arr2 == arr:
        print("descending")
    else:
        print("mixed")