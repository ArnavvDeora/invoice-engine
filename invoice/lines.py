from dataclasses import dataclass
from decimal import Decimal

from .money import to_money

STANDARD_VAT = Decimal("0.20")
ZERO_RATED = Decimal("0")


@dataclass(frozen=True)
class LineItem:
    description: str
    quantity: int
    unit_price: Decimal
    vat_rate: Decimal = STANDARD_VAT

    def __post_init__(self):
        if self.quantity <= 0:
            raise ValueError("quantity must be positive")
        if self.unit_price < 0:
            raise ValueError("unit price cannot be negative")
        if not ZERO_RATED <= self.vat_rate < 1:
            raise ValueError("VAT rate must be between 0 and 1")

    @property
    def net(self) -> Decimal:
        return to_money(self.unit_price * self.quantity)

    @property
    def vat(self) -> Decimal:
        return to_money(self.net * self.vat_rate)
