import functions
import FreeSimpleGUI as sg

label= sg.Text("Type in a To-Do")
input_box=sg.InputText(tooltip="Enter a To-Do", key="To-do")
add_button= sg.Button("Add")

window=sg.Window("My To-Do App", layout=[[label],
                                         [input_box,add_button]],
                                         font=("Helvetica",15))

while True:
    event,value= window.read()
    print(event)
    print(value)

    match event:
        case "Add":
            todo=functions.get_todos()
            new_todo= value["To-do"] + "\n" # this will get the value from the dictionary with key as "To-do"
            todo.append(new_todo)
            functions.write_todos(todo)
        case sg.WIN_CLOSED: # this WIN_CLOSED is used to break the loop when we click the close icon in the GUI
            break

window.close()