# Reverse Engineering

Challenge Name : dong-van

# Solution

- Unzip the file

```bash
unzip re100_35d14595b17756b79556f6eca775c31a
```

- Before jump to radare2 and Ghidra. Let's try run it and see how the program works.

![](https://github.com/H0j3n/EzpzCTF/blob/main/src/Pasted%20image%2020210819122155.png)

- It receive an input (secret) and maybe we should look for the exact secret to get the flag . Let's use Ghidra.

![](https://github.com/H0j3n/EzpzCTF/blob/main/src/Pasted%20image%2020210819123337.png)

- From the strings we found 2 strings that looks like Base64 , but we can't decode it. Looks really weird. Let's look in the function that have the strings

![](https://github.com/H0j3n/EzpzCTF/blob/main/src/Pasted%20image%2020210819123741.png)

- We can see that there is a loop in range of 64 , which might be that the strings we found is a custom Base64. Thats why we cant decode another base64 we found. 

![](https://github.com/H0j3n/EzpzCTF/blob/main/src/Pasted%20image%2020210819124406.png)

- We need to ensure what we input will be the same as **"ms4otszPhcr7tMmzGMkHyFn="** . I have create one python script that could help us to gain the real sentence with using the custom Base64 characters.

```python
import base64

custom_enc = "ms4otszPhcr7tMmzGMkHyFn="
ori = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789/="
custom = "ELF8n0BKxOCbj/WU9mwle4cG6hytqD+P3kZ7AzYsag2NufopRSIVQHMXJri51Tdv"
fix_enc = ""

# Fixing 
for i in range(len(custom_enc)):
	try:
		fix_enc += ori[custom.index(custom_enc[i])]
	except:
		fix_enc += custom_enc[i]
# Decode
print(base64.b64decode(fix_enc))
```

- Run it and we got the secret we need !

![](https://github.com/H0j3n/EzpzCTF/blob/main/src/Pasted%20image%2020210819125514.png)

# Flag

To get the flag we need to send the secret to the flag server.

# References

- https://github.com/ByteBandits/writeups/tree/master/whitehat-grand-prix-quals-2015/reversing/dong%20wan
- https://github.com/ctfs/write-ups-2015/tree/master/whitehat-grand-prix-qualification-2015/reverse/dong-van