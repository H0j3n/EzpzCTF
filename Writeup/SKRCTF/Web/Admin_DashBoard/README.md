# Web

Challenge Name : Admin Dashboard

# Solution

Opening the link will get us into this page

![](https://github.com/H0j3n/EzpzCTF/blob/main/src/Pasted%20image%2020210609235328.png)

We cant find anything actually unless if we can get a correct credentials. Thus checking with curl give us a different results.

```code
 curl -k https://URL
```

![](https://github.com/H0j3n/EzpzCTF/blob/main/src/Pasted%20image%2020210609235952.png)

This is interesting as we found different source code from the first one. So the reason why we go to `login.php` because of this one line.

```code
<script>window.location.href='login.php'</script><html>
```

So we can see that there is a few interesting file that we can look for 
- logs.php
- S3cr3t_P4g3.php

Going into `logs.php` , we can see that there is `server.log` file.

![](https://github.com/H0j3n/EzpzCTF/blob/main/src/Pasted%20image%2020210610000254.png)

Let's download the file first.

```code
curl -k https://URL/server.log --output server.log
```

There is a lot of password in here, so let's filter it to just get the password only. Please add the alias in your `.bashrc` or `.zshrc`
```bash
# Alias

# Commands
for i in $(cat server.log | grep -i '&password' | cut -d' ' -f7 | grep -i "password" | cut -d'&' -f2 | cut -d'=' -f2 | sort | uniq); do echo $i | urldecode;done
```

![](https://github.com/H0j3n/EzpzCTF/blob/main/src/Pasted%20image%2020210610001314.png)

Obviously the password should be between these:
```bash
P@$$w0rd
password
U_W1ll_N3V3R_GU355_TH15_P@55w0rD!LOL
```

Since we already done view `logs.php` , lets go check on `S3cr3t_P4g3.php`. 

![](https://github.com/H0j3n/EzpzCTF/blob/main/src/Pasted%20image%2020210610001515.png)

Trying with different passwords, we can successfully login with credential

```bash
admin:U_W1ll_N3V3R_GU355_TH15_P@55w0rD!LOL
```

Going into `S3cr3t_P4g3.php` again give us this.  

![](https://github.com/H0j3n/EzpzCTF/blob/main/src/Pasted%20image%2020210610001702.png)

Giving the correct password will get us the flag!

# Flag

![](https://github.com/H0j3n/EzpzCTF/blob/main/src/Pasted%20image%2020210610001746.png)

