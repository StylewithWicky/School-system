 🏫 School System – Object-Relational Mapping (ORM) with Python & SQLite

This project is a simple school management system that demonstrates Object-Relational Mapping (ORM) using Python and SQLite. It models Teachers, Students, Classes, and Enrollments, allowing interactions between them such as enrolling students in classes and assigning teachers.

---

## 📁 Project Structure

School-system/
├── lib/
│ ├── helpers.py
│ ├── test_debug.py
│ └── models/
│ ├── init.py
│ ├── student.py
│ ├── Teacher.py
│ ├── SchoolClass.py
│ └── enrolment.py
├── school.db
└── README.md

yaml
Copy
Edit

---

## 🚀 Features

- Create and save `Student`, `Teacher`, and `SchoolClass` records.
- Enroll students into classes through the `Enrollment` model.
- Retrieve:
  - All classes for a given student.
  - All students in a given class.
  - All classes taught by a teacher.

---

## 🧠 Technologies Used

- Python 3.12
- SQLite
- Pytest (for testing)

---

## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/school-system.git
cd school-system

