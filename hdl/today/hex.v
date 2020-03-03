module ha(input a, b, output sum, cout);
   assign {cout, sum} = a + b;
endmodule

module fa(input a, b, cin, output sum, cout);
   assign {cout, sum} = a + b + cin;
endmodule

module mux(input a, b, s, output y);
   reg y;
   always @ (*)
     begin
       if (s) y = b;
       else y = a;
     end
endmodule

module base(input [3:0] x, y, input cin, output [3:0] sum, output cout);
   wire [4:0] c;
   assign c[0] = cin;
   assign cout = c[4];
  
   genvar n;
    for (n = 0; n<4; n = n+1)
      fa fa(x[n], y[n], c[n], sum[n], c[n+1]);
endmodule
        
module prop(input [3:0] sum, output c);
   wire [4:0] s;
   assign s[0] = 1;
   assign c = s[4];
   genvar n;
     for(n = 0; n<3; n = n+1)
       and (s[n+1],sum[n],s[n]); 
endmodule

module sum(input [3:0] x, y, input cin, output [3:0] sum);
   wire [3:0] s;
   wire [4:0] c;
   assign c[0] = cin;
   wire cout;
   base bs(x, y, 1'b0, s, cout);
   genvar n;
     for(n = 0; n < 4; n=n+1)
        ha h(s[n], c[n], sum[n], c[n+1]);
endmodule

module radix (input [3:0] x, y, input cin, output [3:0] sum, output cout);
  wire [3:0] s;
  wire c, k;
  base b (x, y, 1'b0, s, c);
  prop p (s,k);
  mux m (c, cin, k, cout);
  sum j (x, y, cin, sum);
endmodule

module radixf #(parameter m = 4) (input [4*m-1:0] x, y, input cin, output [4*m-1:0] sum, output cout);
  wire [4:0] c;
  assign c[0] = cin;
  assign cout = c[4];

  radix r1 (x[3:0], y[3:0], c[0], sum[3:0], c[1]);
  radix r2 (x[7:4], y[7:4], c[1], sum[7:4], c[2]); 
  radix r3 (x[11:8], y[11:8], c[2], sum[11:8], c[3]); 
  radix r4 (x[15:12], y[15:12], c[3], sum[15:12], c[4]);     
endmodule
  

 
 
  
  
 
