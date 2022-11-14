s= 100
s = int(input('what is your average percentage: '))

if s >= 90:
    print('you have a A you tryhard')
elif s >= 80 and s <=89:
    print('You have a B. Pretty good')
elif s >= 70 and s <=79:
    print('you get a C. Pretty decent')
elif s >= 60 and s <= 69:
    print('you got a D. youll do better next time')
else:
    print('you failed try harder')
    
#grade level from A to D is displaye based on your average percentage