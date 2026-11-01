"""Money helpers. Every amount is a Decimal in pounds."""
from decimal import ROUND_HALF_EVEN, Decimal

PENNY = Decimal("0.01")


def to_money(value) -> Decimal:
    """Round to the penny (banker's rounding, the IEEE default)."""
    return Decimal(str(value)).quantize(PENNY, rounding=ROUND_HALF_EVEN)


def format_gbp(amount) -> str:
    """£1,234.50 style, for the PDF renderer."""
    return f"£{to_money(amount):,.2f}"
