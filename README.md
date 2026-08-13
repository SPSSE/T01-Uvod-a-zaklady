# Týden 01 – Úvod a základy

## Cíl lekce
- Nainstalovat si Python a VS Code a spustit první program.
- Naučit se pracovat s proměnnými a základními datovými typy (`int`, `float`, `str`, `bool`).
- Umět načíst vstup od uživatele pomocí `input()` a vypsat výstup pomocí `print()` a f-stringů.

## Výklad

### Instalace
1. Stáhni a nainstaluj Python z [python.org](https://www.python.org/downloads/) (při instalaci na Windows zaškrtni "Add python.exe to PATH").
2. Stáhni a nainstaluj [VS Code](https://code.visualstudio.com/) a v něm rozšíření **Python** (od Microsoftu).
3. Ověř instalaci v terminálu:
   ```bash
   python --version
   ```

### První program
```python
print("Ahoj, světe!")
```
Funkce `print()` vypíše text na obrazovku (do konzole).

### Proměnné a datové typy
Proměnná je pojmenované místo v paměti pro uloženou hodnotu. Python typ proměnné pozná sám podle přiřazené hodnoty:

```python
jmeno = "Petra"      # str   - text (v uvozovkách)
vek = 21              # int   - celé číslo
vyska = 172.5         # float - desetinné číslo
je_studentka = True    # bool  - True / False
```

Typ hodnoty zjistíš funkcí `type()`.

### Vstup a výstup
```python
jmeno = input("Jak se jmenuješ? ")   # input() vždy vrací str
vek = int(input("Kolik je ti let? ")) # převod textu na číslo pomocí int()
print(f"Ahoj, {jmeno}, za rok ti bude {vek + 1} let.")
```

f-string (řetězec s předponou `f`) umožňuje vkládat hodnoty proměnných přímo do textu pomocí `{}`.

Podrobné okomentované ukázky najdeš v souborech `priklady/priklad_1.py` a `priklady/priklad_2.py` - projdi si je a zkus si je spustit.

## Cvičení

Doplň funkce v souborech ve složce `cviceni/`:

- **`ukol_1.py` - `pozdrav(jmeno)`**: Vrať pozdrav ve tvaru `"Ahoj, <jmeno>!"`.
  - Příklad: `pozdrav("Petra")` -> `"Ahoj, Petra!"`
- **`ukol_2.py` - `secti(a, b)`**: Vrať součet dvou čísel `a` a `b`.
  - Příklad: `secti(2, 3)` -> `5`
- **`ukol_3.py` - `preved_na_text(cislo)`**: Vrať řetězec ve tvaru `"Hodnota je <cislo>"` pomocí f-stringu.
  - Příklad: `preved_na_text(5)` -> `"Hodnota je 5"`

## Jak si to sám zkontrolovat
```bash
pip install -r requirements.txt
pytest cviceni -v
```
Po nahrání na GitHub navíc automaticky poběží testy přes GitHub Actions – uvidíš zelenou/červenou fajfku u commitu.

## Odevzdání
Vyplň soubory v `cviceni/`, commitni a pushni do svého repozitáře do stanoveného termínu. Řešení (branch `reseni`) zveřejní vyučující až po deadline.
