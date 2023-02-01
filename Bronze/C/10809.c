#include <stdio.h>
#include <string.h>
int main(void) {

	int arr[26];
	int i, index;

	char str[101];

	scanf("%s", str);

	for (i = 0; i < 26; i++) {
		arr[i] = -1;
	}

	for (i = 0; i < strlen(str); i++) {
		index = str[i] - 'a';

		if (arr[index] == -1) {
			arr[index] = i;
		}
	}

	for (i = 0; i < 26; i++) {
		printf("%d ", arr[i]);
	}

	return 0;
}