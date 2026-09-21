module ir_interpreter(
    input wire clk,
    input wire rst_n,
    input wire ir_valid,
    input wire [31:0] ir_word,
    output reg exec_step
);
    reg [31:0] opcode;

    always @(posedge clk or negedge rst_n) begin
        if (!rst_n) begin
            exec_step <= 1'b0;
            opcode <= 32'd0;
        end else begin
            exec_step <= ir_valid;
            if (ir_valid)
                opcode <= ir_word;
        end
    end
endmodule
