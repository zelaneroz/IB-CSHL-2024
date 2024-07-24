from q3sample import translate_dna
import pytest

def test_a_to_t():
    assert translate_dna("A") == "T"

def test_non_protein():
    assert translate_dna("Z") == "not valid"

