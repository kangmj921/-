S = input()
S = S.upper().lower()
s = list(set(S))
result = list()
for k in range(len(s)):
    result.append(S.count(s[k]))
if result.count(max(result)) > 1:
    print("?")
else:
    print(str(s[result.index(max(result))]).upper())