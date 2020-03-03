sim: nerd.v nerd_tb.v
	iverilog -o sim nerd.v nerd_tb.v
	
a.vcd: sim
	./sim
