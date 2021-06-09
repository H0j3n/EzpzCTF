# Web

Challenge Name : Juggling Clown

# Solution

Opening the link will get us into this page

![](https://github.com/H0j3n/EzpzCTF/blob/main/src/Pasted%20image%2020210609155303.png)

It receive input from us. But since the challenge name is juggling it must has related with `type juggling`, or `type coercion`.

You can read more in here [https://medium.com/swlh/php-type-juggling-vulnerabilities-3e28c4ed5c09](https://medium.com/swlh/php-type-juggling-vulnerabilities-3e28c4ed5c09)

Instead of comparing with string let's make it comparing with an array. 

```
/index.php?answer[]=test
```

# Flag

![](https://github.com/H0j3n/EzpzCTF/blob/main/src/Pasted%20image%2020210609155510.png)
