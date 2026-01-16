from functions import get_todos, write_todos # this is local modules we created
# import functions - this is another way to get functions from function module
import time # these are standard modules created by python developers itself
now= time.strftime("%b %d %Y %H:%M:%S")
print("It is", now)
#print(help(write_todos))  - this is used to print the doc text we arite for the definition of write_todos() function




while True:
    user_action=input( 'type add, show,edit,complete or exit:')

    if user_action.startswith('add'):   # check if user_action is 'add'
        todo= user_action[4:] + '\n'  # this displays the string from the 4th position in the list


        todos=get_todos() # this is similar to get_todos("todos.txt") but we already assign this file to filepath variable in  user defined function
        todos.append(todo)


        write_todos(todos)  # if  we use the second way of importing the function, we need to replace this line of code by functions.write_todos()


    elif user_action.startswith('show'):


        todos=get_todos()


        for index,items in enumerate(todos):
            items= items.strip('\n')
            print(f"{index+1}.{items}")
    elif user_action.startswith('edit'):
        try:
            number=int(user_action[5:])
            number=number-1

            todos=get_todos()

            new_todo=input('Enter a new todo:')
            todos[number]=new_todo + '\n'

            write_todos(todos)
        except ValueError:
            print('Your command is not valid. Please enter a valid number as input if your command is EDIT')
            continue

    elif user_action.startswith('complete'):
        try:
            number= int(user_action[9:])

            todos=get_todos()

            index = number-1
            todo_to_remove=todos[index]
            todos.pop(index)

            write_todos(todos)

            message= f"The todo {todo_to_remove} is completed."
            print(message)
        except IndexError:
            print('The value you entered is out of range.')
            continue
    elif user_action.startswith('exit'):
        break
print('bye...')