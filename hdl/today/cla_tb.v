`timescale 1 ns / 100 ps

module test;
  localparam width = 10;
  reg [width-1:0] A, B;
  reg C;

  initial
  begin
      A = 55;
      B = 421;
      C = 0;
  end
  

  wire [width-1:0] A1;
  wire C1;
  
  carry_look_ahead_adder #(.width(width)) wa (A1, C1, A, B, C);
  initial
    begin
        $monitor("At time %t, sum = %0d  cout = %0d  numbers::  %0d %0d %0d", $time, A1, C1, A, B, C);
        #10 $finish;
    end
  initial
    begin
        $dumpfile("a.vcd"); 
        $dumpvars;
    end 
endmodule


