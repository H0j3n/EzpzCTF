# Web

Challenge Name : My First XSS

# Solution

Opening the link will get us into this page

![[Pasted image 20210609145414.png]]

There is a comment section. By giving a common XSS payload will get us the flag.

```bash
# Payload
<script>alert(1)</script>
```

# Flag

![[Pasted image 20210609145629.png]]


