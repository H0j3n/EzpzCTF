# Reverse Engineering

Challenge Name : Baby Rev

# Solution

![[Pasted image 20210921144041.png]]

```python
import binascii

xor_key = 0xdeadbeef
flag_hex = [0x99dfdf8d, 0x9de2f094, 0x7830acdf8d8b, 0x5feadadf96, 0x5f33b8cb8fdf]
flag = ""
for i in flag_hex:
	flag += str(hex(xor_key ^ i)[2:])

print(bytes.fromhex(flag).decode('utf-8')+"}")
```

# Flag

![[Pasted image 20210921144122.png]]

# References

- 