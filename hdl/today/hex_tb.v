module test;
   localparam m = 4;
   reg [4*m-1:0] x, y;
   reg cin;
   wire [4*m-1:0] sum;
   wire cout;

   radixf rf (x, y, cin, sum, cout);

   initial begin
      #5 {x, y, cin} = {16'h121a, 16'h211b, 1'b0};
     
   end

   initial begin
        $dumpfile("a.vcd");
        $dumpvars;
        $monitor("Time = %t, x = %d, y = %d, sum = %d, cout = %b", $time, x, y, sum, cout);
        #150 $finish;
   end
endmodule
