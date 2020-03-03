module non_res_test;

    reg clk, reset;
    reg [15:0] x, y;
    wire [15:0] q, r;
    reg start; 
    wire done_tick;
    wire tx_full1, rx_empty1, tx_full2, rx_empty2;

    localparam c_CLOCK_PERIOD_NS=20; 
    initial begin clk=0; reset=0; forever #c_CLOCK_PERIOD_NS clk=~clk; end
    
    non_rest rest(.QUOTIENT(q), .REMAINDER(r), .done(done_tick), .x(x), .y(y), .clk(clk), .reset(reset), .start(start));
    initial begin 
        #80;
        reset = 1'b1; 
        #200;
        reset = 1'b0;
        #80; 
        {x, y} = {16'b0000000000000011, 16'b0000000000001000};  
        @(posedge clk) start = 1'b1; 
	#20;
        @(posedge clk) start = 1'b0;
        #600;
        $finish;
    end
initial begin
			if(x>y) $monitor("At time = %t,Q = %b, R = %b", $time, q, r);
			else $monitor("At time = %t,Q = %b, R = %b", $time, r, q);
			end

    initial begin
        $dumpfile("a.vcd");
        $dumpvars;
    end

endmodule
