A Python-based To-Do List application with both Command Line Interface (CLI) and Graphical User Interface (GUI). The project allows users to add, edit, view, and complete tasks while storing data in a text file. It demonstrates Python concepts such as file handling, modular programming, and GUI development using FreeSimpleGUI.


📝 Python To-Do List Application (CLI + GUI)
📌 Project Overview

This project is a Python-based To-Do List Manager that allows users to create, view, edit, and complete tasks. The application is implemented in two versions:

Command Line Interface (CLI) version for terminal interaction

Graphical User Interface (GUI) version built using FreeSimpleGUI

All tasks are stored in a text file so that the to-do list persists even after the program is closed.

🎯 Project Objectives

Build a practical task management application using Python

Practice file handling, functions, and modular programming

Implement both CLI and GUI interfaces

Demonstrate basic software structure and code reusability

🛠️ Technologies Used
| Technology           | Purpose                   |
| -------------------- | ------------------------- |
| Python               | Core programming language |
| FreeSimpleGUI        | GUI development           |
| Text File Storage    | Persistent task storage   |
| Jupyter / Python IDE | Development environment   |

📂 Project Structure
project-folder
│
├── functions.py
├── todo.py
├── to-do-gui.py
├── todos.txt
└── README.md

File Descriptions

functions.py

Contains reusable functions for reading and writing todo tasks from a text file.

get_todos() → Reads tasks from the file

write_todos() → Saves updated tasks to the file

These functions handle file operations for the application. 

todo.py

Implements the command-line version of the To-Do application.

Users can type commands such as:

add → Add a new task

show → Display all tasks

edit → Modify an existing task

complete → Mark a task as completed

exit → Close the program

The program continuously runs in a loop and processes user input to manage tasks.

to-do-gui.py

Implements a Graphical User Interface version using FreeSimpleGUI.

The GUI includes:

Input box for entering tasks

Listbox showing all current tasks

Buttons to add and edit tasks

Dynamic updates to the task list

This version provides a more user-friendly interface for managing the to-do list.

⚙️ Features

✔ Add new tasks
✔ Display all tasks
✔ Edit existing tasks
✔ Mark tasks as completed
✔ Persistent storage using a text file
✔ GUI-based task management
✔ Modular code structure

▶️ How to Run the Project
1️⃣ Install Python

Download and install Python from:
https://www.python.org

2️⃣ Install FreeSimpleGUI
pip install FreeSimpleGUI

3️⃣ Run the CLI Version
python todo.py

4️⃣ Run the GUI Version
python to-do-gui.py
💡 Example Commands (CLI Version)
type add, show, edit, complete or exit

Example:

add Study Python
show
edit 1
complete 2
exit
🚀 Skills Demonstrated

This project demonstrates important Python programming concepts, including:

File handling

Modular programming

User input handling

Exception handling

GUI development

Data persistence

📌 Future Improvements

Potential enhancements for the project:

Add task deadlines

Add task priority levels

Store tasks using a database (SQLite)

Add task completion tracking

Create a web version using Flask or Streamlit

⭐ If you like this project, feel free to star the repository.
