from temp_mod import *
import tkinter
import tkinter.messagebox

class TemperaturesGUI():
    """ GUI for converting temperatures. """

    def __init__(self):
        """ Construct a GUI with main window, label, text entry, and 3 buttons. """

        self.main_window = tkinter.Tk()
        self.instructions = tkinter.Label(self.main_window,
                                          text="\nPlease enter a temperature in degrees F or C:\n")
        self.userInput = tkinter.Entry(self.main_window)
        self.toC = tkinter.Button(self.main_window, text="Convert to deg C", command=self.toCelsius)
        self.toF = tkinter.Button(self.main_window, text="Convert to deg F", command=self.toFarenheit)
        self.quit = tkinter.Button(self.main_window, text="Quit", command=self.main_window.destroy)
        return

    def toCelsius(self):
        """ Code for handling "toC" button click event. """

        try:
            tempF = float(self.userInput.get())
            tempC = F_to_C(tempF)
            tkinter.messagebox.showinfo("Deg F to Deg C", f"{tempF:.4f} deg F = {tempC:.4f} deg C")
        except ValueError:
            tkinter.messagebox.showinfo("Error", "An error occured: could not convert input to a float")
        return

    def toFarenheit(self):
        """ Code for handling "toF" button click event. """

        try:
            tempC = float(self.userInput.get())
            tempF = C_to_F(tempC)
            tkinter.messagebox.showinfo("Deg C to Deg F", f"{tempC:.4f} deg C = {tempF:.4f} deg F")
        except ValueError:
            tkinter.messagebox.showinfo("Error", "An error occured: could not convert input to a float")
        return

    def run(self):
        """ Pack all widgets into main window and run the main loop. """

        self.instructions.pack()
        self.userInput.pack()
        self.toC.pack()
        self.toF.pack()
        self.quit.pack()
        tkinter.mainloop()
        return


# Driver code only runs when the script is run as main
if __name__ == "__main__":
    my_gui = TemperaturesGUI()
    my_gui.run()
