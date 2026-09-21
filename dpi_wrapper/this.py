from __future__ import annotations

import argparse
import struct
from dataclasses import dataclass
from pathlib import Path

from hdl_parser.serializer import to_binary

MAGIC = 0x48444C49
VERSION = 0x0001
DESIGN_NAME_MAX = 64


@dataclass
class TransferPacket:
    design_name: str
    module_count: int
    payload: bytes

    def pack(self) -> bytes:
        name = self.design_name.encode("utf-8")[: DESIGN_NAME_MAX - 1]
        name = name + b"\x00" * (DESIGN_NAME_MAX - len(name))
        checksum = checksum32(self.payload)
        header = struct.pack(
            "<IHH64sIIII",
            MAGIC,
            VERSION,
            0,
            name,
            self.module_count,
            len(self.payload),
            4096,
            checksum,
        )
        return header + self.payload


def checksum32(payload: bytes) -> int:
    value = 0
    for b in payload:
        value = ((value << 5) - value + b) & 0xFFFFFFFF
    return value


def build_packet(design_name: str, ir: dict) -> bytes:
    payload = to_binary(ir)
    module_count = len(ir.get("modules", {}))
    return TransferPacket(design_name=design_name, module_count=module_count, payload=payload).pack()


def main() -> None:
    parser = argparse.ArgumentParser(description="Build binary packet for HDL IR DMA transfer")
    parser.add_argument("design_name")
    parser.add_argument("ir_json")
    parser.add_argument("output")
    args = parser.parse_args()

    import json

    ir = json.loads(Path(args.ir_json).read_text(encoding="utf-8"))
    blob = build_packet(args.design_name, ir)
    Path(args.output).write_bytes(blob)


if __name__ == "__main__":
    main()
