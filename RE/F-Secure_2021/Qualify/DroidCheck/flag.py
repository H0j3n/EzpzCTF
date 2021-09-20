target = [ i % 256 for i in [-74, 56, -99, -111, 95, 98, -38, -116, -5, 76, -18, -84, -65, -112, 31, -81]]
flag = [ ord(i) for i in "p"*16 ]
realFlag = ["a"]*16

# Read transform_table data
bytes = open("dump","rb").read()
transform_table = []
for i in bytes:
	transform_table.append(i)

# Solution (BruteForce)
index1 = 0
for index2 in range(0,len(target),2):
	bVar1 = transform_table[index2]

	# Bruteforce flag
	if (target[index2] != transform_table[flag[index2]] ^ bVar1 ^ index1):
		for k in range(256):
			if (target[index2] == transform_table[k] ^ bVar1 ^ index1):
				realFlag[index2] = chr(k)
				break
	# Bruteforce flag
	index1 = transform_table[index2 + 1] ^ bVar1 ^ index1
	if (target[index2 + 1] != transform_table[flag[index2 + 1]] ^ index1):
		for k in range(256):
			if (target[index2 + 1] == transform_table[k] ^ index1):
				realFlag[index2 + 1] = chr(k)
				break
print("".join(realFlag))
