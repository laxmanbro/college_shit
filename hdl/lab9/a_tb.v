module aavs1_test;

	reg x,y,u,v;
        wire z;
        reg clk,reset;
	wire cout;
        aavs1 a1(z,cout,x,y,u,v);

	initial begin
		clk = 0;
		reset <= 0 ;
	end
	always #10 clk = ~clk;

	initial begin
		
		x=0;y=1;v=1;u=1;
		#20 x=1;y=1;v=0;u=1 ;
                #20 x=1;y=0;v=1;u=1;
		#20 x=1;y=0;v=1;u=0;
		#100 $finish;

	end

	initial begin
		$dumpfile("a.vcd");
		$dumpvars;
		$monitor(" At time %t, %0d, %0d, %0d, %0d, %0d, %0d ",$time, z,cout,x,y,u,v);
	end
endmodule
