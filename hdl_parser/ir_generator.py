from __future__ import annotations

from collections import defaultdict
from typing import Dict, List

from .ast import Module, ProjectAST


class IRGenerator:
    def generate(self, project_ast: ProjectAST) -> Dict:
        hierarchy = self._build_hierarchy(list(project_ast.modules.values()))
        modules = {name: self._module_to_dict(module) for name, module in project_ast.modules.items()}
        return {
            "version": "1.0",
            "project_root": project_ast.root,
            "includes": project_ast.includes,
            "defines": project_ast.defines,
            "module_hierarchy": hierarchy,
            "modules": modules,
        }

    def _build_hierarchy(self, modules: List[Module]) -> Dict[str, List[str]]:
        tree = defaultdict(list)
        names = {m.name for m in modules}
        for module in modules:
            for inst in module.instances:
                if inst.module in names:
                    tree[module.name].append(inst.module)
        return dict(tree)

    def _module_to_dict(self, module: Module) -> Dict:
        return {
            "file_path": module.file_path,
            "ports": [vars(p) for p in module.ports],
            "parameters": [vars(p) for p in module.parameters],
            "signals": [vars(s) for s in module.signals],
            "always_blocks": [vars(a) for a in module.always_blocks],
            "continuous_assignments": [vars(a) for a in module.continuous_assignments],
            "procedural_statements": [vars(s) for s in module.procedural_statements],
            "instances": [vars(i) for i in module.instances],
            "generate_blocks": [vars(g) for g in module.generate_blocks],
        }
