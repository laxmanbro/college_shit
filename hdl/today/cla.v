module exor(output z_i,input x_i,y_i);
  wire Ab,Bb,A11,B11;
  not(Ab,x_i);
  not(Bb,y_i);
  and(A11,Ab,y_i);
  and(B11,Bb,x_i);
  or(z_i,A11,B11);
endmodule

module carry(output cii , input xi,yi,ci);
  wire z_i; 
  exor x1(z_i,xi,yi);
  
  reg cii;
   always @(*)
       if (z_i)  cii = ci;
       else  cii = yi;
endmodule

module sum_onebit(output zi , input xi,yi,ci);
  wire x11;
  exor z1(x11,xi,yi);
  exor z2(zi,x11,ci);
endmodule

module cla(output wire s, cout, input wire a, b, cin);
    carry c1(cout,a,b,cin);
    sum_onebit s1(s,a,b,cin);
endmodule

module carry_look_ahead_adder #(parameter [10:0] width = 10) (s, cout, a, b, cin);
    output [width-1:0] s;
    output cout;
    input [width-1:0] a, b;
    input cin;

    wire [width:0] c;
    assign c[0] = cin;
    assign cout = c[width];

    genvar n;
    generate
        for(n=0; n<width; n=n+1)
            cla fa(s[n], c[n+1], a[n], b[n], c[n]);
    endgenerate
endmodule
 

