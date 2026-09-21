package dpi_hdl_transfer_pkg;
  typedef struct packed {
    bit [31:0] magic;
    bit [15:0] version;
    bit [15:0] flags;
    bit [31:0] module_count;
    bit [31:0] ir_size_bytes;
    bit [31:0] chunk_size;
    bit [31:0] checksum;
  } hdl_transfer_header_t;

  import "DPI-C" function int hdl_dma_start(input chandle header, input chandle payload);
  import "DPI-C" function int hdl_dma_get_status();
endpackage
