def secti(a, b):
    """
    Vrať součet čísel a a b.

    Příklad:
        secti(2, 3) -> 5
        secti(2.5, 1.5) -> 4.0

    Pokud a nebo b není int/float, vyhoď TypeError s výstižnou zprávou.
    """
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("a i b musí být int nebo float")
    return a + b
