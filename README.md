# HTML Portfolio Generator (Python)

## 📌 What is this project?

This is a Python-based desktop application that allows users (especially freelancers or developers) to generate a personalized HTML portfolio file. It is built using **Tkinter** for the user interface and **Jinja2** for templating.

---

## 🧠 What does it do?

The program collects user input such as:
- Name
- Project title
- Project description
- Preferred color (hex)
- Job roles
- Profile image
- Main project image

It then uses a **Jinja2 HTML template** to dynamically fill in the data and generate a styled `.html` portfolio file.

---

## 🛠️ Tech stack used

- `tkinter` – for the GUI interface
- `jinja2` – for HTML templating
- `os` and `filedialog` – for handling file paths and image uploads

---

## 📂 Features

- Interactive form to enter portfolio details
- Upload user image and project image
- Supports custom color themes via hexadecimal input
- Automatically formats job roles
- Generates an HTML portfolio and saves it as:  
