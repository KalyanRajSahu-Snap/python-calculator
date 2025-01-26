import math
import tkinter as tk
from tkinter import messagebox

class ScientificCalculator:
    def __init__(self, master):
        self.master = master
        master.title("Scientific Calculator")
        master.geometry("400x600")
        master.configure(bg='#f0f0f0')

        # Entry field
        self.display = tk.Entry(master, width=30, font=('Arial', 18), justify='right')
        self.display.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky='nsew')

        # Buttons
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+',
            'sin', 'cos', 'tan', '^',
            'log', 'ln', 'sqrt', 'clear',
            '(', ')', 'pi', 'e'
        ]

        # Create buttons
        row = 1
        col = 0
        for button in buttons:
            cmd = lambda x=button: self.click(x)
            tk.Button(master, text=button, command=cmd, 
                      font=('Arial', 14), bg='#e0e0e0').grid(row=row, column=col, padx=5, pady=5, sticky='nsew')
            
            col += 1
            if col > 3:
                col = 0
                row += 1

        # Configure grid
        for i in range(4):
            master.grid_columnconfigure(i, weight=1)
        for i in range(row):
            master.grid_rowconfigure(i, weight=1)

    def click(self, key):
        if key == '=':
            try:
                result = eval(self.display.get().replace('^', '**')
                               .replace('sin', 'math.sin')
                               .replace('cos', 'math.cos')
                               .replace('tan', 'math.tan')
                               .replace('log', 'math.log10')
                               .replace('ln', 'math.log')
                               .replace('sqrt', 'math.sqrt')
                               .replace('pi', 'math.pi')
                               .replace('e', 'math.e'))
                self.display.delete(0, tk.END)
                self.display.insert(0, str(result))
            except Exception as e:
                messagebox.showerror("Error", str(e))
        
        elif key == 'clear':
            self.display.delete(0, tk.END)
        
        else:
            self.display.insert(tk.END, key)

def main():
    root = tk.Tk()
    calculator = ScientificCalculator(root)
    root.mainloop()

if __name__ == "__main__":
    main()