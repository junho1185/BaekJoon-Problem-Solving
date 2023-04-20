#include <stdio.h>

int main(void) {
	int n0, n4;
	int count = 1;
	scanf("%d", &n0);
	while (n0 != 0) {
		if ((n0 * 3) % 2 == 1) {
			n4 = (n0 - 1) / 2;
			printf("%d. odd %d\n", count, n4);
		}
		else {
			n4 = n0 / 2;
			printf("%d. even %d\n", count, n4);
		}
		count++;
		scanf("%d", &n0);
	}
}