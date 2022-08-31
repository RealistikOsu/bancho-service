from __future__ import annotations

import struct


class ReadableBuffer:
    __slots__ = ("_buffer",)

    def __init__(self, buffer: bytearray) -> None:
        self._buffer = buffer

    def _select(self, n: int) -> bytearray:
        res = self._buffer[:n]
        self._buffer = self._buffer[n:]
        return res

    def read_u8(self) -> int:
        return self._select(1)[0]

    def read_u16(self) -> int:
        return int.from_bytes(
            self._select(2),
            "little",
            signed=False,
        )

    def read_u32(self) -> int:
        return int.from_bytes(
            self._select(4),
            "little",
            signed=False,
        )

    def read_u64(self) -> int:
        return int.from_bytes(
            self._select(8),
            "little",
            signed=False,
        )

    def read_i16(self) -> int:
        return int.from_bytes(
            self._select(2),
            "little",
            signed=True,
        )

    def read_i32(self) -> int:
        return int.from_bytes(
            self._select(4),
            "little",
            signed=True,
        )

    def read_i64(self) -> int:
        return int.from_bytes(
            self._select(8),
            "little",
            signed=True,
        )

    def read_f32(self) -> float:
        return struct.unpack(
            "<f",
            self._select(4),
        )[0]

    def read_raw(self, n: int) -> bytearray:
        """Reads `n` number of bytes straight from the buffer."""

        return self._select(n)

    def read_i32_array(self) -> list[int]:
        """Reads a u16 prefixed array of i32s."""

        length = self.read_u16()

        return [self.read_i32() for _ in range(length)]

    def read_uleb128(self) -> int:
        value = 0
        shift = 0

        while True:
            b = self._select(1)[0]
            value |= (b & 0b1111111) << shift

            if b & (1 << 7) == 0:
                return value

            shift += 7

    def read_osu_string(self) -> str:
        """Reads an osu string, defined as a string of utf-8 bytes first prefixed
        by an exists byte (0xb if exists, else 0x0) and then an ULEB128 of the
        string's length."""

        exists = self._select(1)[0] == 0xB

        if not exists:
            return ""

        length = self.read_uleb128()
        string_bytes = self._select(length)
        return string_bytes.decode("utf-8")
