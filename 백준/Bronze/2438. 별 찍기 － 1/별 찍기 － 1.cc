#include <stdio.h>
int main(void)
{
	int x;
	scanf("%d", &x);
	for (int i = 1; i <= x; i++)
	{
		for (int j = 1; j <= i;j++)
			printf("*");
		printf("\n");
	}
	return 0;
}