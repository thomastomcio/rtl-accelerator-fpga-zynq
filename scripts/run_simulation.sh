#!/usr/bin/env bash
set -euo pipefail
vlog +acc ../uvm_tb/*.sv ../fpga_rtl/*.v ../dpi_wrapper/dpi_hdl_transfer.sv
vsim -c top_tb -do "run -all; quit"
