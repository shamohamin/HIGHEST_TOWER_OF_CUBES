import tkinter as tk


class WelcomeFrame(tk.Frame):
    LARGE_FONT = ("Verdana", 12)

    def __init__(self, master, controller):
        super().__init__(master)
        self.label = tk.Label(self, text="welcome")
        self.button = tk.Button(self, text="start", font=WelcomeFrame.LARGE_FONT, background="red",
                                command=lambda: self.clear_and_change_frame(controller))
        self.label.pack()
        self.button.pack()
        self.pack(padx=20, pady=20)

    def clear_and_change_frame(self, con):
        self.label.destroy()
        self.button.destroy()
        con.starter()
