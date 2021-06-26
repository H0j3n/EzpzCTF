enc_1 = open("output.txt").read().strip()

# PartA
k = 0
partA = ""
for i in range(0,len(enc_1),8):
	partA += enc_1[k:i+8][3]
	k += 8

# Output
found = int(partA, 2).to_bytes((len(partA) + 7) // 8, byteorder='big')
print(found)


