module fa(output wire s, cout, input wire a, b, cin);
    assign {cout, s} = cin + a + b;
endmodule

module wide_adder #(parameter [3:0] width = 4) (output wire [width-1:0] s, 
    output wire cout, input wire [width-1:0] a, b, input wire cin);

    wire [width:0] c;
    assign c[0] = cin;
    assign cout = c[width];

    genvar n;
    generate
        for(n=0; n<width; n=n+1)
            fa fa(s[n], c[n+1], a[n], b[n], c[n]);
    endgenerate
endmodule

module adder_16bit(output wire [15:0] sum, output wire cout, input wire [15:0] a, b, 
    input wire cin, clk, reset);
    reg [3:0] r1,r2,r3;
    reg [3:0] s1,s2,s3,s4;
    reg [3:0] t1,t2,t3,t4,t5;
    reg [3:0] u1,u2,u3,u4,u5,u6;
    reg [3:0] a1,a2,a3;
    wire [2:0] c;
    wire [15:0] s;

    wide_adder w1(s[3:0], c[0], a[3:0], b[3:0], cin);
    wide_adder w2(s[7:4], c[1], s1, s2, a1);
    wide_adder w3(s[11:8], c[2], t3, t4, a2);
    wide_adder w4(sum[15:12], cout, u5, u6, a3);

    always @(posedge clk, reset) begin
        if (reset) begin
            r1<=0;r2<=0;r3<=0;
            a1<=0;a2<=0;a3<=0;
            s1<=0;s2<=0;s3<=0;s4<=0;
            t1<=0;t2<=0;t3<=0;t4<=0;t5<=0;
            u1<=0;u2<=0;u3<=0;u4<=0;u5<=0;u6<=0;
        end
        else begin
        //1st level
            r1<=s[3:0];
            r2<=r1;
            r3<=r2;
        //2nd level
            s1<=a[7:4];
            s1<=b[7:4];
            a1<=c[0];
            s3<=s[7:4];
            s4<=s3;
        //3rd level
            t1<=a[11:8];
            t2<=b[11:8];
            t3<=t1;
            t4<=t2;
            a2<=c[1];
            t5<=s[11:8];
        //4th level
            u1<=a[15:12];
            u2<=b[15:12];
            u3<=u1;
            u4<=u2;
            u5<=u3;
            u6<=u4;
            a3<=c[2];
        end
    end

    assign sum[3:0]=r3;
    assign sum[7:4]=s4;
    assign sum[11:8]=t5;
endmodule
