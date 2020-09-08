from dataclasses import dataclass
from typing import Any

from ynab_sdk.utils import parsers


@dataclass
class ErrorDetail:
    id: str
    name: str
    detail: str

    @staticmethod
    def from_dict(obj: Any) -> "ErrorDetail":
        assert isinstance(obj, dict)
        error_id = parsers.from_str(obj.get("id"))
        error_name = parsers.from_str(obj.get("name"))
        error_detail = parsers.from_str(obj.get("detail"))
        return ErrorDetail(error_id, error_name, error_detail)


@dataclass
class ErrorResponse:
    error: ErrorDetail

    @staticmethod
    def from_dict(obj: Any) -> "ErrorResponse":
        assert isinstance(obj, dict)
        error = ErrorDetail.from_dict(obj.get("error"))
        return ErrorResponse(error)
