`include "uvm_macros.svh"
import uvm_pkg::*;
import hdl_accel_pkg::*;

class hdl_accel_agent extends uvm_agent;
  `uvm_component_utils(hdl_accel_agent)
  function new(string name = "hdl_accel_agent", uvm_component parent = null);
    super.new(name, parent);
  endfunction
endclass
