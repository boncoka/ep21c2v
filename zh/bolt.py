


class Bolt:
    """
    A vásárlásokat kezelő osztály. Az osztály egyetlen attribútuma a kosarak listája.
    """

    def __init__(self):
        """
        A bolt létrehozásakor beállítja az osztály attribútumait.
        """
        pass

    def feladat_1(self, filepath: str) -> None:
        try:
            print("1. feladat")
            vasarlas = []
            egyvasarlas = []

            with open("kosar.txt", "r", ) as i:
                for elem in i:
                    elem = elem.strip()
                    if elem != "F":
                        egyvasarlas.append(elem)
                    else:
                        vasarlas.append(egyvasarlas)
                        egyvasarlas = []
        except ValueError:
            print("Hibasan megadott ertek")
        pass

    def feladat_2(self) -> None:

        try:
            print("2. feladat")
            hanyszor_fizettek = len(vasarlasok)
            print(f"Ennyiszer fizettek: {hanyszor_fizettek}")
            pass
        except ValueError:
            print("Hibasan megadott ertek")
    def feladat_3(self) -> None:
        try:

            print("3. feladat")
            sorszam = int(input("Adja meg a vasarlas sorszamat: "))
            sorszam_darab = len(vasarlasok[sorszam])
            print(f"A {sorszam}. vasarlo kosaraban ennyi termek volt: {sorszam_darab}")

            kosar = ()
            for egyvasarlas in vasarlasok[sorszam - 1]:
                if egyvasarlas not in kosar.keys():
                    kosar[egyvasarlas] = 1
                else:
                    kosar[egyvasarlas] = kosar[egyvasarlas] + 1
            for cikk, db in kosar.items():
                print(f"{cikk}:{db}")
        except ValueError:
            print("Hibasan megadott ertek")
        pass

    def feladat_4(self) -> None:
        try:
            print("4. feladat")

            arucikk = input("Adja meg az arucikk nevet: ")

            cikkvasarlasai = []
            i = 0
            for kosar in vasarlasok:
                if arucikk in kosar:
                    cikkvasarlasai.append(i)
                i += 1
            print(f"Az elso es utolso {arucikk} vasarlas")
            print(f"Eloszor a {cikkvasarlasai[0]}, Utoljara a {cikkvasarlasai[len(cikkvasarlasai)-1]}")
            print(f"Osszesen {len(cikkvasarlasai)} vasaroltak meg")
        except ValueError:
            print("Hibasan megadott ertek")
        pass

    def feladat_5(self, filepath: str) -> None:

        try:
            with open("osszeg.txt", "w") as i:
                i = 0
                for egyvasarlas in vasarlasok:
                    osszeg = 0
        except ValueError:
            print("Hibasan megadott ertek")
        pass
