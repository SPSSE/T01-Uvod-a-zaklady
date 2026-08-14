def pozdrav(jmeno):
    """
    Vrať pozdrav ve tvaru "Ahoj, <jmeno>!".

    Příklad:
        pozdrav("Petra") -> "Ahoj, Petra!"

    Pokud jmeno není str, vyhoď TypeError s výstižnou zprávou.
    """
    return f"Ahoj, {jmeno}!"
