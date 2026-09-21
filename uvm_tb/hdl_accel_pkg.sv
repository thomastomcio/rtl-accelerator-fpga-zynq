package hdl_accel_pkg;
  import uvm_pkg::*;
  `include "uvm_macros.svh"

  class hdl_txn extends uvm_sequence_item;
    rand bit [31:0] word;
    `uvm_object_utils(hdl_txn)
    function new(string name = "hdl_txn");
      super.new(name);
    endfunction
  endclass
endpackage
