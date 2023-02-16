import pytest
import eparkhontos as epi


def test_version():
    assert epi.version() == "0.0.1"


def test_to_arkhon():
    assert epi.to_arkhon(-430) == "431/430"
    assert epi.to_arkhon(-430, True) == "431/430 BCE"
    assert epi.to_arkhon(-430, True, True) == "BCE 431/430"
    assert epi.to_arkhon(-430, False, True) == "431/430"

    assert epi.to_arkhon(430) == "430/431"
    assert epi.to_arkhon(430, True) == "430/431  CE"
    assert epi.to_arkhon(430, True, True) == " CE 430/431"
    assert epi.to_arkhon(430, False, True) == "430/431"


def test_to_astronomical():
    assert epi.to_astronomical(431) == -430
    assert epi.to_astronomical(431, False) == 431


def test_to_astronomical_strings():
    assert epi.to_astronomical("431") == -430
    assert epi.to_astronomical("431", False) == 431

    with pytest.raises(epi.UnparseableDateError, match="arkhon year"):
        epi.to_astronomical("431/430")

    with pytest.raises(
        epi.UnparseableDateError, match=r"Could not convert date 'ZZZ'$"
    ):
        epi.to_astronomical("ZZZ")


def test_parse_arkhon():
    assert epi.parse_arkhon("431/430") == -430
    assert epi.parse_arkhon("431/430 BC") == -430
    assert epi.parse_arkhon("431/430 BCE") == -430
    assert epi.parse_arkhon("431/430 B.C.") == -430
    assert epi.parse_arkhon("431/430 b.c.") == -430

    assert epi.parse_arkhon("431/432 CE") == 431
    assert epi.parse_arkhon("431/432 C.E.") == 431
    assert epi.parse_arkhon("431/432 AD") == 431
    assert epi.parse_arkhon("431/432 a.d.") == 431

    with pytest.raises(epi.UnparseableDateError):
        epi.parse_arkhon("Not a date")
    
    
    
