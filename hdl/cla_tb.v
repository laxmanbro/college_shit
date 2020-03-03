module claa_test;
 
  localparam width = 10;
  reg [width-1:0] a, b;
  reg cin;
  reg clk,reset;
  
  wire [width-1:0] z;
  wire cout;
  main m1(z,cout,a,b,cin);
   	
 
  initial begin
		clk = 0;
		cin = 1'b0;
		reset <= 0 ;
   end
   always #10 clk = ~clk;		
 
   initial begin
	 
		 
		 a = 10;b = 6; 
		 
		 #20 a = 43; b = 22;
		 
		 #20 a = 97;b = 143;
		 
		 #20 a = 530;b = 520;
		 #100  $finish;
		
	 end
   
   
  
  initial begin
	$dumpfile ("a.vcd");
	$dumpvars;
        $monitor(" At time %t,%0d   %0d     %0d  %0d   %0d    ", $time, z,cout,a,b,cin);
        
    end

endmodule

