FILEPATH ="todos.txt"

def get_todos(filepath=FILEPATH):
    """Read a text file and return a list of todo items"""   # this is written to know about the function of our user defined function using help function
    with open(filepath, 'r') as file_local:
        todos_local= file_local.readlines()
    return todos_local

#print(help(get_todos)) -  this is used to print the documentation text for write todos function

def write_todos(todos_arg,filepath=FILEPATH): # the non-default parameter should write first before default parameter
    """write the todo items list in the text file"""
    with open(filepath, 'w') as file_2:
        file_2.writelines(todos_arg)