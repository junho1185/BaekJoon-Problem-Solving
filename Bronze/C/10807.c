#include <stdio.h>
int main(void) {

	int arr[100];
	int N, search, cnt = 0, i;

	scanf("%d", &N);
	
	for (i = 0; i < N; i++) {
		scanf("%d", &arr[i]);
	}

	scanf("%d", &search);

	for (i = 0; i < N; i++) {
		if (arr[i] == search)
			cnt++;
	}

	printf("%d", cnt);

	return 0;
}