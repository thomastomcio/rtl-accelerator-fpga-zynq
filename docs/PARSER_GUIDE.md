# HDL Parser Guide

## Usage

```python
from hdl_parser import parse_project

ir = parse_project("/abs/path/to/hdl/project")
```

The parser recursively scans `.v/.sv/.vh/.svh`, captures includes/defines,
module hierarchy, ports, parameters, signals, always blocks,
continuous assignments, procedural statements, instances, and generate blocks.
