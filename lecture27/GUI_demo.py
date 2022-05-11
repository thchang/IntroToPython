import tkinter
import tkinter.messagebox

class myGUI():
    """ Class for implementing a GUI """

    def __init__(self):
        """ The constructor should create a new tkinter window and all widgets """

        self.window = tkinter.Tk()
        self.label = tkinter.Label(self.window, text="Enter your name below:")
        self.entry = tkinter.Entry(self.window)
        self.hi_button = tkinter.Button(self.window, text="Say Hi", command=self.button1_func)
        self.quit_button = tkinter.Button(self.window, text="Quit", command=self.window.destroy)
        return

    def button1_func(self):
        """ This is the code for handling the "hi_button" click event """

        name = self.entry.get()
        tkinter.messagebox.showinfo("hello", f"Hello {name}!")
        return

    def run(self):
        """ Pack all widgets into the window (in order of their pack command) and run. """

        self.label.pack()
        self.entry.pack()
        self.hi_button.pack()
        self.quit_button.pack()
        tkinter.mainloop()
        return


# This driver code will only run when the script is run as the main program
if __name__ == "__main__":
    new_gui = myGUI()
    new_gui.run()
