#include <stdio.h>
int main(void) {

	int a, b, result;

	scanf("%d %d", &a, &b);

	result = (a > b ? (a - b) : (b - a));

	printf("%d", result);

	return 0;
}