import tkinter as tk
import sys

class ConsoleOutput(tk.Text):
    def write(self, message):
        self.insert(tk.END, message)
        self.see(tk.END)

def button_click():
    # Perform some action
    output_text.write("Button clicked\n")

root = tk.Tk()

output_text = ConsoleOutput(root, height=10, width=40)
output_text.pack()
output_text.configure(state="disabled")

sys.stdout = output_text

button = tk.Button(root, text="Click me", command=button_click)
button.pack()

root.mainloop()
