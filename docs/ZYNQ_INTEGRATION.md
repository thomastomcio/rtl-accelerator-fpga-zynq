# Zynq-7 Integration

- Vivado automation: `zynq_ps/vivado_build.tcl`
- Bare-metal access: `zynq_ps/arm_driver.c`
- AXI register map: `zynq_ps/axi_registers.h`

Control path uses AXI Lite for start/status and readback.
