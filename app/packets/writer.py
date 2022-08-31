from __future__ import annotations

import struct
from typing import Optional


class WritableBuffer:
    __slots__ = ("_buffer",)

    def __init__(self, buffer: Optional[bytearray] = None) -> None:
        self._buffer = buffer or bytearray()

    def write_u8(self, val: int) -> None:
        self._buffer.append(val)

    def write_u16(self, val: int) -> None:
        self._buffer += val.to_bytes(
            length=2,
            byteorder="little",
            signed=False,
        )

    def write_u32(self, val: int) -> None:
        self._buffer += val.to_bytes(
            length=4,
            byteorder="little",
            signed=False,
        )

    def write_u64(self, val: int) -> None:
        self._buffer += val.to_bytes(
            length=8,
            byteorder="little",
            signed=False,
        )

    def write_i16(self, val: int) -> None:
        self._buffer += val.to_bytes(
            length=2,
            byteorder="little",
            signed=True,
        )

    def write_i32(self, val: int) -> None:
        self._buffer += val.to_bytes(
            length=4,
            byteorder="little",
            signed=True,
        )

    def write_i64(self, val: int) -> None:
        self._buffer += val.to_bytes(
            length=8,
            byteorder="little",
            signed=True,
        )

    def write_f32(self, val: float) -> None:
        self._buffer += struct.pack("<f", val)
