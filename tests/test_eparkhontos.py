# Eparkhontos, ancient Greek arkhon year formatting/parsing
# Copyright (C) 2023 Sean Redmond

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

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
