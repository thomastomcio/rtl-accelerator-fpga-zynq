create_project rtl_accel_z7 ./build -part xc7z020clg400-1
add_files ../fpga_rtl/top_accel.v
add_files ../fpga_rtl/dma_controller.v
add_files ../fpga_rtl/ir_interpreter.v
add_files ../fpga_rtl/execution_fsm.v
add_files ../fpga_rtl/signal_register_bank.v
add_files -fileset constrs_1 ../fpga_rtl/constraints.xdc
update_compile_order -fileset sources_1
launch_runs impl_1 -to_step write_bitstream
wait_on_run impl_1
