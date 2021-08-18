# Reverse Engineering

Challenge Name : Reversing-1

# Solution

- Extract the binary from compressed data.

```bash
bzip2 -d boo.tar.gz
tar -xvf boo.tar.gz.out
```

- Found out that it pack with UPX using binwalk.

```bash
binwalk boo
```

![[Pasted image 20210818104014.png]]

- Unpacked using upx commands

```bash
upx -d boo
```

![[Pasted image 20210818104051.png]]

- Found out a lot of python on the binary but cannot found the header "50 59 5A" (PYZ). Looking back at the packed binary found the header.

```bash
xxd boo.\~ | grep -i PYZ
```

![[Pasted image 20210818105758.png]]

- Extract using **pyinstxtractor.py**

```bash
# Download
https://github.com/extremecoders-re/pyinstxtractor.git

# Command
python3 pyinstxtractor.py boo
```

![[Pasted image 20210818115710.png]]

- Read boo.pyc and get the flag!

# Flag

![[Pasted image 20210818115822.png]]

# References

- https://github.com/ctfs/write-ups-2015/tree/master/nullcon-hackim-2015/reversing-1