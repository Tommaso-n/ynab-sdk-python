from dataclasses import dataclass
from typing import Any

from ynab_sdk.utils import parsers


@dataclass
class User:
    id: str

    @staticmethod
    def from_dict(obj: Any) -> "User":
        assert isinstance(obj, dict)
        user_id: str = parsers.from_str(obj.get("id"))
        return User(user_id)


@dataclass
class Data:
    user: User

    @staticmethod
    def from_dict(obj: Any) -> "Data":
        assert isinstance(obj, dict)
        user: User = User.from_dict(obj.get("user"))
        return Data(user)


@dataclass
class UserResponse:
    data: Data

    @staticmethod
    def from_dict(obj: Any) -> "UserResponse":
        assert isinstance(obj, dict)
        user_data: Data = Data.from_dict(obj.get("data"))
        return UserResponse(user_data)
