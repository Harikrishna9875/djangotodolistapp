# ✅ Django To-Do List App

A simple and clean To-Do List web application built using **Django**.  
Users can add tasks, mark tasks as done/undone, edit tasks, and delete tasks.

---

## 🚀 Features

- ➕ Add new tasks  
- ✏️ Edit existing tasks  
- ✔️ Mark tasks as completed  
- ❌ Mark tasks as incomplete  
- 🗑️ Delete tasks  
- 📅 Displays current date  
- 🎨 Clean Bootstrap UI  
- 📌 Separate "Completed" and "Incomplete" task sections  

---

## 📁 Project Structure

todo_main/
│── todo_main/
│── todo/
│ ├── migrations/
│ ├── templates/
│ │ ├── home.html
│ │ ├── edit_task.html
│ ├── models.py
│ ├── views.py
│ ├── urls.py
│── db.sqlite3
│── manage.py


---

## 🛠️ Installation & Setup

### 1️⃣ Clone the repository

```bash
git clone https://github.com/Harikrishna9875/todo.git
cd todo
2️⃣ Create & activate a virtual environment
python3 -m venv env
source env/bin/activate
3️⃣ Install dependencies
pip install -r requirements.txt
4️⃣ Run migrations
python3 manage.py migrate
5️⃣ Start the development server
python3 manage.py runserver
Now visit:
http://127.0.0.1:8000/
📝 How Tasks Work
Add Task
Users can add tasks using the input box on the home page.
Edit Task
Click the blue pencil button next to a task to edit it.
Mark As Done / Undone
Green ✔ button → mark task as completed
Red ❌ button → mark task as incomplete
Delete Task
Click the red trash icon to remove a task permanently.
🧩 Technologies Used
Python 3
Django 5
Bootstrap 5
SQLite3 (default Django database)

✨ Author
Harikrishna
Django Developer | Student | Tech Enthusiast
GitHub: https://github.com/Harikrishna9875
