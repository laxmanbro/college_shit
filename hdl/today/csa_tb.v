module csa_test;
 
  localparam width = 8;
  reg [width-1:0] a, b,c;
  reg clk,reset;
  
  wire [width-1:0] z;
  wire cout;
  csa c1 (z,cout,a,b,c);
   	
 
  initial begin
		clk = 0;
		reset <= 0 ;
   end
   always #10 clk = ~clk;		
 
   initial begin
	 
		 a = 45;b = 72; c = 56;
		 #20 a = 66; b = 62;c = 48;
		 #20 a = 92;b = 85;c = 74;
		 #20 a = 12;b = 27;c = 143;
		 #100  $finish;
		
	 end
   
   initial begin
	$dumpfile ("a.vcd");
	$dumpvars;
        $monitor(" At time %t,%0d   %0d     %0d  %0d   %0d    %0d", $time, z,cout,a,b,c,clk);
        
    end

endmodule

