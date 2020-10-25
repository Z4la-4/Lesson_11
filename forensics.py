

characteristics = {
    "black_hair": "CCAGCAATCGC",
    "brown_hair": "GCCAGTGCCG",
    "blonde_hair": "TTAGCTATCGC",
    "Square_face": "GCCACGG",
    "Round_face": "ACCACAA",
    "Oval_face": "AGGCCTCA",
    "Blue_eyes": "TTGTGGTGGC",
    "Green_eyes": "GGGAGGTGGC",
    "Brown_eyes": "AAGTAGTGAC",
    "Female": "TGAAGGACCTTC",
    "Male": "TGCAGGAACTTC",
    "White": "AAAACCTCA",
    "Black": "CGACTACAG",
    "Asian": "CGCGGGCCG",
}

characteristics_set = []


Eva = ["Female", "White", "blonde_hair", "Blue_eyes", "Oval_face"]
Larisa = ["Female", "White", "brown_hair", "Brown_eyes", "Oval_face"]
Matej = ["Male", "White", "black_hair", "Blue_eyes", "Oval_face"]
Miha = ["Male", "White", "brown_hair", "Green_eyes", "Square_face"]

Eva.sort()
Larisa.sort()
Matej.sort()
Miha.sort()

with open('dna.txt', 'r') as perpetrator:
    search = perpetrator.read()

    for key in characteristics:
        x = characteristics.get(key)
        y = search.find(x)

        if y != -1:
            characteristics_set.append(key)

characteristics_set.sort()

if  characteristics_set == Eva:
    print("Storilec je: Eva")
elif characteristics_set == Larisa:
    print("Storilec je: Larisa")
elif characteristics_set == Matej:
    print("Storilec je: Matej")
else:
    print("Storilec je: Miha")

