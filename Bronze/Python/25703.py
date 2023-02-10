n = int(input())
print("int a;")
print("int *ptr = &a;")
for i in range(n-1):
    print("int ", end='')
    if i == 0:
        print("**ptr2 = &ptr;")
        continue
    for j in range(i+2):
        print("*", end='')
    print(f"ptr{i+2} = &ptr{i+1};")