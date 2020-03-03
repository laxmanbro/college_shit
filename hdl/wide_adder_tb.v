module test;

    reg clk, reset;
    reg [15:0] a, b;
    wire [15:0] sum;
    reg cin; 
    wire cout;

    localparam c_CLOCK_PERIOD_NS=20; 
    initial begin clk=0; reset=0; forever #c_CLOCK_PERIOD_NS clk=~clk; end
    
    adder_16bit add1(.sum(sum), .cout(cout), .a(a), .b(b), .cin(cin), .clk(clk), .reset(reset));
    initial begin 
        #80;
        reset = 1'b1;
        #200;
        reset = 1'b0;
        #200; //wait for 5 clks
        {a, b, cin} = {16'b0000100000001000, 16'b0000110100001101, 1'b1};
        @(posedge clk) cin = 1'b1; //generate only a pulse
        @(posedge clk) cin = 1'b0; //generate only a pulse
        #100000;

        //above can be put in a loop to transmit more data.
        $finish;
    end
    initial begin
        $dumpfile("a.vcd");
        $dumpvars;
    end
endmodule
