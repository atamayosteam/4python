

grades = []

x = input('Add numbers: ')
grades.append(int(x))

x = input('Add numbers: ')
grades.append(int(x))

x = input('Add numbers: ')
grades.append(int(x))

x = input('Add numbers: ')
grades.append(int(x))

x = input('Add numbers: ')
grades.append(int(x))

x = input('Add numbers: ')
grades.append(int(x))


sum = 0

for grade in grades:
    sum = sum + grade

print(sum / len(grades))

print(grades)