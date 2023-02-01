#include <stdio.h>
int main(void) {

	int N, M, i, j;
	int mat_a[100][100], mat_b[100][100];

	scanf("%d %d", &N, &M);

	for (i = 0; i < N; i++) {
		for (j = 0; j < M; j++) {
			scanf("%d", &mat_a[i][j]);
		}
	}
	for (i = 0; i < N; i++) {
		for (j = 0; j < M; j++) {
			scanf("%d", &mat_b[i][j]);
		}
	}
	for (i = 0; i < N; i++) {
		for (j = 0; j < M; j++) {
			printf("%d ", mat_a[i][j] + mat_b[i][j]);
		}
		printf("\n");
	}

	return 0;
}