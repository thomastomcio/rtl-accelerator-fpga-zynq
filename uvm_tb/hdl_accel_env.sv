`include "uvm_macros.svh"
import uvm_pkg::*;
import hdl_accel_pkg::*;

class hdl_accel_env extends uvm_env;
  `uvm_component_utils(hdl_accel_env)
  function new(string name = "hdl_accel_env", uvm_component parent = null);
    super.new(name, parent);
  endfunction
endclass
