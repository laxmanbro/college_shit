`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date:    16:42:47 01/15/2019 
// Design Name: 
// Module Name:    sb 
// Project Name: 
// Target Devices: 
// Tool versions: 
// Description: 
//
// Dependencies: 
//
// Revision: 
// Revision 0.01 - File Created
// Additional Comments: 
//
//////////////////////////////////////////////////////////////////////////////////
module sb1(b,a,cin,s,d,cout);

input a,b,cin,s;
output d,cout;
///full adder/subtractor........
assign d = a^b1^cin;

assign cout = (b1 & cin)|(b1 & a)|(a & cin);
////compliment of b
assign b1 = s^b;
endmodule
