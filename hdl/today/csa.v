module fa(output wire s, oc, input wire a, b, ic);
    assign {oc, s} = ic + a + b;
endmodule

module csa(output wire [7:0] z,output wire cout,input wire [7:0] a,b,c);
	wire s[7:0];
	wire pc[7:0];
	wire fc[7:0];
	wire u;
	
	//one bit full adders
	fa f1(s[0],pc[0],a[0],b[0],c[0]);
	fa f2(s[1],pc[1],a[1],b[1],c[1]);
	fa f3(s[2],pc[2],a[2],b[2],c[2]);
	fa f4(s[3],pc[3],a[3],b[3],c[3]);
	fa f5(s[4],pc[4],a[4],b[4],c[4]);
	fa f6(s[5],pc[5],a[5],b[5],c[5]);
	fa f7(s[6],pc[6],a[6],b[6],c[6]);
	fa f8(s[7],pc[7],a[7],b[7],c[7]);


	//carry save adder implementation
	fa f9(z[1],fc[0],s[1],pc[0],1'b0);
	fa f10(z[2],fc[1],s[2],pc[1],fc[0]);
	fa f11(z[3],fc[2],s[3],pc[2],fc[1]);
	fa f12(z[4],fc[3],s[4],pc[3],fc[2]);
	fa f13(z[5],fc[4],s[5],pc[4],fc[3]);
	fa f14(z[6],fc[5],s[6],pc[5],fc[4]);
	fa f15(z[7],fc[6],s[7],pc[6],fc[5]);
	fa f16(u,cout,1'b0,pc[7],fc[6]);



	assign z[0] = s[0];
endmodule	

