#include <stdio.h>
int main(void) {

	int arr[31] = { 0, };
	int i, n;

	for (i = 0; i < 28; i++) {
		scanf("%d", &n);
		arr[n] = 1;
	}

	for (i = 1; i <= 30; i++) {
		if (arr[i] != 1)
			printf("%d\n", i);
	}

	return 0;
}