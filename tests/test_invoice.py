from decimal import Decimal

import pytest

from invoice import Invoice, LineItem
from invoice.money import to_money


def test_to_money_rounds_half_up():
    assert to_money("0.125") == Decimal("0.13")
    assert to_money("0.124") == Decimal("0.12")


def test_line_net_and_vat():
    line = LineItem("Widget", 3, Decimal("9.99"))
    assert line.net == Decimal("29.97")
    assert line.vat == Decimal("5.99")


@pytest.mark.parametrize("qty, price", [(0, "1.00"), (-1, "1.00"), (1, "-0.01")])
def test_line_rejects_bad_input(qty, price):
    with pytest.raises(ValueError):
        LineItem("Bad", qty, Decimal(price))


def test_invoice_totals():
    inv = Invoice("Acme").add("Widget", 2, "10.00").add("Gadget", 1, "5.50")
    assert inv.net_total == Decimal("25.50")
    assert inv.vat_total == Decimal("5.10")
    assert inv.total == Decimal("30.60")


def test_empty_invoice_is_zero():
    inv = Invoice("Nobody")
    assert inv.total == Decimal("0.00")


def test_summary_is_strings():
    summary = Invoice("Acme").add("Widget", 1, "1.00").summary()
    assert summary == {"customer": "Acme", "net": "1.00", "vat": "0.20", "total": "1.20"}
