# Programming

Challenge Name : Layers Of 101

# Solution

First of all we need to download the file first:
- [https://drive.google.com/file/d/1FVge4z-beR2pxSk3M1H7vTyy4bHn0fSc/view](https://drive.google.com/file/d/1FVge4z-beR2pxSk3M1H7vTyy4bHn0fSc/view)

The content of the file itself really hurt my eyes haha

![](https://github.com/H0j3n/EzpzCTF/blob/main/src/Pasted%20image%2020210626211417.png)

If we look closely it similar to 8 bit-binary . Example :  `000000110`. Using this python script we can differentiate and see how we can divide the strings as 8 bit-binary.

```python
enc_1 = open("message.txt").read().strip()

k = 0
partA = ""
for i in range(0,len(enc_1),8):
        print(enc_1[k:i+8])
        k += 8

```

![](https://github.com/H0j3n/EzpzCTF/blob/main/src/Pasted%20image%2020210626212414.png)

From the output above we can see that there is a pattern which one row with value `1` in index 3 and another row with `0` in index 3.  From the top 1 until the first `1` value we encounter almost the same as 8 bit-binary. Maybe we can try get with index 3 value first?

```python
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
        print(partA[k:i+8])
        k += 8
```

![](https://github.com/H0j3n/EzpzCTF/blob/main/src/Pasted%20image%2020210626213324.png)

From the output above we can see that there is a pattern which one row with value `1` in index 4 and another row with `0` in index 4. We can try the same technique that we already implement and lets see if we can get something .

```python
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
k = 0
for i in range(0,len(partB),8):
        print(partB[k:i+8])
        k += 8
```

![](https://github.com/H0j3n/EzpzCTF/blob/main/src/Pasted%20image%2020210626214204.png)

This time it doesn't look like have any patterns. Might be that we can directly convert it from binary and combine it. I found a method that we can implement and you can try read it in here:
- [https://stackoverflow.com/questions/32675679/convert-binary-string-to-bytearray-in-python-3](https://stackoverflow.com/questions/32675679/convert-binary-string-to-bytearray-in-python-3)

```python

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
print(file_found)

```

Wow! There is PNG there!!

![](https://github.com/H0j3n/EzpzCTF/blob/main/src/Pasted%20image%2020210626214531.png)

Let's try write it into one image file from this bytes.

```python
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

```

Okay nice we can see that it is a PNG file but we can't open it?

![](https://github.com/H0j3n/EzpzCTF/blob/main/src/Pasted%20image%2020210626215351.png)

Luckily we have this tool that can try fix/repair our PNG image.
- [https://github.com/sherlly/PCRT](https://github.com/sherlly/PCRT)

```bash
python PCRT.py -i /pathto/output.png
```

![](https://github.com/H0j3n/EzpzCTF/blob/main/src/Pasted%20image%2020210626215751.png)

Okay thats a good sign! Let's try open it!

![](https://github.com/H0j3n/EzpzCTF/blob/main/src/Pasted%20image%2020210626215838.png)

We got like really random kind of QR Code. We might be able to scan if we lucky xD. But let's use another tool which could help us identify for any data in here.

```bash
# Install
sudo apt-get install zbar-tools

# Commands
zbarimg output.png
```

![](https://github.com/H0j3n/EzpzCTF/blob/main/src/Pasted%20image%2020210626220057.png)

Nice! We are almost there! Let's save this as `output.txt` and run our previous script to get to the next step.

```python
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
```

We get the flag as we manage to decode the last layer!

# Flag

![](https://github.com/H0j3n/EzpzCTF/blob/main/src/Pasted%20image%2020210626220600.png)