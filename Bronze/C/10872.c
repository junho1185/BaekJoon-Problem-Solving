#include <stdio.h>
int main(void) {

	long int facto = 1;
	int N, i;

	scanf("%d", &N);

	for (i = 0; i < N; i++) {
		facto *= (N - i);
	}

	printf("%d", facto);

	return 0;
}