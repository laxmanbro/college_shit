module rdd #(parameter n=8, p=8) (output wire [p-1:0] quotient, remainder, output wire done,
    input wire [n-1:0] x, y, input wire clk, reset, start,t);
    reg [p-1:0] Q;
    integer t=8;
    reg [p:0] M, A,temp;
    reg done_tick;
    
    assign quotient = Q;
    assign remainder = A;
    assign done = done_tick;

    always @(posedge clk, posedge reset) begin
      if (reset) begin  Q = 0; A = 0;M=0; end
      else if (start) begin Q = x; M=y; end
      
			  if (t>0) begin
				temp=A;
				A = {A[p:1], Q[p-1]};
				Q=Q<<1;
				A=A-M;
			if(A[p]==0) begin Q[0]=1; end
			else begin Q[0]=0;A=temp;	end
			  end
			  t=t-1;
			  if(t==0) begin done_tick=1'b1; end
    end
endmodule
