module aavs2_test;

	localparam width1 = 4;
        reg [width1 - 1:0] x,u ;
	reg y,v;
	wire [width1 - 1:0] z;
	reg clk,reset;
	wire cout;
	aavs2 a1(z,cout,x,u,y,v);

	initial begin
		clk = 0;
		reset <= 0 ;
	end
	always #10 clk = ~clk;

	initial begin

		x=2;y=1;v=1;u=2;
		#20 x=2;y=1;v=1;u=1 ;
                #20 x=1;y=0;v=0;u=1;
		#20 x=2;y=0;v=1;u=6;
		#100 $finish;

	end

	initial begin
		$dumpfile("a.vcd");
		$dumpvars;
		$monitor(" At time %t, %0d, %0d, %0d, %0d, %0d, %0d ",$time, z,cout,x,y,u,v);
	end
endmodule
