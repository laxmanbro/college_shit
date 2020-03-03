
module rd #(parameter n=8, p=8) (output wire [p-1:0] quotient, remainder, output wire done,
    input wire [n-1:0] x, y, input wire clk, reset, start);
    reg [p-1:0] q, r, rnext;
    integer z1, z2, count;
    reg qbit, done_tick;

    assign quotient = q;
    assign remainder = r;
    assign done = done_tick;

    always @(posedge clk, posedge reset) begin
      if (reset) begin count = 0; done_tick = 1'b0; qbit = 1'b0; q = 0; r = 0; end
      else if (start) begin rnext = x; count = 1; end
      else if (count>0) begin
				//both are run at a time in always to make it in one clock cycle
        r = rnext;
        qbit = 1'b0;
        z1 = 2*r - y;
        z2 = 2*r + y;//first bit iteration
        if (r[p-1]==1) begin rnext = z2; end
        if (r[p-1]==0) begin rnext = z1; end
        if (rnext[p-1]==1) begin qbit = 1'b0; end
        if (rnext[p-1]==0) begin qbit = 1'b1; end
        q = {q[p-2:0], qbit};


        r = rnext;
        qbit = 1'b0;
        z1 = 2*r - y;//second bit iteration and then it again repeats
        z2 = 2*r + y;
        if (r[p-1]==1) begin rnext = z2; end
        if (r[p-1]==0) begin rnext = z1; end
        if (rnext[p-1]==1) begin qbit = 1'b0; end
        if (rnext[p-1]==0) begin qbit = 1'b1; end
        q = {q[p-2:0], qbit};

        count = count + 1;
        if (count==p-3) begin
          count=0;
          done_tick = 1'b1;
        if (r[p-1]==1) begin r = r + y; end
        end
      end
    end
endmodule
