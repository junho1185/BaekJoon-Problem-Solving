#include <stdio.h>

int main(void) {

	int a, b, t, i, j;
	int server;

	scanf("%d", &t);
	
	for (i = 0; i < t; i++) {
		scanf("%d %d", &a, &b);
		server = a % 10;
		for (j = 1; j < b; j++) {
			server = (server * a) % 10;
		}
		if (server != 0)
			printf("%d\n", server);
		else
			printf("10\n");
	}

	return 0;
}