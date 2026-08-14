def preved_na_text(cislo):
    """
    Vrať řetězec ve tvaru "Hodnota je <cislo>" pomocí f-stringu.

    Příklad:
        preved_na_text(5) -> "Hodnota je 5"
        preved_na_text(3.14) -> "Hodnota je 3.14"

    Pokud cislo není int/float, vyhoď TypeError s výstižnou zprávou.
    """
    if not isinstance(cislo, (int, float)):
        raise TypeError("cislo musí být int nebo float")
    return f"Hodnota je {cislo}"
