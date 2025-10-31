enc = b'ndqqwtgkW[)Xc`b\"\\\"`LM^R'
enc += b'\x5F\x22\x23\x3B\x1A\x53\x4F\x1A'[::-1]

for _ in range(len(enc)):
    print(chr(enc[_] + _), end="")

# OUTPUT : nest{ymr_d3comp1l3r_ash1gl4V??}