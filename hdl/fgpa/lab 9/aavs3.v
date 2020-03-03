module fulladder(output wire s1, outc, input wire a1, b1,c1);
    assign {outc, s1} = a1 + b1 + c1 ;
endmodule

module aavs(output wire [5:0] z, output wire cout, input wire [3:0] x,u , input wire [2:0] y,v);
	wire [3:0] c1,c2,c3 ; 
	wire [2:0] o1,o2 ;
	wire [3:0] s1,s2,s3 ; 
	assign cout = c3[3];

        and( s1[0] ,x[0] , y[0] );
	and( s1[1] ,x[1] , y[0] );
	and( s2[0] ,x[0] , y[1] );
	and( s1[2] ,x[2] , y[0] );
	and( s2[1] ,x[1] , y[1] );
	and( s3[0] ,x[0] , y[2] );
        and( s1[3] ,x[3] ,y[0] );
	and( s2[2] ,x[2] ,y[1] );
	and( s3[1] ,x[1] ,y[2] );
	and( s2[3] ,x[3] ,y[1] );
	and( s3[2] ,x[2] ,y[2] );	
	and( s3[3] ,x[3] ,y[2] );


	fulladder f2(o1[0],c1[1],s1[1],u[1],c1[0]);
	fulladder f4(o1[1],c1[2],s1[2],u[2],c1[1]);
	fulladder f5(o2[0],c2[1],s2[1],o1[1],c2[0]);
	fulladder f7(o1[2],c1[3],s1[3],u[3],c1[2]);
	fulladder f8(o2[1],c2[2],s2[2],o1[2],c2[1]);
	fulladder f10(o2[2],c2[3],s2[3],c1[3],c2[2]);
	fulladder f1(z[0],c1[0],s1[0],u[0],v[0]);
	fulladder f3(z[1],c2[0],s2[0],o1[0],v[1]);
	fulladder f6(z[2],c3[0],s3[0],o2[0],v[2]);
	fulladder f9(z[3],c3[1],s3[1],o2[1],c3[0]);
	fulladder f11(z[4],c3[2],s3[2],o2[2],c3[1]) ;
 	fulladder f12(z[5],c3[3],s3[3],c2[3],c3[2]);
endmodule

