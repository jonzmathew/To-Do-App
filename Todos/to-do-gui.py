import functions
import FreeSimpleGUI as sg



label= sg.Text("Type in a To-Do")
input_box=sg.InputText(tooltip="Enter a To-Do", key="Entered_todo") # InputText is producing a dictionary with the typed todos with a key to it
list_box=sg.Listbox(functions.get_todos(), key="list_todos",
                    enable_events=True, size=[45,10])  # Listbox is actually producing a dictionary with todos list with a key to the list
add_button= sg.Button("Add")
edit_button= sg.Button("Edit")

window=sg.Window("My To-Do App", layout=[[label],
                                         [input_box,add_button],
                                         [list_box,edit_button]],
                                         font=("Helvetica",15))

while True:
    event,value= window.read()
    print(event)
    print(value)

    match event:
        case "Add":
            todo=functions.get_todos()
            new_todo= value["Entered_todo"] + "\n" # this will add the value we entered to the dictionary with key as "Entered_todo"
            todo.append(new_todo) # added new_todo to the existing todo list
            functions.write_todos(todo)
            window["list_todos"].update(values=todo) # we are referencing listbox items and adding updated todos to the listbox

        case "Edit":
            todo_to_edit = value["list_todos"][0]  # when we click a todo in the list box,it will be located first in the list of the dictionary, so [0]
            todo_to_replace = value["Entered_todo"]

            todo=functions.get_todos()
            index=todo.index(todo_to_edit)
            todo[index]=todo_to_replace + "\n"
            functions.write_todos(todo)
            window["list_todos"].update(values=todo)

        case "list_todos":
            window["Entered_todo"].update(value=value["list_todos"][0])

        case sg.WIN_CLOSED: # this WIN_CLOSED is used to break the loop when we click the close icon in the GUI
            break

window.close()