from decimal import Decimal

from invoice import Invoice


def test_small_order_gets_no_discount():
    inv = Invoice("Shop").add("Widget", 3, "10.00")
    assert inv.discount == Decimal("0.00")


def test_large_order_gets_five_percent_off_before_vat():
    inv = Invoice("Trade").add("Widget", 20, "10.00")
    assert inv.discount == Decimal("10.00")
    assert inv.vat_total == Decimal("38.00")
    assert inv.total == Decimal("228.00")


def test_exactly_ten_items_gets_the_discount():
    inv = Invoice("Trade").add("Widget", 10, "10.00")
    assert inv.discount == Decimal("5.00")


def test_nine_items_gets_no_discount():
    inv = Invoice("Trade").add("Widget", 9, "10.00")
    assert inv.discount == Decimal("0.00")
