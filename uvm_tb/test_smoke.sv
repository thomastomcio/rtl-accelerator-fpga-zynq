`include "uvm_macros.svh"
import uvm_pkg::*;
import hdl_accel_pkg::*;

class test_smoke extends uvm_test;
  `uvm_component_utils(test_smoke)
  function new(string name = "test_smoke", uvm_component parent = null);
    super.new(name, parent);
  endfunction

  task run_phase(uvm_phase phase);
    phase.raise_objection(this);
    #10ns;
    phase.drop_objection(this);
  endtask
endclass
