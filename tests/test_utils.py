import pytest

from main import convert_date, masking_card


def test_convert_date():
    assert convert_date("2019-04-04T23:20:05.206878") == "04.04.2019"
    assert convert_date("2019-03-23T01:09:46.296404") == "23.03.2019"


def test_masking_card():
    assert masking_card("Счет 44812258784861134719") == "Счет  ** 4719"
    assert masking_card("Visa Platinum 8990922113665229") == "Visa Platinum 899092 ** 5229"
