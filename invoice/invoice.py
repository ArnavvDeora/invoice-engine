from dataclasses import dataclass, field
from decimal import Decimal

from .lines import LineItem
from .money import to_money


@dataclass
class Invoice:
    customer: str
    lines: list = field(default_factory=list)

    def add(self, description: str, quantity: int, unit_price) -> "Invoice":
        self.lines.append(LineItem(description, quantity, Decimal(str(unit_price))))
        return self

    @property
    def net_total(self) -> Decimal:
        return to_money(sum((line.net for line in self.lines), Decimal("0")))

    @property
    def vat_total(self) -> Decimal:
        return to_money(sum((line.vat for line in self.lines), Decimal("0")))

    @property
    def total(self) -> Decimal:
        return self.net_total + self.vat_total

    def summary(self) -> dict:
        return {
            "customer": self.customer,
            "net": str(self.net_total),
            "vat": str(self.vat_total),
            "total": str(self.total),
        }
