from dataclasses import dataclass
from typing import Any

from ynab_sdk.utils import parsers


@dataclass
class CurrencyFormat:
    iso_code: str
    example_format: str
    decimal_digits: int
    decimal_separator: str
    symbol_first: bool
    group_separator: str
    currency_symbol: str
    display_symbol: bool

    @staticmethod
    def from_dict(obj: Any) -> "CurrencyFormat":
        assert isinstance(obj, dict)
        iso_code = parsers.from_str(obj.get("iso_code"))
        example_format = parsers.from_str(obj.get("example_format"))
        decimal_digits = parsers.from_int(obj.get("decimal_digits"))
        decimal_separator = parsers.from_str(obj.get("decimal_separator"))
        symbol_first = parsers.from_bool(obj.get("symbol_first"))
        group_separator = parsers.from_str(obj.get("group_separator"))
        currency_symbol = parsers.from_str(obj.get("currency_symbol"))
        display_symbol = parsers.from_bool(obj.get("display_symbol"))
        return CurrencyFormat(
            iso_code,
            example_format,
            decimal_digits,
            decimal_separator,
            symbol_first,
            group_separator,
            currency_symbol,
            display_symbol,
        )
