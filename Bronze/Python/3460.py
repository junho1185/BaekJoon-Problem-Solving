from sys import stdin

def decimal_to_binary(decimal):
    binary = ""
    while decimal > 0:
        binary = str(decimal % 2) + binary
        decimal //= 2
    return binary

def reverse_string(input_string):
    return input_string[::-1]

T = int(stdin.readline())

for i in range(T):
    decimal_number = int(stdin.readline())

    binary_number = decimal_to_binary(decimal_number)

    reversed_binary = reverse_string(binary_number)

    binary_len = len(reversed_binary)

    for i in range(binary_len):
        if(reversed_binary[i] == '1'):
            print(i, end=' ')
    print()