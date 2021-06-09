# Cryptography

Challenge Name : Beginner Reverse

# Solution

Download the c program file first. We will see this inside.

```c
#include <stdio.h>

int main () {
	char password[16];
	printf("Enter password: ");
	scanf("%15s",password);
	if (strcmp(password, "P@ssw0rd1337") == 0)
	{
		printf("Welcome admin!\nFlag: SKR{%s}",password);
	}else{
		printf("Login failed!");
	}
}#  
```

It receive one input and store into `password` variable. The password will then be comparing with "P@ssw0rd1337".

If its correct it will welcome us with the flag. If its wrong it will say Login Failed.

Also the password itself is the flag which in the format of SKR{password}.

We can try compile it and run to get the flag itself. To compile it:
```bash
gcc beginner.c -o beginner
chmod +x beginner
./beginner
```

Then enter the correct password.

# Flag

![](https://github.com/H0j3n/EzpzCTF/blob/main/src/Pasted%20image%2020210609131341.png)

