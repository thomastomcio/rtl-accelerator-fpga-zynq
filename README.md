# rtl-accelerator-fpga-zynq

Comprehensive RTL accelerator framework for Zynq-7 (Z7-20) featuring:
- Full HDL project parsing (`hdl_parser/`)
- JSON/binary IR generation and serialization
- DPI-C/DMA transfer protocol (`dpi_wrapper/`)
- FPGA RTL execution architecture (`fpga_rtl/`)
- UVM co-simulation scaffold (`uvm_tb/`)
- Zynq PS integration files (`zynq_ps/`)
- Documentation, scripts, and example designs

## Quick parser check

```bash
python -m unittest tests/test_hdl_parser.py
```
