# Library-Management-System-
 In this system each member is provided with a member  code and all the records are maintained in a table along with the member’s code.  Any information can be accessed according to member-code anytime from the  table and also at the time of issuing books

# 📚 Library Management System

A Python and MySQL-based CLI application built to automate library record keeping, book issuing, returning, and inventory tracking. Developed as a Class XII Computer Science project.

---

## 📌 Project Overview

Maintaining library records manually can be tedious and prone to errors. This project provides a computerized backend system using **MySQL** and a user-friendly frontend command-line interface written in **Python**.

It allows librarians to:
* Manage book inventory (donate/add new books or remove old ones).
* Issue books to students and store issue logs[cite: 1].
* Track returned books and store transaction dates[cite: 1].
* Display full catalogs and system records[cite: 1].

---

## 🛠️ System Requirements & Prerequisites

* **Operating System:** Windows 7 / 10 / 11[cite: 1]
* **Python:** Python 3.7 or higher[cite: 1]
* **Database:** MySQL Server[cite: 1]
* **Python Driver:** `mysql-connector-python`[cite: 1]

---

## 🗄️ Database Schema

The database `library` consists of 3 primary tables[cite: 1]:

1. **`books`**: Stores book catalog details (`bookname`, `authorname`, `bookcode`, `total`)[cite: 1].
2. **`issue`**: Stores issue records (`bookname`, `bookcode`, `studentname`, `issuedate`)[cite: 1].
3. **`return`**: Stores return records (`bookname`, `bookcode`, `studentname`, `returndate`)[cite: 1].

---

## 🚀 Setup & Installation

### 1. Clone the Repository
```bash
git clone [https://github.com/your-username/library-management-system.git](https://github.com/your-username/library-management-system.git)
cd library-management-system
```

### 2. Set Up the MySQL Database
Open your MySQL Command Line Client or MySQL Workbench and run the contents of schema.sql:

### 3. Install Python Dependencies
Install the required MySQL connector module:

```bash
pip install mysql-connector-python
```

### 4. Update Database Credentials
In main.py, update the MySQL connection string with your local MySQL password:
```python
con = mysql.connector.connect(
    host='localhost',
    user='root',
    password='YOUR_MYSQL_PASSWORD',
    database='library'
)
```
### 5. 💻 How to Run
Execute the main script using Python:
```bash
python main.py
```
Default Password: nvps

#### 📁 Repository Structure
```text

├── main.py        # Main Python program (CLI Menu & Logic)
├── schema.sql     # MySQL database initialization script
└── README.md      # Project documentation
```
