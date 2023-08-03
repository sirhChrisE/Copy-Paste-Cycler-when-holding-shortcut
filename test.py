import tkinter as tk
from tkinter import filedialog
import os
import pandas as pd
from tkinter import ttk

class TopBar:
    def __init__(self, root, on_set_shortcut_click, on_change_paste_pref_click, on_ribbon_button_click):
        self.root = root
        self.selected_ribbon_button = None  # Variable to keep track of the selected ribbon button
        self.top_bar = tk.Frame(self.root, bg='black')
        self.top_bar.pack(fill=tk.X)

        self.alpha_button = tk.Button(self.top_bar, text="Set Shortcut", bg="white", fg="black", font=("Calibri", 12), bd=2, height=2, command=on_set_shortcut_click)
        self.alpha_button.pack(side=tk.TOP, padx=0, pady=0, fill=tk.BOTH, expand=True)

        self.beta_button = tk.Button(self.top_bar, text="Change Paste Preference", bg="white", fg="black", font=("Calibri", 12), bd=2, height=2, command=on_change_paste_pref_click)
        self.beta_button.pack(side=tk.TOP, padx=0, pady=0, fill=tk.BOTH, expand=True)
###Seperator label start
        self.beta_label = tk.Label(self.top_bar, text="", bg='black', fg='white', font=("Calibri", 10))
        self.beta_label.pack(side=tk.TOP, padx=0, pady=7, fill=tk.BOTH)
