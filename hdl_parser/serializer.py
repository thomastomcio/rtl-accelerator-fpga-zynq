from __future__ import annotations

import json
import zlib
from pathlib import Path
from typing import Any, Dict


def to_json(ir: Dict[str, Any], pretty: bool = True) -> str:
    return json.dumps(ir, indent=2 if pretty else None, sort_keys=True)


def from_json(payload: str) -> Dict[str, Any]:
    return json.loads(payload)


def to_binary(ir: Dict[str, Any]) -> bytes:
    return zlib.compress(to_json(ir, pretty=False).encode("utf-8"), level=9)


def from_binary(blob: bytes) -> Dict[str, Any]:
    return from_json(zlib.decompress(blob).decode("utf-8"))


def save_ir(ir: Dict[str, Any], out_path: str, binary: bool = False) -> None:
    path = Path(out_path)
    path.parent.mkdir(parents=True, exist_ok=True)
    if binary:
        path.write_bytes(to_binary(ir))
        return
    path.write_text(to_json(ir), encoding="utf-8")


def load_ir(path: str) -> Dict[str, Any]:
    p = Path(path)
    if p.suffix == ".bin":
        return from_binary(p.read_bytes())
    return from_json(p.read_text(encoding="utf-8"))
