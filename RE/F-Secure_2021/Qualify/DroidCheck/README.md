# Reverse Engineering

Challenge Name : DroidCheck

# Solution

We received one apk file . When we installed it, we can view this interface on our mobile phone.

![](https://github.com/H0j3n/EzpzCTF/blob/main/src/Pasted%20image%2020210920213220.png)

Trying to give random string , will give us **"WRONG PASSWORD"**

![](https://github.com/H0j3n/EzpzCTF/blob/main/src/Pasted%20image%2020210920213246.png)

Let's try to decompile it using `jadx-gui`. Looking at `AndroidManifest.xml` , we know that the package name is `com.test.locked`. 

![](https://github.com/H0j3n/EzpzCTF/blob/main/src/Pasted%20image%2020210920212058.png)

We can see more in `MainActivity.java`  

![](https://github.com/H0j3n/EzpzCTF/blob/main/src/Pasted%20image%2020210920212246.png)

It seems like our input which is the password will be pass to `transform` function which we can't seem to find the content of the function anywhere. Then, it will store in **"DIGEST"** which will then be called in `UnlockActivity.java` into **byteArrayExtra** variable.

![](https://github.com/H0j3n/EzpzCTF/blob/main/src/Pasted%20image%2020210920212932.png)

I can't solve it during the competition, but thanks to my friend @SKR , he give me some hint which is to look at **"/lib"** directory. After research on it, I found out that at `MainActivity.java`, there is one `native-lib` been loaded. This bring me to this article 

https://book.hacktricks.xyz/mobile-apps-pentesting/android-app-pentesting/reversing-native-libraries

The location of the library can be seen in **"/lib"** directory 

![](https://github.com/H0j3n/EzpzCTF/blob/main/src/Pasted%20image%2020210920213132.png)

Let's open it using Ghidra and rename the variable.

![](https://github.com/H0j3n/EzpzCTF/blob/main/src/Pasted%20image%2020210920223229.png)

The `transform_table` can be read by double click on the variable name. Highlight everything > Right Click > Copy Special > Byte String

![](https://github.com/H0j3n/EzpzCTF/blob/main/src/Pasted%20image%2020210920223456.png)

Then we can easily convert it to bytes using this command

```bash
echo -e "c6 49 13 9a 67 09 de 2b 58 1e 48 53 4f 9d 35 ae 81 d8 c4 77 ad 96 c1 ee 0c 16 32 1f aa 08 e5 ca 87 83 fe 45 e0 14 54 ff 5e 10 7f d3 20 2d 2e a7 7b 3e 64 a2 84 6f 91 bf b4 41 d6 ef 75 ac ed 5b 3c 50 74 0f 04 5d 71 4b 25 ba 9f 3f e1 60 8c 33 e7 c7 f4 1b c5 bc e2 ec b3 b1 43 23 1a 9c 24 7e cd da 82 6c d0 38 70 7d 0a fd 01 11 4e 7a 97 ce 40 88 26 b7 a0 86 cb 17 99 30 6e 63 98 8a cc d2 02 5a 56 34 8b a4 80 7c 19 42 95 21 b9 c2 8e 66 90 55 0d 47 b6 e4 d9 d4 a1 8d 93 db 6d 92 36 12 61 f0 e3 f5 73 f1 c9 c8 72 c0 f2 ab a8 85 f8 af d5 2f f9 0b eb 9e 4c dc 94 bb d1 a6 29 8f 37 4a a3 51 22 e9 39 e6 c3 1c 00 76 52 3b 65 fb 03 44 f3 05 a9 5c 46 e8 57 f7 4d 3d 06 27 cf 15 3a f6 5f dd b8 b2 fc 68 d7 bd 62 9b 07 89 59 2a 6b 31 a5 1d 0e b5 28 2c fa be 79 18 6a 78 69 ea b0" | xxd -r -p > dump
```

There are 2 methods to solve this challenge, but I will only write the solutions for `Bruteforce` while the other one you can read my friend's writeup in the reference. You can recheck the variable name for python with the Ghidra.

```python
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
```

# Flag

![](https://github.com/H0j3n/EzpzCTF/blob/main/src/Pasted%20image%2020210920223859.png)

# References

- https://hong5489.github.io/2021-09-17-fsec2021/