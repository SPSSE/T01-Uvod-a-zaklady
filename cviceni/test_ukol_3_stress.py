import pytest
from hypothesis import given, settings, strategies as st

from ukol_3 import preved_na_text


@settings(max_examples=10000, deadline=None)
@given(
    cislo=st.one_of(
        st.integers(),
        st.floats(allow_nan=False, allow_infinity=False),
    )
)
def test_preved_na_text_spravny_vystup(cislo):
    assert preved_na_text(cislo) == f"Hodnota je {cislo}"


@settings(max_examples=10000, deadline=None)
@given(
    neplatna_hodnota=st.one_of(
        st.none(),
        st.text(),
        st.lists(st.integers()),
        st.dictionaries(st.text(), st.integers()),
    )
)
def test_preved_na_text_neplatny_typ_vyhodi_typeerror(neplatna_hodnota):
    with pytest.raises(TypeError):
        preved_na_text(neplatna_hodnota)