###Seperator label end

        self.beta_label = tk.Label(self.top_bar, text="Select the database for use below", bg='black', fg='white', font=("Times new roman", 12), wraplength=250)
        self.beta_label.pack(side=tk.TOP, padx=0, pady=30, fill=tk.BOTH)

        
        self.beta_label = tk.Label(self.top_bar, text="", bg='black', fg='white', font=("Calibri", 10))
        self.beta_label.pack(side=tk.TOP, padx=0, pady=0, fill=tk.BOTH)

        # Frame to contain ribbon buttons and the "Foxtrot" label
        self.ribbon_frame = tk.Frame(self.top_bar, bg='black')
        self.ribbon_frame.pack(side=tk.TOP, fill=tk.BOTH)

        self.ribbon_buttons = []
        ribbon_text = ["1", "2", "3", "4", "5"]

        for text in ribbon_text:
            ribbon_button = tk.Button(self.ribbon_frame, text=text, bg="white", fg="black", font=("Calibri", 12), bd=2, height=2, command=lambda btn_text=text: on_ribbon_button_click(btn_text), highlightthickness=0)
            ribbon_button.pack(side=tk.LEFT, padx=0, pady=0, fill=tk.BOTH, expand=True)
            self.ribbon_buttons.append(ribbon_button)


        # Custom arrow image as a Unicode character
        self.arrow_image = ""

        # Arrow indicator Label widget
        self.arrow_label = tk.Label(self.root, text=self.arrow_image, bg="red", fg='yellow', font=("Calibri", 9), height=2, width=1)

        # Callback functions from MyGUI
        self.on_set_shortcut_click = on_set_shortcut_click
        self.on_change_paste_pref_click = on_change_paste_pref_click
        self.on_ribbon_button_click = on_ribbon_button_click

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
        self.root.geometry("600x400")

        self.file_path = file_path
        self.current_df = None
        self.current_column = None
        self.current_row = -1

        self.top_bar = TopBar(self.root, self.on_set_shortcut_click, self.on_change_paste_pref_click, self.on_ribbon_button_click)

        self.selected_ribbon_button = None  # Variable to keep track of the selected ribbon button

        self.selected_column = tk.StringVar()
        self.checkbuttons_frame = tk.Frame(self.root)
        self.checkbuttons_frame.pack(side=tk.TOP, fill=tk.X)

        self.treeview_frame = tk.Frame(self.root)
        self.treeview_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        self.treeview = ttk.Treeview(self.treeview_frame, show="headings")
        self.treeview.pack(fill=tk.BOTH, expand=True)

        self.arrow_image = "⇒"
        self.arrow_label = tk.Label(self.root, text=self.arrow_image, bg="red", fg='yellow', font=("Calibri", 9), height=2, width=1)

        self.create_menu()

    def create_menu(self):
            self.menu_bar = tk.Menu(self.root)
            self.root.config(menu=self.menu_bar)

            self.file_menu = tk.Menu(self.menu_bar, tearoff=0)
            self.file_menu.add_command(label="Open", command=self.on_open_file)
            self.file_menu.add_separator()
            self.file_menu.add_command(label="Exit", command=self.root.quit)
            self.menu_bar.add_cascade(label="File", menu=self.file_menu)

            self.edit_menu = tk.Menu(self.menu_bar, tearoff=0)
            self.edit_menu.add_command(label="Clear All", command=self.on_clear_all)
            self.menu_bar.add_cascade(label="Edit", menu=self.edit_menu)

    def on_open_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Excel Files", "*.xlsx"), ("CSV Files", "*.csv"), ("All Files", "*.*")])
        if file_path:
            self.current_df = pd.read_excel(file_path)  # Assuming an Excel file
            self.current_column = None
            self.display_data(self.current_df)

    def on_clear_all(self):
        self.current_df = None
        self.current_column = None
        self.current_row = -1
        self.top_bar.beta_label.config(text="All preferences cleared.")
        self.treeview.delete(*self.treeview.get_children())

    def on_set_shortcut_click(self):
        self.top_bar.beta_label.config(text="Set Shortcut button clicked")

    def on_change_paste_pref_click(self):
        self.top_bar.beta_label.config(text="Change Paste Preference button clicked")

    def on_ribbon_button_click(self, button_text):
        if self.current_df is None:
            self.top_bar.beta_label.config(text="Please select a spreadsheet first.")
            return

        if not self.current_column:
            self.top_bar.beta_label.config(text="Please select a column as the paste preference.")
            return

        self.current_row = int(button_text) - 1
        self.on_paste()

    def load_data(self):
        if not self.file_path:
            return

        try:
            df = pd.read_excel(self.file_path)  # Assuming an Excel file
            self.display_data(df)
        except Exception as e:
            self.label.config(text=f"Error loading data: {str(e)}")

    def display_data(self, df):
        columns = df.columns.tolist()
        self.treeview.delete(*self.treeview.get_children())
        self.treeview["columns"] = columns

        for col in columns:
            self.treeview.heading(col, text=col)
            self.treeview.column(col, width=100)

        for _, row in df.iterrows():
            self.treeview.insert("", "end", values=row.tolist())

        self.create_checkbuttons(columns)

    def create_checkbuttons(self, columns):
        for col in columns:
            tk.Checkbutton(self.checkbuttons_frame, text=col, variable=self.selected_column, onvalue=col, offvalue="").pack(side=tk.LEFT)

    def save_to_database(self):
        selected_col = self.selected_column.get()
        if selected_col:
            # Implement your database-saving logic here using the selected column data from the DataFrame
            self.label.config(text=f"Data from column '{selected_col}' saved to the database.")
        else:
            self.label.config(text="No column selected. Please select a column to save to the database.")

    def on_paste(self):
        if self.current_row == -1 or self.current_column is None:
            self.top_bar.beta_label.config(text="Please select a column and row to paste.")
            return

        data_to_paste = self.current_df.iloc[self.current_row, self.current_df.columns.get_loc(self.current_column)]
        if not pd.isna(data_to_paste):
            self.paste_to_clipboard(data_to_paste)
            self.current_row += 1
            if self.current_row >= len(self.current_df):
                self.current_row = -1
                self.top_bar.beta_label.config(text="All rows pasted.")
            else:
                self.top_bar.beta_label.config(text=f"Pasting row {self.current_row + 1}")
        else:
            self.top_bar.beta_label.config(text="No data to paste in the selected row.")

    def paste_to_clipboard(self, data):
        self.root.clipboard_clear()
        self.root.clipboard_append(data)

def main(file_path=None):
    if file_path is None:
        root = tk.Tk()
        first_screen = FirstScreen(root)
        root.wait_window(first_screen.root)

        if first_screen.completed:
            main(file_path=first_screen.file_path)
    else:
        root = tk.Tk()
        gui = MyGUI(root, file_path)
        root.mainloop()

if __name__ == "__main__":
    main()


