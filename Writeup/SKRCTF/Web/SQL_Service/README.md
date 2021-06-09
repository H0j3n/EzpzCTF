# Web

Challenge Name : SQL Service

# Solution

Opening the link will get us into this page

![](https://github.com/H0j3n/EzpzCTF/blob/main/src/Pasted%20image%2020210609154455.png)

There is a login page. 

![](https://github.com/H0j3n/EzpzCTF/blob/main/src/Pasted%20image%2020210609155033.png)

We can try with simple SQL Injection payload that can be found in here [https://github.com/payloadbox/sql-injection-payload-list](https://github.com/payloadbox/sql-injection-payload-list)

```code
# Payload
' or ''&'
```

We manage to get in and get the flag!

# Flag

![](https://github.com/H0j3n/EzpzCTF/blob/main/src/Pasted%20image%2020210609154914.png)






