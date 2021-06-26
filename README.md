# EzpzCTF

# Misc

### Zbar-Tools (QR Code)

```code
# Install
sudo apt-get install zbar-tools

# Commands
zbarimg output.png
```

# CryptoGraphy

### Online Tools

```bash
https://gchq.github.io/CyberChef/
https://scwf.dima.ninja/
```

### RSACtftool

```bash
# Download
https://github.com/Ganapati/RsaCtfTool

#If sagemath error try
sudo apt-get install sagemath

#If wolframe error try
pip3 install wolframalpha

#Commands
python3 RsaCtfTool.py --publickey PublicKey.pem --private --uncipher ciphertext
python3 RsaCtfTool.py -n 712312... -e 65537 --uncipher 125123...
python3 RsaCtfTool.py --publickey public.pem --private > private.key
```

### GPG/PGP

```bash
# Commands
gpg --import key.asc
gpg --decrypt backup.pgp
```

### Openssl

```bash
# Commands
openssl rsautl -decrypt -inkey private.key -in note2_encrypted.txt -out note2.txt
```

### PadBuster

```bash
# Downloads
https://github.com/AonCyberLabs/PadBuster

# Commands
perl ./padBuster.pl http://10.10.10.10/index.php "GVrfxWD0mmxRM0RPLht/oUpybgnBn/Oy" 8 -encoding 0 -cookies "hcon=GVrfxWD0mmxRM0RPLht/oUpybgnBn/Oy"
```

### Jwt-Cracker

```bash
# Downloads
https://github.com/lmammino/jwt-cracker

# Commands
jwt-cracker "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiYWRtaW4iOnRydWV9.TJVA95OrM7E2cBab30RMHrHDcEfxjoYZgeFONFh7HgQ" "abcdefghijklmnopqrstuwxyz" 6
```

### AES Encrypt/Decrypt (Python)

```python3
from Crypto.Cipher import AES
from base64 import b64decode
from base64 import b64encode

key = b64decode(b"2OVIftcUZNGlIyb9ezz+8fNU6eScakdfrtJaiHz25Mw=")
iv = b64decode(b"ff6XdYMDM7e5K23RrcsFZQ==")
while True:
	options = input("[+] Enter (1 - Encrypt, 2 - Decrypt) : ")
	print()
	if options == "1":
		print("====Encrypting====")
		texts = input("Enter Text : ").encode()
		aes = AES.new(key, AES.MODE_CBC, iv)
		print(b64encode(aes.encrypt(texts+b"\0"*(16-len(texts)))))
	else:
		print("====Decrypting====")
		texts = input("Enter Encrypted : ").encode()
		aes = AES.new(key, AES.MODE_CBC, iv)
		decoded = b64decode(texts)
		decrypted = aes.decrypt(decoded)
		print(decrypted.decode())
	print()
```

### Cipher/Encode/Hash

1. **Old Krytan Language (Guild Wars2)**

