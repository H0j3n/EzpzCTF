# Reverse Engineering

Challenge Name : aWASMe

# Solution

```python
import string

def checkFlag_3(flag,indexflag,checker):
	var3 = 0 #Index (Not using)
	var5 = -1
	payload = string.printable
	for k in payload:
		for l in payload:
			for m in payload:
				# Initialize
				var5 = -1
				# Start Look for flag
				flag[indexflag[0]] = m
				flag[indexflag[1]] = l
				flag[indexflag[2]] = k
				for i in flag:
					var0 = 48
					var6 = ord(i)
					var4 = 8 # Index
					# Loop (2)
					for i in range(var4):
						var2 = ((var5 & 0xFFFFFFFF) >> 1)
						var6 = ((var6 << 24) >> 24)
						if ((var6 ^ var5) & 1):
							var5 = var2 ^ -306674912
						else:
							var5 = var2
						var6 = var6  >> 1
				var5 = var5 ^ -1
				if var5 == checker:
					print("[+] Found!")
#					print(flag)
					return flag

def checkFlag_2(flag,indexflag,checker):
	var3 = 0 #Index (Not using)
	var5 = -1
	payload = string.printable
	for k in payload:
		for l in payload:
			# Initialize
			var5 = -1
			# Start Look for flag
			flag[indexflag[0]] = k
			flag[indexflag[1]] = l
			for i in flag:
				var0 = 48
				var6 = ord(i)
				var4 = 8 # Index
				# Loop (2)
				for i in range(var4):
					var2 = ((var5 & 0xFFFFFFFF) >> 1)
					var6 = ((var6 << 24) >> 24)
					if ((var6 ^ var5) & 1):
						var5 = var2 ^ -306674912
					else:
						var5 = var2
					var6 = var6  >> 1
			var5 = var5 ^ -1
			if var5 == checker:
				print("[+] Found!")
				return flag
flag = ['f','s'] + ['CHANGE_HERE']*18 + ['c','y','b','e','r']
# Round 1
tempflag =  [flag[0]]+[flag[2]]+[flag[22]]+[flag[9]]+[flag[16]]+[flag[24]]
len_flag = [i for i, e in enumerate(tempflag) if e == 'CHANGE_HERE']
checker = -206711191
temp = checkFlag_3(tempflag,len_flag,checker)
flag[2] = temp[1]
flag[9] = temp[3]
flag[16] = temp[4]
# Round 2
tempflag =  [flag[20]] + [flag[21]] + [flag[6]] + [flag[20]] + [flag[12]]
len_flag = [i for i, e in enumerate(tempflag) if e == 'CHANGE_HERE']
checker = -1201157354
temp = checkFlag_2(tempflag,len_flag,checker)
flag[6] = temp[2]
flag[12] = temp[4]
# Round 3 
tempflag = [flag[3]] + [flag[1]] + [flag[1]] + [flag[4]] + [flag[5]] + [flag[24]]
len_flag = [i for i, e in enumerate(tempflag) if e == 'CHANGE_HERE']
checker = 797743837
temp = checkFlag_3(tempflag,len_flag,checker)
flag[3] = temp[0]
flag[4] = temp[3]
flag[5] = temp[4]
# Round 4
tempflag = [flag[23]] + [flag[23]] + [flag[8]] + [flag[18]]
len_flag = [i for i, e in enumerate(tempflag) if e == 'CHANGE_HERE']
checker = -376868582
temp = checkFlag_2(tempflag,len_flag,checker)
flag[8] = temp[2]
flag[18] = temp[3]
# Round 5
tempflag = [flag[1]] + [flag[7]] + [flag[13]] + [flag[17]] + [flag[0]]
len_flag = [i for i, e in enumerate(tempflag) if e == 'CHANGE_HERE']
checker = 1616048751
temp = checkFlag_3(tempflag,len_flag,checker)
flag[7] = temp[1]
flag[13] = temp[2]
flag[17] = temp[3]
# Round 6
tempflag = [flag[10]] + [flag[20]] + [flag[14]] + [flag[19]] + [flag[24]] + [flag[21]]
len_flag = [i for i, e in enumerate(tempflag) if e == 'CHANGE_HERE']
checker = -12729135
temp = checkFlag_3(tempflag,len_flag,checker)
flag[10] = temp[0]
flag[14] = temp[2]
flag[19] = temp[3]
# Last Round
tempflag =  [flag[0]] + [flag[15]] + [flag[11]] + [flag[22]]
len_flag = [i for i, e in enumerate(tempflag) if e == 'CHANGE_HERE']
checker = 2122552725
temp = checkFlag_2(tempflag,len_flag,checker)
flag[15] = temp[1]
flag[11] = temp[2]

print("Flag : " + ''.join(flag))
```

# Flag

![](https://github.com/H0j3n/EzpzCTF/blob/main/src/Pasted%20image%2020210920233500.png)

# References

- 