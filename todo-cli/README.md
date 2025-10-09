# 📝 To-Do CLI — Command Line Task Manager

A minimal command-line to-do list application built to practice proper Python project structure, module separation, dependency management, and Git workflow.

---

## 🚀 Features

- Add a new task ✅  
- List all tasks ✅  
- Delete a task ✅  
- Tasks are stored locally using a JSON file ✅

---

## 📂 Project Structure
todo-cli/
├── README.md
├── requirements.txt
├── .gitignore
└── src/
├── main.py # Entry point of the application
├── todo.py # Business logic for task management
└── storage.py # Handles loading/saving data


---

## 🛠 Setup Environment

```bash
# Create and activate virtual environment

# Conda (recommended)
conda create -n todo-cli python=3.9 -y
conda activate todo-cli

# OR using venv
python3 -m venv venv
source venv/bin/activate      # Windows: venv\Scripts\activate

