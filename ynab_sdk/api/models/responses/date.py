from dataclasses import dataclass
from typing import Any

from ynab_sdk.utils import parsers


@dataclass
class DateFormat:
    format: str

    @staticmethod
    def from_dict(obj: Any) -> "DateFormat":
        assert isinstance(obj, dict)
        date_format = parsers.from_str(obj.get("format"))
        return DateFormat(date_format)
