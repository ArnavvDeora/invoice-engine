"""Money helpers. Every amount is a Decimal in pounds."""
from decimal import ROUND_HALF_UP, Decimal

PENNY = Decimal("0.01")


def to_money(value) -> Decimal:
    """Round to the penny, half-up: the convention HMRC uses for VAT."""
    return Decimal(str(value)).quantize(PENNY, rounding=ROUND_HALF_UP)
