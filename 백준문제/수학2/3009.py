X_position = list()
Y_position = list()
for k in range(3):
    X, Y = map(int, input().split())
    X_position.append(X)
    Y_position.append(Y)
for t in range(3):
    if X_position.count(X_position[t]) == 1:
        print(X_position[t], end=" ")
    if Y_position.count(Y_position[t]) == 1:
        print(Y_position[t])