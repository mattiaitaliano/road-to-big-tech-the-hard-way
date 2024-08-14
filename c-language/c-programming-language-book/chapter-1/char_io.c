#include <stdio.h>

int main()
{
	int c;
	int count;

	c = getchar();
	while (c != EOF) {
		putchar(c);
		c = getchar();
		count++;
	}

	printf("Number of char counter: %d\n", count);

	printf("EOF: %d\n", EOF);
	printf("C: %d\n", c);

	return 0;
}
