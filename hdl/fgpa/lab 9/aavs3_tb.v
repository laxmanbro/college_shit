module aavs_test;
   
	localparam width1 = 4;
        localparam width2 = 3;
	localparam width3 = 6;
	reg [width1 - 1:0] x,u ;
	reg [width2 - 1:0] y,v ;
	wire [width3 - 1:0] z;
	reg clk,reset;
	wire cout;
	aavs a1(z,cout,x,u,y,v);

	initial begin
		clk = 0;
		reset <= 0 ;
	end
	always #10 clk = ~clk;

	initial begin
		
		x=2;y=2;v=2;u=2;
		#20 x=2;y=1;v=1;u=1 ;
                #20 x=1;y=2;v=0;u=1;
		#20 x=2;y=3;v=1;u=6;
		#100 $finish;

	end

	initial begin
		$dumpfile("aavs3.vcd");
		$dumpvars;
		$monitor(" At time %t, %0d, %0d, %0d, %0d, %0d, %0d ",$time, z,cout,x,y,u,v);
	end
endmodule
