# Installation Guide

Follow the steps below to set up and run the project locally.

---

## Prerequisites

- Python 3 installed on your system
- Terminal / command-line access

---

## Steps

### 1. Navigate to the project directory

```bash
cd path/to/project
```

### 2. Create a virtual environment

```bash
python3 -m venv .venv
```

### 3. Activate the virtual environment

```bash
. .venv/bin/activate
```

> On Windows, use `.venv\Scripts\activate` instead.

### 4. Install dependencies

```bash
pip3 install flask
```

### 5. Run the application

```bash
flask --app <filename> run
```

Replace `<filename>` with the name of your main application file (e.g., `app` for `app.py`).

---

Once the server starts, it will be available at `http://127.0.0.1:5000` by default.
