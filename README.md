# eparkhontos

Conversion between calendar years (mostly BCE but also CE),
astronomical dates, and the convention used for most ancient Greek
dates, a span of two Julian years (for example, “431/430”).

The name comes from the ancient Greek formula for refering to years as
_ep' arkhontos_ ... (ἐπ᾽ ἄρχοντος ...) “when so-and-so was arkhon.”

## Installation

    pip install eparkhontos
    
## Usage

### Parsing Arkhon Years

`eparkhontos` can parse strings like “431/430”, “431/30”, “431/30
BCE”, “431-430 b.c.”, all of which will return an [“astronomical
year”](https://en.wikipedia.org/wiki/Astronomical_year_numbering)—an
integer which, for years BCE is negative and offset by 1 because 1 BCE
is numbered as 0. The astronomical year is assigned to the year in the
ancient Greek year begins, so "431/430" becomes -430 (meaning 431
BCE):

    >>> import eparkhontos as epi
    >>> epi.parse_arkhon("431/430")
    -430
    >>> epi.parse_arkhon("431/430 B.C.")
    -430
    >>> epi.parse_arkhon("431/430 BCE")
    -430
    >>> epi.parse_arkhon("431-30")
    -430
	
If the string contains any form of “CE” or “AD” the year will be treated accordingly:

    >>> epi.parse_arkhon("100/101 CE")
    100

### Formatting Astronomical Years

You can get a formatted arkhon year from an astronomical year,
including BCE/CE appended if you want, or prepended if you want:

    >>> epi.to_arkhon(-430)
    '431/430'
    >>> epi.to_arkhon(-430, with_era=True)
    '431/430 BCE'
    >>> epi.to_arkhon(-430, with_era=True, prefix_era=True)
    'BCE 431/430'
    >>> epi.to_arkhon(-430, True)
    '431/430 BCE'
    >>> epi.to_arkhon(-430, True, True)
    'BCE 431/430'
    >>> epi.to_arkhon(430, True)
    '430/431  CE'
	
Note that “CE” is padded with leading space to align with “BCE.”
	
### Getting an Astronomical Year

So you don’t have to remember how to correctly offset for an
astronomical year, you can convert an `int` or `str`. For instance, if
you want “431” to be interpreted as “431 BCE”:

    >>> epi.to_astronomical(431)
    -430
    >>> epi.to_astronomical("431")
    -430

If it is, in fact, a year CE:

    >>> epi.to_astronomical("431", is_bce=False)
    431
    >>> epi.to_astronomical("431", False)
    431

## Contributing

Bug reports and pull requests are welcome on GitHub at
https://github.com/seanredmond/eparkhontos

