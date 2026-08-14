import pytest
from hypothesis import given, settings, strategies as st

from ukol_1 import pozdrav


@settings(max_examples=10000, deadline=None)
@given(jmeno=st.text())
def test_pozdrav_spravny_vystup(jmeno):
    assert pozdrav(jmeno) == f"Ahoj, {jmeno}!"


@settings(max_examples=10000, deadline=None)
@given(
    neplatna_hodnota=st.one_of(
        st.none(),
        st.integers(),
        st.floats(allow_nan=False, allow_infinity=False),
        st.booleans(),
        st.lists(st.integers()),
        st.dictionaries(st.text(), st.integers()),
    )
)
def test_pozdrav_neplatny_typ_vyhodi_typeerror(neplatna_hodnota):
    with pytest.raises(TypeError):
        pozdrav(neplatna_hodnota)
