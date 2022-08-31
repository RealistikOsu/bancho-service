from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime


@dataclass
class User:
    id: int
    name: str
    safe_name: str
    privileges: int
    supporter_end: int
