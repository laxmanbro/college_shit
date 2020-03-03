module test;
 reg [3:0] N,D;
 wire [3:0] Q,R;
 
 NonrestoreDV n(N,D,Q,R);
 
 initial begin
	N = 4'b0010;
	D = 4'b0100;
	end
	
	initial begin
	$monitor("At time = %0t, N = %0b, D = %0b, Q = %0b, R = %0b", $time, N, D, Q, R);
	end
	
	initial begin
	#1000;
	$finish;
	end
	endmodule
