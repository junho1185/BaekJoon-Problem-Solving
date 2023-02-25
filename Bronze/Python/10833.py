from sys import stdin

number_of_schools = int(stdin.readline())

number_of_remaining_apples = 0

for i in range(number_of_schools):
    number_of_students, apples = map(int, stdin.readline().split())
    apples_per_student = int(apples/number_of_students)
    number_of_remaining_apples += apples - (apples_per_student*number_of_students)

print(number_of_remaining_apples)