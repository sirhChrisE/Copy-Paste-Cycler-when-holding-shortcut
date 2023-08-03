import tkinter as tk

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

class MyGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Paste Cycler")
        self.root.geometry("260x295")
        self.root.resizable(False, False)
        
        self.top_bar = TopBar(self.root, self.on_set_shortcut_click, self.on_change_paste_pref_click, self.on_ribbon_button_click)

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
        # Code to handle the "Open" menu item click
        pass

    def on_clear_all(self):
        # Code to handle the "Clear All" menu item click
        pass

    def on_set_shortcut_click(self):
        self.top_bar.beta_label.config(text="Set Shortcut button clicked")

    def on_change_paste_pref_click(self):
        self.top_bar.beta_label.config(text="Change Paste Preference button clicked")

    def on_ribbon_button_click(self, button_text):
        # Update the arrow indicator position
        if self.top_bar.selected_ribbon_button:
            self.top_bar.arrow_label.place_forget()  # Remove the arrow from its previous position if any

        selected_button = self.top_bar.ribbon_buttons[int(button_text) - 1]
        x = selected_button.winfo_x() + (selected_button.winfo_width() // 2)
        y = selected_button.winfo_y() + 277

        self.top_bar.arrow_label.place(x=x, y=y)

        self.top_bar.beta_label.config(text=f"Database {button_text} selected")
        self.top_bar.selected_ribbon_button = selected_button

def main():
    root = tk.Tk()
    gui = MyGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
