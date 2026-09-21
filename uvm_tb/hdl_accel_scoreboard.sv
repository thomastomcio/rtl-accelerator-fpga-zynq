`include "uvm_macros.svh"
import uvm_pkg::*;

class hdl_accel_scoreboard extends uvm_component;
  `uvm_component_utils(hdl_accel_scoreboard)
  function new(string name = "hdl_accel_scoreboard", uvm_component parent = null);
    super.new(name, parent);
  endfunction
endclass
