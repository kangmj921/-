N = int(input())
bongdari_5 = N // 5
bongdari_3 = 0
total_bongdari = list()
result = 0
for k in range(bongdari_5+1):
    bongdari_3 = N - 5 * k
    if bongdari_3 % 3 == 0:
        total_bongdari.append(k + (bongdari_3 // 3))
try:
    result = min(total_bongdari)
except:
    result = -1
print(result)