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
}