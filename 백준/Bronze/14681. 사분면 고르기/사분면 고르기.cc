#include <stdio.h>
int main(void)
{
	int x, y;
	scanf("%d", &x);
	scanf("%d", &y);
	if (x > 0)
	{
		if (y > 0)
			printf("1\n");
		if (y < 0)
			printf("4\n");
	}
	if (x < 0)
	{
		if (y > 0)
			printf("2\n");
		if (y < 0)
			printf("3\n");
	}

	return 0;
}