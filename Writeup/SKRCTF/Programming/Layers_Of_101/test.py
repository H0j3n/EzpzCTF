enc_1 = open("message.txt").read().strip()

#PARTA
k = 0
partA = ""
for i in range(0,len(enc_1),8):
    partA += enc_1[k:i+8][3]
    k += 8

#PARTB
k = 0
partB = ""
for i in range(0,len(partA),8):
        partB += partA[k:i+8][4]
        k += 8

file_found=int(partB, 2).to_bytes((len(partB) + 7) // 8, 'big')
strs = ""
for i in file_found:
    strs += chr(i)
print(strs)
