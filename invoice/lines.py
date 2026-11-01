from dataclasses import dataclass
from decimal import Decimal

from .money import to_money

STANDARD_VAT = Decimal("0.20")


@dataclass(frozen=True)
class LineItem:
    description: str
    quantity: int
    unit_price: Decimal

    def __post_init__(self):
        if self.quantity <= 0:
            raise ValueError("quantity must be positive")
        if self.unit_price < 0:
            raise ValueError("unit price cannot be negative")

    @property
    def net(self) -> Decimal:
        return to_money(self.unit_price * self.quantity)

    @property
    def vat(self) -> Decimal:
        return to_money(self.net * STANDARD_VAT)
