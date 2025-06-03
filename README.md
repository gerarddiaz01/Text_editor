# Text Editor Project 🧾

This project is a simple text editor GUI built using Python’s tkinter library. It allowed me to practice structuring a real application with menus, file handling, widgets, and scrollable text — all while learning event-driven design from the ground up.

This project represents one of my first fully functional desktop applications. I used AI as a learning companion — not for copy/paste code, but as a way to understand tkinter, solve integration problems, and deepen my ability to reason through GUI logic.

---

## Learning Context 📚

This app was created in April 2025, during my 3rd month learning Python. It was my first solo GUI project combining state, file logic, and user interaction.

---

## How to Run the Application 🚀

1. **Install Python**:
   - Ensure you have Python installed on your machine.

2. **Run the Script**:
   - Execute the script by running the following command in your terminal (make sure to be in the right folder):
     ```
     python main.py
     ```

---

## Features ✨

1. **Text Editing**:
   - A multi-line text area where users can write and edit text.
   - Supports basic text operations like typing, deleting, and navigating.

2. **File Operations**:
   - Open and save `.txt` files using the `tkinter.filedialog` module.

3. **Menu Bar**:
   - A simple menu bar with options for "Open", "Save", and "Exit".

4. **Scrollbars**:
   - A vertical scrollbar for navigating through the text area.

---

## Tools and Concepts Used 🛠️

- tkinter widgets: Text, Scrollbar, Menu, filedialog
- Python file handling (with open() for read/write)
- GUI layout and window management
- AI-assisted research: used AI to understand syntax, find bugs, and get unstuck — while still applying solutions myself

---

## Challenges Encountered and Solutions 🧩

### Challenge 1: GUI + File Dialog Integration
At first, I didn’t know how to connect menu commands to opening/saving files. I learned how to use tkinter.filedialog to open file pickers and bind their output into the app.

### Challenge 2: Scrollbar Linking
I struggled to make the scrollbar actually scroll the text area. Eventually learned that I had to use yscrollcommand and command to connect both widgets properly.

### Challenge 3: Organizing Code Cleanly
I initially had everything in one giant main() function. I then refactored to break functionality into smaller helper functions (file operations, UI init, bindings), improving readability and reusability.

### Challenge 4: Learning Tkinter’s Ecosystem
tkinter felt foreign at first, especially its event loop and widget system. Instead of Googling every method, I leaned into AI-assisted exploration — asking why things worked, not just how.

---

## What I Learned 👨‍🎓

- How to build a functioning text editor UI from scratch
- The difference between imperative and event-driven GUI logic
- How to use filedialog and file I/O to work with real text files
- Best practices for linking Scrollbar and Text widgets
- How to organize code modularly as complexity increases
- This was a major milestone in learning how to design desktop applications in Python.

---

## Conclusion 📝

This project was a valuable learning experience that allowed me to explore GUI development with `tkinter`. By combining programming concepts, file handling, and user interface design, I created a simple yet functional text editor. The use of AI as a learning tool helped me overcome challenges and accelerate my understanding of `tkinter`.

This project demonstrates my progression as a programming student and my ability to apply new knowledge to build practical applications. Feel free to explore, use, and contribute to this project!
