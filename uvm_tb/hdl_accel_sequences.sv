`include "uvm_macros.svh"
import uvm_pkg::*;
import hdl_accel_pkg::*;

class hdl_load_sequence extends uvm_sequence #(hdl_txn);
  `uvm_object_utils(hdl_load_sequence)
  function new(string name = "hdl_load_sequence");
    super.new(name);
  endfunction

  task body();
    hdl_txn txn;
    txn = hdl_txn::type_id::create("txn");
    start_item(txn);
    assert(txn.randomize());
    finish_item(txn);
  endtask
endclass
