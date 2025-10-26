---

# SLMCTS – Loan Management System (Web-Based)

A web-based **Loan Management System** built with Flask and SQLAlchemy.
This system allows users to sign up, log in, and manage loan-related operations.

---

## Project Setup Guide

Follow the steps below to set up and run the project on your local machine.

---

### 1. Fork the Repository

1. Go to the repository page on GitHub.
2. Click **"Fork"** at the top right to create your own copy under your account.

---

### 2. Clone the Repository

You can clone the project in two ways:

#### Option A – Using Git (Recommended)

```bash
git clone https://github.com/<your-username>/SLMCTS.git
```

#### Option B – Using GitHub Desktop

1. Open **GitHub Desktop**.
2. Click **File > Clone Repository**.
3. Select the forked repository from your GitHub account.
4. Choose a local folder to save the project.
5. Click **Clone**.

---

### 3. Open the Project in Visual Studio Code

If you used GitHub Desktop, click **“Open in Visual Studio Code”** after cloning.
Otherwise, open the folder manually:

```bash
cd SLMCTS
code .
```

---

### 4. Create and Activate a Virtual Environment

**Windows:**

```bash
python -m venv venv
venv\Scripts\activate
```

**Mac/Linux:**

```bash
python3 -m venv venv
source venv/bin/activate
```

---

### 5. Install Dependencies

Run the following command in your VS Code terminal:

```bash
pip install -r requirements.txt
```

---

### 6. Set Up the Database

The project uses **SQLAlchemy** for ORM.
Check your database configuration in `config.py` or `.env`.

To initialize the database:

```bash
flask db upgrade
```

or manually:

```bash
python
>>> from app import db
>>> db.create_all()
>>> exit()
```

---

### 7. Run the Application

Start the development server:

```bash
flask run
```

or

```bash
python app.py
```

Then open your browser and go to:

```
http://127.0.0.1:5000/
```

---

## Commit Guidelines

For every commit, include a message describing your changes and **add your name (Shalom)**.

Example:

```bash
git add .
git commit -m "Added login and signup modals with SQLAlchemy integration - Shalom"
git push
```

---

## Notes

* If you encounter issues, consult your group or ask in the GC.
* Ensure your environment is activated before installing dependencies or running the app.

---

