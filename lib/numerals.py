b = " "
v = "|"
h = ["_", "‾"]
d = ["\\", "/"]


b_r = [b for _ in range(4)]
v_r = [b, b, b, v]


numbers = [
	[b_r for _ in range(4)], #0
	[[h[0], h[0], h[0], b], b_r, b_r, b_r], #1
	[b_r, b_r, b_r, [h[1], h[1], h[1], b]], #2
	[b_r, [d[0], b, b, b], [b, d[0], b, b], [b, b, d[0], b]], #3
	[b_r, [b, b, d[1], b], [b, d[1], b, b], [d[1], b, b, b]], #4
	[[h[0], h[0], h[0], b], [b, b, d[1], b], [b, d[1], b, b], [d[1], b, b, b]], #5
	[b_r, v_r, v_r, b_r], #6
	[[h[0], h[0], h[0], b], v_r, v_r, b_r], #7
	[b_r, v_r, v_r, [h[1], h[1], h[1], b]], #8
	[[h[0], h[0], h[0], b], v_r, v_r, [h[1], h[1], h[1], b]] #9
]


stem = [b, v, v, v, v, v, v, v, b] # used to place/track centre line within rows (top to bottom)


middle_row = "".join([b, b, b, b, stem[4], b, b, b, b])