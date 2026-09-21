from __future__ import annotations

import re
from pathlib import Path
from typing import Dict, Iterable, List

from .ast import (
    AlwaysBlock,
    ContinuousAssign,
    GenerateBlock,
    Instance,
    Module,
    Parameter,
    Port,
    ProceduralStatement,
    ProjectAST,
    Signal,
)

HDL_EXTENSIONS = {".v", ".sv", ".vh", ".svh"}


class HDLParser:
    def __init__(self, project_root: str):
        self.project_root = Path(project_root).resolve()

    def scan_project(self) -> List[Path]:
        return sorted(
            p
            for p in self.project_root.rglob("*")
            if p.is_file() and p.suffix.lower() in HDL_EXTENSIONS
        )

    def parse_project(self) -> ProjectAST:
        ast = ProjectAST(root=str(self.project_root))
        for file_path in self.scan_project():
            content = file_path.read_text(encoding="utf-8", errors="ignore")
            self._parse_directives(content, ast)
            for module in self._parse_modules(content, file_path):
                ast.modules[module.name] = module
        return ast

    def _parse_directives(self, content: str, ast: ProjectAST) -> None:
        for inc in re.findall(r"`include\s+\"([^\"]+)\"", content):
            if inc not in ast.includes:
                ast.includes.append(inc)
        for name, value in re.findall(r"`define\s+(\w+)\s*(.*)", content):
            ast.defines[name] = value.strip() or "1"

    def _parse_modules(self, content: str, file_path: Path) -> Iterable[Module]:
        module_pattern = re.compile(
            r"module\s+(\w+)\s*(#\s*\((.*?)\))?\s*\((.*?)\);(.*?)endmodule",
            re.S,
        )
        for mod_name, _, params_raw, ports_raw, body in module_pattern.findall(content):
            module = Module(name=mod_name, file_path=str(file_path))
            module.parameters.extend(self._parse_parameters(params_raw))
            module.ports.extend(self._parse_ports(ports_raw))
            module.signals.extend(self._parse_signals(body))
            module.always_blocks.extend(self._parse_always(body))
            module.continuous_assignments.extend(self._parse_assigns(body))
            module.procedural_statements.extend(self._parse_procedural(body))
            module.instances.extend(self._parse_instances(body))
            module.generate_blocks.extend(self._parse_generate(body))
            yield module

    def _parse_parameters(self, text: str) -> List[Parameter]:
        out: List[Parameter] = []
        for name, value in re.findall(r"parameter\s+(\w+)\s*=\s*([^,\n\)]+)", text or ""):
            out.append(Parameter(name=name, value=value.strip()))
        return out

    def _parse_ports(self, text: str) -> List[Port]:
        out: List[Port] = []
        tokens = [t.strip() for t in (text or "").split(",") if t.strip()]
        for token in tokens:
            m = re.match(r"(input|output|inout)\s+(?:reg|wire|logic\s+)?(\[[^\]]+\])?\s*(\w+)", token)
            if not m:
                continue
            direction, width, name = m.groups()
            out.append(Port(name=name, direction=direction, width=(width or "1")))
        return out

    def _parse_signals(self, body: str) -> List[Signal]:
        out: List[Signal] = []
        for kind, width, name, init in re.findall(
            r"\b(wire|reg|logic)\s*(\[[^\]]+\])?\s*(\w+)\s*(?:=\s*([^;]+))?;",
            body,
        ):
            out.append(Signal(name=name, kind=kind, width=width or "1", initial=(init or "").strip() or None))
        return out

    def _parse_always(self, body: str) -> List[AlwaysBlock]:
        out: List[AlwaysBlock] = []
        pattern = re.compile(r"always(?:_ff|_comb|_latch)?\s*@?\s*(\([^\)]*\))?\s*(begin.*?end)", re.S)
        for sensitivity, blk in pattern.findall(body):
            sens = (sensitivity or "(*)").strip()
            kind = "sequential" if re.search(r"posedge|negedge", sens) else "combinatorial"
            out.append(AlwaysBlock(sensitivity=sens, body=blk.strip(), kind=kind))
        return out

    def _parse_assigns(self, body: str) -> List[ContinuousAssign]:
        return [
            ContinuousAssign(lhs=lhs.strip(), rhs=rhs.strip())
            for lhs, rhs in re.findall(r"\bassign\s+([^=;]+)=\s*([^;]+);", body)
        ]

    def _parse_procedural(self, body: str) -> List[ProceduralStatement]:
        out: List[ProceduralStatement] = []
        for stmt in re.findall(r"\b(if\s*\(.*?\)\s*.*?;|case\s*\(.*?\).*?endcase)", body, re.S):
            out.append(ProceduralStatement(text=" ".join(stmt.split())))
        return out

    def _parse_instances(self, body: str) -> List[Instance]:
        out: List[Instance] = []
        for mod, inst in re.findall(r"\b(\w+)\s+(\w+)\s*\([^;]*\);", body):
            if mod in {"if", "for", "while", "case", "assign", "always"}:
                continue
            out.append(Instance(module=mod, name=inst))
        return out

    def _parse_generate(self, body: str) -> List[GenerateBlock]:
        return [GenerateBlock(text=" ".join(g.split())) for g in re.findall(r"generate(.*?)endgenerate", body, re.S)]


def parse_project(project_root: str) -> Dict:
    parser = HDLParser(project_root)
    ast = parser.parse_project()
    from .ir_generator import IRGenerator

    return IRGenerator().generate(ast)
