from decimal import Decimal

from .money import to_money

BULK_THRESHOLD = 10
BULK_RATE = Decimal("0.05")


def bulk_discount(item_count: int, net_total: Decimal) -> Decimal:
    if item_count >= BULK_THRESHOLD:
        return to_money(net_total * BULK_RATE)
    return Decimal("0.00")
