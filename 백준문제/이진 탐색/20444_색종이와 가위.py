# 가로로 색종이를 자른 횟수를 X, 세로로 색종이를 자른 횟수를 Y이라
# 했을 때 만들어지는 색종이의 개수는, (X + 1) * (Y + 1)로 나타낼 수 있다.
# X + Y = N을 만족하는지 확인하면 된다.
# X + 1의 값을 찾으면, B는 자연스레 K / (X+1)이므로, X + 1의 값을
# 이진 탐색으로 찾기 위해서 최솟값 1, 최댓값 K으로 한다.


N, K = map(int, input().split())
cut_min = 0
cut_max = N
result = False
while cut_min <= cut_max:
    mid = (cut_min + cut_max) // 2
    other_side_cut = N - mid
    if (mid + 1) * (other_side_cut + 1) == K:
        result = True
        break
    else:
        if cut_max == cut_min:
            break
        if (mid + 1) * (other_side_cut + 1) > K:
            cut_max = mid - 1
        else:
            cut_min = mid + 1
if result:
    print("YES")
else:
    print("NO")
