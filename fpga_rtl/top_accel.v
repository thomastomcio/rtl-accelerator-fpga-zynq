module top_accel(
    input wire        clk,
    input wire        rst_n,
    input wire [31:0] s_axi_ctrl_wdata,
    input wire        s_axi_ctrl_we,
    output wire [31:0] signal_read_data
);
    wire ir_valid;
    wire [31:0] ir_word;
    wire exec_step;

    dma_controller u_dma (
        .clk(clk),
        .rst_n(rst_n),
        .s_axi_wdata(s_axi_ctrl_wdata),
        .s_axi_we(s_axi_ctrl_we),
        .ir_valid(ir_valid),
        .ir_word(ir_word)
    );

    ir_interpreter u_interp (
        .clk(clk),
        .rst_n(rst_n),
        .ir_valid(ir_valid),
        .ir_word(ir_word),
        .exec_step(exec_step)
    );

    execution_fsm u_exec (
        .clk(clk),
        .rst_n(rst_n),
        .step(exec_step)
    );

    signal_register_bank u_sig (
        .clk(clk),
        .rst_n(rst_n),
        .write_enable(exec_step),
        .write_data(ir_word),
        .read_data(signal_read_data)
    );
endmodule
