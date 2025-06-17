import tkinter as tk
from tkinter import messagebox, filedialog
from jinja2 import Environment , FileSystemLoader
import os
#interface
root = tk.Tk()
root.title("HTML portfolio generator")

#Entries: [client name, Project name, description]
w = 50

tk.Label(root, text="Enter your name:", width= w).grid(row=0,column=0)
name_entry = tk.Entry(root, width= w)
name_entry.grid(row=0, column=2)

tk.Label(root, text="Enter your project name:", width= w).grid(row=1,column=0)
project_entry = tk.Entry(root, width= w)
project_entry.grid(row=1, column=2)

tk.Label(root, text="Enter your project description (copy and paste it here):", width= w).grid(row=2,column=0)
discription_entry = tk.Entry(root, width= w)
discription_entry.grid(row=2, column=2)

tk.Label(root, text="Enter your website's prefered color (hexadecimal):", width= w).grid(row=3,column=0)
color_entry = tk.Entry(root, width= w)
color_entry.grid(row=3, column=2)

tk.Label(root, text="Enter your Jobs (seperate them by commas):", width= w).grid(row=4,column=0)
Jobs_entry = tk.Entry(root, width= w)
Jobs_entry.grid(row=4, column=2)

#Image Entry: [client image, main project image, other project images]

#the function for the file dialog
user_img = None
main_img = None
def file_upload(type):
    global user_img, main_img, other_img
    path = filedialog.askopenfilename(
        title="Select a file",
        filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.gif;*.bmp")]
        )
    if type == "user":
        user_img = path
    elif type == "main":
        main_img = path
def submit():
    global name, project, description, Jobs

    name = name_entry.get()
    project = project_entry.get()
    Jobs = Jobs_entry.get().split(",")
    Jobs = " | ".join(x.strip().title() for x in Jobs)
    description = discription_entry.get()
    color = color_entry.get()
    if color == "":
        color = None
    


    if not user_img or not main_img:
        messagebox.showerror("Error", "You must upload all the images")
        return
    else:
        obj = {
            "name" : name,
            "project" : project,
            "description" : description,
            "jobs" : Jobs,
            "color_": color,
            "user_img" : user_img,
            "main_img" : main_img,
        }
        env = Environment(loader=FileSystemLoader("."))
        template = env.get_template("template.html")
        html = template.render(obj)
        with open(f"portfolio_{name}.html", "w", encoding="utf-8") as file:
            file.write(html)
        messagebox.showinfo("Success", "Portfolio created!")
#the buttons:
tk.Label(root, text="upload your user image file", width=w).grid(row=5, column=0)
tk.Button(root, text="upload", command= lambda: file_upload("user")).grid(row=5, column=2)

tk.Label(root, text="upload your project's main image file", width=w).grid(row=6, column=0)
tk.Button(root, text="upload", command= lambda: file_upload("main")).grid(row=6, column=2)

tk.Button(root, text="submit", command=submit).grid(row=8, column=1)

root.mainloop()