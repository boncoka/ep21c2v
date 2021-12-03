try:
    print("1. feladat")
    vasarlas = []
    egyvasarlas = []


    with open("kosar.txt", "r",) as i:
        for elem in i:
            elem = elem.strip()
            if elem != "F":
                egyvasarlas.append(elem)
            else:
                vasarlas.append(egyvasarlas)
                egyvasarlas = []
    print("2. feladat")
    hanyszor_fizettek = len(vasarlas)
    print(f"Ennyiszer fizettek: {hanyszor_fizettek}")

    print("3. feladat")
    sorszam = int(input("Adja meg a vasarlas sorszamat: "))
    sorszam_darab = len(vasarlas[sorszam])
    print(f"A {sorszam}. vasarlo kosaraban ennyi termek volt: {sorszam_darab}")

    kosar = ()
    for egyvasarlas in vasarlas[sorszam - 1]:
        if egyvasarlas not in kosar.keys():
            kosar[egyvasarlas] = 1
        else:
            kosar[egyvasarlas] = kosar [egyvasarlas] + 1
    for cikk, db in kosar.items():
        print(f"{cikk}:{db}")






    print("4. feladat")

    arucikk = input("Adja meg az arucikk nevet: ")

    cikkvasarlasai = []
    i = 0
    for kosar in vasarlas:
        if arucikk in kosar:
            cikkvasarlasai.append(i)
        i += 1
    print(f"Az elso es utolso {arucikk} vasarlas")
    print(f"Eloszor a {cikkvasarlasai[0]}, Utoljara a {cikkvasarlasai[len(cikkvasarlasai)-1]}")
    print(f"Osszesen {len(cikkvasarlasai)} vasaroltak meg")



    print("5. feladat")

    with open("osszeg.txt", "w") as i:
        i = 0
        for egyvasarlas in vasarlas:
            osszeg = 0

except ValueError:
    print("hibas ertek")