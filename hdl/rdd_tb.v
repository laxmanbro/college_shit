

module rd_test;

    reg clk, reset;
    reg [7:0] x, y;
    wire [7:0] Q, A;
    reg start; 
    wire done_tick;
    wire tx_full1, rx_empty1, tx_full2, rx_empty2;

    localparam c_CLOCK_PERIOD_NS=20; 
    initial begin clk=0; reset=0; forever #c_CLOCK_PERIOD_NS clk=~clk; end
    
    rdd rd1 (.quotient(Q), .remainder(A), .done(done_tick), .x(x), .y(y), .clk(clk), .reset(reset), .start(start),.t(t));
    initial begin 
        #80;
        reset = 1'b1;
        #200;
        reset = 1'b0;
        #200; //wait for 5 clks
        {x, y, start,t} = {8'b00001000, 8'b00001101, 1'b1,8};
        @(posedge clk) start = 1'b1; //generate only a pulse
        @(posedge clk) start = 1'b0; //generate only a pulse
        #100000;

        //above can be put in a loop to transmit more data.
        $finish;
    end
    initial begin
        $dumpfile("a.vcd");
        $dumpvars;
    end
endmodule
