module fulladder(output wire s1, outc, input wire a1, b1,c1);
    assign {outc, s1} = a1 + b1 + c1 ;
endmodule

module aavs2(output wire [3:0] z, output wire cout, input wire [3:0] x,u , input wire  y,v);
	wire [3:0] c;
	wire [3:0] s;
	assign cout = c[3];
   
	and(s[0] , x[0] ,y);
        and(s[1] , x[1] ,y);
	and(s[2] , x[2] ,y);
	and(s[3] , x[3] ,y);

	fulladder f1(z[0],c[0],s[0],u[0],v);
        fulladder f2(z[1],c[1],s[1],u[1],c[0]);
	fulladder f3(z[2],c[2],s[2],u[2],c[1]);
	fulladder f4(z[3],c[3],s[3],u[3],c[2]);
endmodule
