
module non_rest #(parameter n=16, s=16) (output wire [s-1:0] QUOTIENT, REMAINDER, output wire done,
    input wire [n-1:0] x, y, input wire clk, reset, start);
    
    reg [s-1:0] Q, R, M;
    integer count;
    reg finish_tk;

    assign QUOTIENT = Q;
    assign REMAINDER = R;
    assign done = finish_tk;

    always @(posedge clk, posedge reset) 
		begin
			if (reset) 
				begin 
					count = 0; finish_tk = 1'b0; Q = 0; R = 0; 
				end
			else if (start) 
				begin 
					Q = x; M = y; count = 1; 
				end 
			else if (count > 0) 
				begin 
					if (R[s-1] == 1) 
						begin  
							R = R << 1;             
							R[0] = Q[s-1];          
							Q = Q << 1;             
							R = R + M; 
						end
					else 
						begin    
							R = R << 1;           
							R[0] = Q[s-1];        
							Q = Q << 1;           
							R = R - M;  
						end
			if (R[s-1] == 1) 
				begin 
					Q[0] = 0; 
				end 
			else 
				begin 
					Q[0] = 1; 
				end             
			 count = count + 1; 
			 if (count==s+1) 
    begin 
		count = 0;
		if (R[s-1] == 1) 
			begin 
				R = R + M; 
			end  
		finish_tk = 1'b1;
	end
	end
    end
endmodule
