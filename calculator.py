import tkinter as tk
def button_click(symbol):
    current = display_var.get()
    display_var.set(current + symbol)
def clear_display():
    display_var.set("")
def calculate_result():
    try:
        result = eval(display_var.get())
        display_var.set(result)
    except Exception as e:
        display_var.set("Error")
root = tk.Tk()
root.title(" Calculator")
root.geometry("300x400")
root.configure(bg="lightblue")
display_var = tk.StringVar()
display_entry = tk.Entry(root, textvariable=display_var, font=('Arial', 18), bd=10, insertwidth=4, width=14, justify='right')
display_entry.grid(row=0, column=0, columnspan=4)
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('C', 4, 1), ('=', 4, 2), ('+', 4, 3),
]

for (text, row, column) in buttons:
    button = tk.Button(root, text=text, font=('Arial', 18), padx=20, pady=20, bg='#f78f0a' if text in {'=', 'C'} else 'white', command=lambda t=text: button_click(t) if t not in {'=', 'C'} else calculate_result() if t == '=' else clear_display())
    button.grid(row=row, column=column, sticky='nsew')
for i in range(5):
    root.columnconfigure(i, weight=1)
    root.rowconfigure(i, weight=1)
root.mainloop()
