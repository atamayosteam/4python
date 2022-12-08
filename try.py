
# age = int(input('Enter your age: '))
try:
    age = int(input('Enter your age: '))

    faveNum = int(input('What is your favorite number: '))

    if age <= 21:
         print('You are not allowed to enter, you are too young.')
    else:
        print('Welcome, you are old enough.')

    print("Fun Fact! Your age divided by your favorite number is: " , age / faveNum)
except ValueError or TypeError:
    print("please input a number")
except ZeroDivisionError:
    print("Plese do not enter the number zero")
finally:
    print("congrats no ID-10-T errors! ")

# if age <= 21:
#   print('You are not allowed to enter, you are too young.')
# else:
#   print('Welcome, you are old enough.')

# try:
#     print("Fun Fact! Your age divided by your favorite number is: " , age / faveNum)
# except:
#     print('no number zero plz')

