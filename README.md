</h> Popis kódu </h>

Tento kód vytváří 2D pole o určené šířce a výšce, kde každý prvek pole je vybrán náhodně z možných čísel podle několika pravidel(budou vložena vespod README).
Inspirace pro výběr obrázků, čísel a logiky za touto úlohou je ze zadání Semestrální práce na předmět ALD, kde byly i vzorové obrázky pro tuto úlohu.
Poté vizualizuje výsledné pole pomocí knihovny Matplotlib, kde každé číslo je reprezentováno odpovídajícím obrázkem načteným ze souboru.

Zde je rozdělení funkcí a jejich vysvětlení:

    valid_number(pole, radek, sloupec):
        Tato funkce přijímá 2D pole, řádek a sloupec, a rozhoduje, které číslo (1 až 6) může být na těchto souřadnicích umístěno.
        Funkce provádí kontrolu okolních prvků a odstraňuje čísla, která by porušila pravidla.
        Návratová hodnota je náhodně vybrané platné číslo z možností.

    main():
        Tato funkce je vstupní bod programu.
        Uživatel je nejprve požádán o zadání šířky a výšky 2D pole.
        Následně je vytvořeno 2D pole a každý prvek je naplněn voláním funkce valid_number.
        Výsledné pole je vypsáno do konzole pro účely debugování.
        Nakonec je vytvořena vizualizace výsledného pole pomocí Matplotlib, kde každé číslo je reprezentováno odpovídajícím obrázkem.

    if name == "main":
        Tato část zajišťuje, že funkce main() bude spuštěna pouze při přímém spuštění tohoto skriptu a ne při jeho importu jako modulu.

Pravidla pro daná čísla:
| Číslo | možné čísla nad ním | možné čísla vlevo od něho |
| 1     |                   5 |                      2, 3 |
| 2	    |             2,3,4,6	|		                4, 5, 6 |
| 3    	|                1, 5 |	                	4, 5, 6	|
|  4    |	               1, 5 |			              1, 2, 3 |
| 5     |	            2,3,4,6 |		              	1, 2, 3 |
|6      |           	2,3,4,6	|	                 	4, 5, 6 |
