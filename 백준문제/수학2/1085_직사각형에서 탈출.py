x, y, w, h = map(int, input().split())
current_position_x = x
current_position_y = y
right_top_x = w
right_top_y = h
X = right_top_x - current_position_x
Y = right_top_y - current_position_y
distance = list()
if X > right_top_x/2:
    distance.append(x)
else:
    distance.append(X)
if Y > right_top_y/2:
    distance.append(y)
else:
    distance.append(Y)
print(min(distance))