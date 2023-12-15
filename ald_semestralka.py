#vypracovali:
#Jan Sodomka, Jiří Šeps, Martin Šimon, Tomáš Rychlý

import random
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

def valid_number(pole, radek, sloupec):
    
    # Seznam možných čísel
    moznosti = [1, 2, 3, 4, 5, 6]

    # Podmínky pro jednotlivá čísla
    if 1 in moznosti and (sloupec == 0 or pole[radek][sloupec-1] not in [2, 3] or (radek > 0 and pole[radek-1][sloupec] != 5)):
        moznosti.remove(1)
    if 2 in moznosti and ((radek > 0 and pole[radek-1][sloupec] not in [2, 3, 4, 6]) or (sloupec > 0 and pole[radek][sloupec-1] not in [4, 5, 6])):
        moznosti.remove(2)
    if 3 in moznosti and ((radek > 0 and pole[radek-1][sloupec] not in [1, 5]) or (sloupec > 0 and pole[radek][sloupec-1] not in [4, 5, 6])):
        moznosti.remove(3)
    if 4 in moznosti and ((radek > 0 and pole[radek-1][sloupec] not in [1, 5]) or (sloupec > 0 and pole[radek][sloupec-1] not in [1, 2, 3])):
        moznosti.remove(4)
    if 5 in moznosti and ((radek > 0 and pole[radek-1][sloupec] not in [2, 3, 4, 6]) or (sloupec > 0 and pole[radek][sloupec-1] not in [1, 2, 3])):
        moznosti.remove(5)
    if 6 in moznosti and ((radek > 0 and pole[radek-1][sloupec] not in [2, 3, 4, 6]) or (sloupec > 0 and pole[radek][sloupec-1] not in [4, 5, 6])):
        moznosti.remove(6)

    # Náhodný výběr z možných čísel
    return random.choice(moznosti)

def main():
    # Získání šířky a výšky od uživatele
    sirka = int(input("Zadejte šířku 2D pole: "))
    vyska = int(input("Zadejte výšku 2D pole: "))
    
    #hodnoty pro terstování bez inputu
    #sirka = 20
    #vyska = 10
    
    pole = [[0 for _ in range(sirka)] for _ in range(vyska)]
    for i in range(vyska):
        for j in range(sirka):
            pole[i][j]= valid_number(pole, i, j)
    
    # Výpis 2D pole - pro debuging
    for radek in pole:
        print(radek)

    # Vykreslení obrázku
    fig, axs = plt.subplots(vyska, sirka)
    for i in range(vyska):
        for j in range(sirka):
            img = mpimg.imread('obrazek' + str(pole[i][j]) + '.png')
            axs[i, j].imshow(img)
            axs[i, j].axis('off')  # Skrytí os
    plt.show()


if __name__ == "__main__":
    main()