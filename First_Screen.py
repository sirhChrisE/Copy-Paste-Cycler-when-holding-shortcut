import tkinter as tk
from tkinter import filedialog
import os

class FirstScreen:
    def __init__(self, root):
        self.root = root
        self.root.title("Paste Cycler")
        self.root.geometry("260x150")

        self.label = tk.Label(self.root, text="Welcome", font=("Calibri", 14))
        self.label.pack(pady=20)

        self.choose_file_button = tk.Button(self.root, text="Choose Spreadsheet to Start", font=("Calibri", 12), command=self.on_choose_file_click)
        self.choose_file_button.pack()

        self.completed = False  # Flag to track completion of the first screen

    def on_choose_file_click(self):
        file_path = filedialog.askopenfilename(filetypes=[("Excel Files", "*.xlsx"), ("CSV Files", "*.csv"), ("All Files", "*.*")])
        if file_path:
            self.root.destroy()  # Close the first screen
            self.completed = True
            main(file_path)  # Start the main GUI with the selected file path

class MyGUI:
    def __init__(self, root, file_path):
        self.root = root
        self.root.title("Paste Cycler")
        self.root.geometry("260x400")

        # Use the file path passed from the first screen
        self.file_path = file_path

        # Rest of your main GUI code...

def main(file_path=None):
    if file_path is None:
        root = tk.Tk()
        first_screen = FirstScreen(root)
        root.wait_window(first_screen.root)

        if first_screen.completed:
            main(tk.Tk(), file_path=first_screen.file_path)
    else:
        root = tk.Tk()
        gui = MyGUI(root, file_path)
        root.mainloop()

if __name__ == "__main__":
    main()