![](https://github.com/H0j3n/EzpzCTF/blob/main/src/Pasted%20image%2020210610103129.png)

2. **Predator Language**

![](https://github.com/H0j3n/EzpzCTF/blob/main/src/Pasted%20image%2020210610103153.png)

3. **Malbolge**

Malbolge is a public domain esoteric programming language invented by Ben Olmstead in 1998, named after the eighth circle of hell in Dante's Inferno, the Malebolge. It was specifically designed to be almost impossible to use, via a counter-intuitive 'crazy operation', base-three arithmetic, and self-altering code.

Link : [http://malbolge.doleczek.pl/](http://malbolge.doleczek.pl/)

```bash
# Examples
('&%:9]!~}|z2Vxwv-,POqponl$Hjig%eB@@>}=<M:9wv6WsU2T|nm-,jcL(I&%$#"
`CB]V?Tx<uVtT`Rpo3NlF.Jh++FdbCBA@?]!~|4XzyTT43Qsqq(Lnmkj"Fhg${z@>
```

4. **Rot13**

```bash
# Example
JFJAM{j@3$@y_j!wo3y}
```

5. **Base64**

```bash
# Example
aGVsbG8=
```

5. **Base85**

```bash
# Example
87cURD]i,"Ebo7
```

6. **MD5**

```bash
# Example
2bafea54caf6f8d718be0f234793a9be

# Bruteforce with salt (Python3)
import itertools
import hashlib
import string

pwd_hash = '2bafea54caf6f8d718be0f234793a9be'
salt = b'04532@#!!'

for key in itertools.product(string.ascii_lowercase,repeat=5):
    key = ''.join(key).encode()
    if hashlib.md5(key+salt).hexdigest() == pwd_hash:
        print('key =',key.decode())
        break
```

7. **Fernet**

Link : [https://asecuritysite.com/encryption/ferdecode](https://asecuritysite.com/encryption/ferdecode)

![](https://github.com/H0j3n/EzpzCTF/blob/main/src/Pasted%20image%2020210610103707.png)

8. **Zodiac Killer**

Link :
- [https://www.dcode.fr/zodiac-killer-cipher](https://www.dcode.fr/zodiac-killer-cipher)
- [http://www.zodiackillerciphers.com/](http://www.zodiackillerciphers.com/)
- [https://github.com/H0j3n/Zodiac-Z340](https://github.com/H0j3n/Zodiac-Z340)

![](https://github.com/H0j3n/EzpzCTF/blob/main/src/Pasted%20image%2020210610103852.png)

9. **Reverse Fuck**

Link : [https://www.dcode.fr/reversefuck-language](https://www.dcode.fr/reversefuck-language)

```bash
# Example
----------]<-<---<-------<---------->>>>+[<<<<,>+++,<-----------,+++++++++++,-,>>--,<---------------,<,-----------------,+++++++++++++++++,-------------,-,++++++++++++++,>++++++++++++,<----------------,++++++++++++++++++,--------,
```

10. **Brain Fuck**

Link : [https://www.dcode.fr/brainfuck-language](https://www.dcode.fr/brainfuck-language)

```bash
# Example
++++++++++[>+>+++>+++++++>++++++++++<<<<-]>>>>.<---.>+++++++++++.-----------.+.<<++.>-.>+++++++++++++.-----------------.++++++++.+++++.--------.+++++++++++++++.------------------.++++++++.
```

11. **Ascii Art Encoder**

Link : [https://pictureworthsthousandwords.appspot.com/](https://pictureworthsthousandwords.appspot.com/)

12. **IMB Barcodes**

Link : [http://bobcodes.weebly.com/imb.html](http://bobcodes.weebly.com/imb.html)

![](https://github.com/H0j3n/EzpzCTF/blob/main/src/Pasted%20image%2020210610104150.png)

13. **Book Cipher**

You got book.txt and got code.txt . Use this

Link : [https://www.dcode.fr/book-cipher](https://www.dcode.fr/book-cipher)

13. **Wingdingsr**

Link : [https://lingojam.com/WingdingsTranslator](https://lingojam.com/WingdingsTranslator)

```bash
♐●♋♑❀♏📁🖮🖲📂♍♏⌛🖰♐🖮📂🖰📂🖰🖰♍📁🗏🖮🖰♌📂♍📁♋🗏♌♎♍🖲♏❝
```

14. **Emoji MorseCode**

Link : [https://cryptii.com/pipes/morse-code-with-emojis](https://cryptii.com/pipes/morse-code-with-emojis)
```bash
😘😘 ✋ 😘😍😘😘 😍😍😍 😘😘😘😍 😘 ✋ 😍😘😍😍 😍😍😍 😘😘😍
```

15. **Decimal**

```bash
#Examples
6710111011611497108457311010211183101991235351678251559577535795685167125
* split by actual decimal numbers manually
```

16. **Octal**

```bash
#Examples
103 145 156 164 162 141 154 055 111 156 146 157 123 145 143 173 065 063 103 122 063 067 137 115 065 071 137 060 103 067 175
* Use Cyberchef
```

# Forensics

### Online Tools

```bash
https://packettotal.com/
```

### Tshark

```bash
# Install
sudo apt install tshark

# Commands
tshark -r dump.pcap
```

### Tcpdump

```bash
# Commands
tcpdump -r dump.pcap
```

### PCAP File

```bash
# DNS
- If its related to exilftration you can try check this out
	* https://blog.stalkr.net/2010/10/hacklu-ctf-challenge-9-bottle-writeup.html
	* https://github.com/yarrick/iodine
	* https://gist.github.com/SwissKid/438fbcf8a472be62ba4a412e37dc2d27
```

### GuestMount

```bash
# Install
sudo apt install libguestfs-tools -y

# Commands
sudo mkdir /mnt/vhd
guestmount --add file.vhd --inspector --ro -v /mnt/vhd
guestunmount mnt

# If windows
cd /Windows/System32/config
cp SAM SYSTEM /<localDir>
secretsdump.py -sam SAM -system SYSTEM local
```


### PCRT

```bash
# About
- Fix/Repair PNG image file

# Downloads
https://github.com/sherlly/PCRT.git

# Commands
python PCRT.py -i /pathto/output.png
```

# Reverse Engineering

### GDB 

```bash
# Install
sudo apt-get install gdb

# GEF
https://github.com/hugsy/gef

# Peda
https://github.com/longld/peda

# Commands
x/w $rbp-0x4
run auth2 < input.txt

# References
http://www.gdbtutorial.com/tutorial/how-install-gdb
https://gist.github.com/rkubik/b96c23bd8ed58333de37f2b8cd052c30
http://csapp.cs.cmu.edu/3e/docs/gdbnotes-x86-64.pdf
```

# Web

### Practices

```bash
http://websec.fr/
```

### Convert Curl to Different Language

```bash
- Go to this website https://curl.trillworks.com/
```

# Binary Exploitation

### Payload

```bash
for i in {1..50};do python3 -c "print('a' * $i)" | ./auth;done
for i in {1..50};do python -c "print('a' * $i)" | ./auth;done
for i in {1..10};do python3 -c "print('\nadmin'+('\x00' * $i)+'admin')" | ./auth2;done
for i in {1..10};do python2 -c "print('\nadmin'+('\x00' * $i)+'admin')" | ./auth2;done
echo -e "\naaaaaaaaaaaaaaa" > input.txt
```

# References
- http://www.wechall.net/challs
- https://ctftime.org/