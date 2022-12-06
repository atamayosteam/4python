my_file = open('todo.txt', 'a')

while True:
    # print('your todos are:')
    # print(todos)


    x = input(" What todo would you like to add? ")
    # todos.append(x)
    my_file.write(x)
