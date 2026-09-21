from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict, List, Optional


@dataclass
class Port:
    name: str
    direction: str
    width: str = "1"


@dataclass
class Signal:
    name: str
    kind: str
    width: str = "1"
    initial: Optional[str] = None


@dataclass
class Parameter:
    name: str
    value: str


@dataclass
class AlwaysBlock:
    sensitivity: str
    body: str
    kind: str


@dataclass
class ContinuousAssign:
    lhs: str
    rhs: str


@dataclass
class ProceduralStatement:
    text: str


@dataclass
class Instance:
    module: str
    name: str


@dataclass
class GenerateBlock:
    text: str


@dataclass
class Module:
    name: str
    file_path: str
    ports: List[Port] = field(default_factory=list)
    parameters: List[Parameter] = field(default_factory=list)
    signals: List[Signal] = field(default_factory=list)
    always_blocks: List[AlwaysBlock] = field(default_factory=list)
    continuous_assignments: List[ContinuousAssign] = field(default_factory=list)
    procedural_statements: List[ProceduralStatement] = field(default_factory=list)
    instances: List[Instance] = field(default_factory=list)
    generate_blocks: List[GenerateBlock] = field(default_factory=list)


@dataclass
class ProjectAST:
    root: str
    modules: Dict[str, Module] = field(default_factory=dict)
    includes: List[str] = field(default_factory=list)
    defines: Dict[str, str] = field(default_factory=dict)
