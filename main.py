import tkinter as tk
from tkinter import filedialog

def open_file():
    '''Open a file'''
    input_file_path  = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
    if input_file_path:
        with open(input_file_path , "r") as file:
            content = file.read()
            input_text.delete('1.0', tk.END)
            input_text.insert("1.0", content)

def save_file():
    '''Save a file'''
    output_file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
    if output_file_path:
        with open(output_file_path, "w") as file:
            file.write(input_text.get("1.0", "end-1c"))

root = tk.Tk()
root.title("Text Editor")

# We set up a menu
menu_bar = tk.Menu(root)
root.config(menu=menu_bar)
file_menu = tk.Menu(menu_bar, tearoff=0) # Creating a submenu that drops down
file_menu.add_command(label="Open", command=open_file) # We access to the functions to open and save files
file_menu.add_command(label="Save", command=save_file)
file_menu.add_separator() # Adds a horizontal line to visually separate groups of menu items
file_menu.add_command(label="Exit", command=root.quit)
menu_bar.add_cascade(label="File", menu=file_menu) # Adds file_menu as a dropdown menu under menu_bar

# We create the text widget with a scrollbar
scrollbar = tk.Scrollbar(root)
scrollbar.pack(side="right", fill="y")
input_text = tk.Text(root, yscrollcommand=scrollbar.set, wrap="word", font=("Arial", 12))
input_text.pack(side="left", expand=True, fill="both") # It expands when the window is redimensioned
scrollbar.config(command=input_text.yview)

root.mainloop() # Keep the application running