hewan = ["kucing", "ikan", "burung", "kelinci", "anjing", "ayam"]

score = 0               

print("Hallo, disini anda ditugaskan untuk menebak 3 hewan yang benar dari 6 hewan yang tersedia (hewan peliharaan). ")

hewan1 = input("Masukkan nama hewan pertama: ")
if hewan1 in hewan:
    print("Tebakan anda benar!" + hewan1)
    score += 1
else:
    print("Tebakan anda salah!" + hewan1)

hewan2 = input("Masukkan nama hewan kedua: ")
if hewan2 in hewan:
    print("Tebakan anda benar!" + hewan2)
    score += 1
else:
    print("Tebakan anda salah!" + hewan2)

hewan3 = input("Masukkan nama hewan ketiga: ")
if hewan3 in hewan:
    print("Tebakan anda benar!" + hewan3)
    score += 1
else:
    print("Tebakan anda salah!" + hewan3)

print("Skor akhir Anda: " + str(score))
