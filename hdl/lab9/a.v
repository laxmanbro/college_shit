module fulladder(output wire s1, outc, input wire a1, b1,c1);
    assign {outc, s1} = a1 + b1 + c1 ;
endmodule

module aavs(output wire  z, output wire cout, input wire  x,u,y,v);
	wire s,c;
	assign cout = c;

	and(s ,x ,y );
        
	fulladder f1(z,c,s,u,v);
endmodule

