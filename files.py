my_file = open("anthony.txt", "a")
#print (my_file.readlines())
print('welcome')
my_file.write ("im writing python\n")
my_file.close()
my_file = open('anthony.txt')
for line in my_file.readlines():
    print(line, end="")

   
   
   
 