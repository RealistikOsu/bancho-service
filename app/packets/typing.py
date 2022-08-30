from __future__ import annotations

from typing import Protocol
from typing import Optional
from typing import Union

class PacketHandler(Protocol):
    def __call__(self, *args: ALL_TYPES) -> Optional[bytes]:
        ...

class u8(int):
    pass

class u16(int):
    pass

class u32(int):
    pass

class u64(int):
    pass

class i16(int):
    pass

class i32(int):
    pass

class i64(int):
    pass

ALL_TYPES = Union[
    u8,
    u16,
    u32,
    u64,
    i16,
    i32,
    i64,
    str,
    float,
]
