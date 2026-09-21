module signal_register_bank(
    input wire        clk,
    input wire        rst_n,
    input wire        write_enable,
    input wire [31:0] write_data,
    output reg [31:0] read_data
);
    reg [31:0] signal_mem [0:255];
    reg [7:0] write_ptr;

    always @(posedge clk or negedge rst_n) begin
        if (!rst_n) begin
            write_ptr <= 8'd0;
            read_data <= 32'd0;
        end else if (write_enable) begin
            signal_mem[write_ptr] <= write_data;
            read_data <= write_data;
            write_ptr <= write_ptr + 1'b1;
        end
    end
endmodule
