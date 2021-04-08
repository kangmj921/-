import sys


def first_char_in_game_pan(n, ob_word, cache, game_pan):
    for i in range(5):
        for j in range(5):
            if ob_word[n] == game_pan[i][j]:
                cache.append((i, j))


def next_char_in_game_pan(ob_char, cache1, n, game_pan):
    cache2 = list()
    if n < len(ob_char):
        for i in range(len(cache1)):
            (x, y) = cache1[i]
            if x - 1 >= 0 and y - 1 >= 0 and game_pan[x - 1][y - 1] == ob_char[n]:
                cache2.append((x - 1, y - 1))
            if x - 1 >= 0 and game_pan[x - 1][y] == ob_char[n]:
                cache2.append((x - 1, y))
            if y - 1 >= 0 and game_pan[x][y - 1] == ob_char[n]:
                cache2.append((x, y - 1))
            if x + 1 <= 4 and y + 1 <= 4 and game_pan[x + 1][y + 1] == ob_char[n]:
                cache2.append((x + 1, y + 1))
            if x + 1 <= 4 and game_pan[x + 1][y] == ob_char[n]:
                cache2.append((x + 1, y))
            if y + 1 <= 4 and game_pan[x][y + 1] == ob_char[n]:
                cache2.append((x, y + 1))
            if x + 1 <= 4 and y - 1 >= 0 and game_pan[x + 1][y - 1] == ob_char[n]:
                cache2.append((x + 1, y - 1))
            if y + 1 <= 4 and game_pan[x - 1][y + 1] == ob_char[n] and x - 1 >= 0:
                cache2.append((x - 1, y + 1))
            else:
                pass
        cache2 = list(set(cache2))
        next_char_in_game_pan(ob_char, cache2, n + 1, game_pan)
    else:
        if cache1:
            print("".join(ob_char) + " YES")
        else:
            print("".join(ob_char) + " NO")


C = int(input())
for k in range(C):
    game_pan = [list(sys.stdin.readline().rstrip('\n')) for row in range(5)]
    N = int(input())
    word = [list(sys.stdin.readline().rstrip('\n')) for row in range(N)]
    for i in range(len(word)):
        cache = list()
        first_char_in_game_pan(0, word[i], cache, game_pan)
        next_char_in_game_pan(word[i], cache, 1, game_pan)
