def pozdrav(jmeno):
    """
    Vrať pozdrav ve tvaru "Ahoj, <jmeno>!".

    Příklad:
        pozdrav("Petra") -> "Ahoj, Petra!"

    Pokud jmeno není str, vyhoď TypeError s výstižnou zprávou.
    """
    if not isinstance(jmeno, str):
        raise TypeError("jmeno musí být str")
    return f"Ahoj, {jmeno}!"
