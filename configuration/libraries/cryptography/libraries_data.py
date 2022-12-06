from typing import List
from enum import Enum
from pydantic.dataclasses import dataclass

class Category(Enum):
    HASH = 1
    MAC = 2
    KEY_EXCHANGE = 3
    SIGNATURE = 4
    ENCRYPTION = 5


@dataclass
class CryptoUsage:
    word: str
    category: Category
    algorithms: List[str]
    params: List[object]


@dataclass
class Key:
    name: str
    length: int

encrypt_libraries = {
    "python": {
        " cryptography":["CryptoUsage"]
    }
}

