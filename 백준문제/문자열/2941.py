croaia_alphabet = {'c=': 1, 'c-': 2, 'dz=': 3, 'd-': 4,
                   'lj': 5, 'nj': 6, 's=': 7, 'z=': 8}
croaia_alphabet_keys = list(croaia_alphabet.keys())
W = input()
replace_W = W
for k in range(len(croaia_alphabet_keys)):
    while replace_W.find(croaia_alphabet_keys[k]) >= 0:
        replace_W = replace_W.replace(croaia_alphabet_keys[k], '.', 1)
print(len(replace_W))
