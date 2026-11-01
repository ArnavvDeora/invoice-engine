from decimal import Decimal

from invoice.money import format_gbp


def test_format_gbp_adds_symbol_and_separators():
    assert format_gbp(Decimal("1234.5")) == "£1,234.50"


def test_format_gbp_small_amounts():
    assert format_gbp("0.5") == "£0.50"
