#include <stdio.h>
int main(void) {

	int sum = 0;
	int i, n;

	for (i = 0; i < 5; i++) {
		scanf("%d", &n);
		sum += (n * n);
	}

	printf("%d", sum % 10);

	return 0;
}