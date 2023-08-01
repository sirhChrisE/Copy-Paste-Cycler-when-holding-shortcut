import tkinter as tk
import customtkinter



class MyGUI: #defines the GUI elements and their behavior
    def __init__(self, root):
        # Initialize the main window (root)
        self.root = root
        self.root.title("Paste Cycler")
        
        # Create and place GUI widgets (buttons, labels, etc.)
        self.label = tk.Label(self.root, text="Lets get started!")
        self.label.pack()
        self.root.geometry("400x300")
        self.root.minsize(400, 300)
        self.root.resizable(True, True)





        # Define other GUI elements and their behavior

    def run(self):
        # Start the event loop that goes to main
        self.root.mainloop() #main window#







#### not going to touch main for a bit ####
def main():
    root = tk.Tk()
    gui = MyGUI(root)
    gui.run()

if __name__ == "__main__":
    main()
