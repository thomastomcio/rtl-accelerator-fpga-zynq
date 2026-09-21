module dma_controller(
    input wire        clk,
    input wire        rst_n,
    input wire [31:0] s_axi_wdata,
    input wire        s_axi_we,
    output reg        ir_valid,
    output reg [31:0] ir_word
);
    always @(posedge clk or negedge rst_n) begin
        if (!rst_n) begin
            ir_valid <= 1'b0;
            ir_word <= 32'd0;
        end else begin
            ir_valid <= s_axi_we;
            if (s_axi_we)
                ir_word <= s_axi_wdata;
        end
    end
endmodule
