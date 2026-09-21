module execution_fsm(
    input wire clk,
    input wire rst_n,
    input wire step
);
    localparam IDLE = 2'd0;
    localparam EVAL_COMB = 2'd1;
    localparam EVAL_SEQ = 2'd2;

    reg [1:0] state;

    always @(posedge clk or negedge rst_n) begin
        if (!rst_n)
            state <= IDLE;
        else begin
            case (state)
                IDLE: if (step) state <= EVAL_COMB;
                EVAL_COMB: state <= EVAL_SEQ;
                EVAL_SEQ: state <= IDLE;
                default: state <= IDLE;
            endcase
        end
    end
endmodule
