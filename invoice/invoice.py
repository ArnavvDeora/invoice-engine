from dataclasses import dataclass, field
from decimal import Decimal

from .discounts import bulk_discount
from .lines import STANDARD_VAT, LineItem
from .money import to_money


@dataclass
class Invoice:
    customer: str
    lines: list = field(default_factory=list)

    def add(self, description: str, quantity: int, unit_price) -> "Invoice":
        self.lines.append(LineItem(description, quantity, Decimal(str(unit_price))))
        return self

    @property
    def item_count(self) -> int:
        return sum(line.quantity for line in self.lines)

    @property
    def net_total(self) -> Decimal:
        return to_money(sum((line.net for line in self.lines), Decimal("0")))

    @property
    def discount(self) -> Decimal:
        return bulk_discount(self.item_count, self.net_total)

    @property
    def vat_total(self) -> Decimal:
        return to_money((self.net_total - self.discount) * STANDARD_VAT)

    @property
    def total(self) -> Decimal:
        return self.net_total - self.discount + self.vat_total

    def summary(self) -> dict:
        return {
            "customer": self.customer,
            "net": str(self.net_total),
            "discount": str(self.discount),
            "vat": str(self.vat_total),
            "total": str(self.total),
        }
