# RTL Accelerator Architecture

This project provides a Zynq-7 RTL acceleration flow with:
- HDL project parsing to a JSON/binary IR
- DPI-based packet transfer protocol for DMA streaming
- FPGA execution skeleton with interpreter and signal register bank
- UVM co-simulation scaffolding
- Zynq PS build/deployment stubs

Signal flow:
1. `hdl_parser` scans full project trees and emits IR.
2. `dpi_wrapper/this.py` packages IR to a transfer packet.
3. DPI-C sends packet words into the FPGA DMA controller.
4. FPGA interpreter/execution FSM updates signal register bank.
5. UVM testbench drives packets and checks observed values.
