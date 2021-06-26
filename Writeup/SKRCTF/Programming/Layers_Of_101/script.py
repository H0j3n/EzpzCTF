enc_1 = open("message.txt").read().strip()

# PartA
k = 0
partA = ""
for i in range(0,len(enc_1),8):
	partA += enc_1[k:i+8][3]
	k += 8

# PartB
k = 0
partB = ""
for i in range(0,len(partA),8):
	partB += partA[k:i+8][4]
	k += 8

# File Output
file_found = int(partB, 2).to_bytes((len(partB) + 7) // 8, byteorder='big')
f = open("output.png", "wb")
f.write(file_found)
f.close()
