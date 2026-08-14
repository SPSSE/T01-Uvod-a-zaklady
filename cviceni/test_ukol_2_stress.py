import pytest
from hypothesis import given, settings, strategies as st

from ukol_2 import secti

cisla = st.one_of(
    st.integers(),
    st.floats(allow_nan=False, allow_infinity=False),
)


@settings(max_examples=10000, deadline=None)
@given(a=cisla, b=cisla)
def test_secti_spravny_soucet(a, b):
    assert secti(a, b) == a + b


@settings(max_examples=10000, deadline=None)
@given(a=cisla, b=cisla)
def test_secti_je_komutativni(a, b):
    assert secti(a, b) == secti(b, a)


@settings(max_examples=10000, deadline=None)
@given(
    a=st.one_of(
        st.none(),
        st.text(),
        st.lists(st.integers()),
        st.dictionaries(st.text(), st.integers()),
    ),
    b=cisla,
)
def test_secti_neplatny_typ_a_vyhodi_typeerror(a, b):
    with pytest.raises(TypeError):
        secti(a, b)


@settings(max_examples=10000, deadline=None)
@given(
    a=cisla,
    b=st.one_of(
        st.none(),
        st.text(),
        st.lists(st.integers()),
        st.dictionaries(st.text(), st.integers()),
    ),
)
def test_secti_neplatny_typ_b_vyhodi_typeerror(a, b):
    with pytest.raises(TypeError):
        secti(a, b)
