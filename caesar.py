key = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

pesan = input("masukkan pesan : ").upper()
enskripsi = ""

for i in pesan:
    if key.index(i) + 1 > len(key):
        enskripsi += key[0]
    else:
        enskripsi += key[key.index(i) + 1]

print(enskripsi)

dekripsi = ""

for i in enskripsi:
    if key.index(i) + 1 < 0:
        dekripsi += key[len(key) - 1]
    else:
        dekripsi += key[key.index(i) - 1]
        
print(dekripsi)