# calculator GUI v1

import tkinter  as tk

def calculator():
    try :
        number1 = int(entry_number1.get())
        operator = entry_operator.get()
        number2 = int(entry_number2.get())
        
        if operator == "+":
            hasil.config(text= number1 + number2)
        elif operator == "-":
            hasil.config(text= number1 - number2)
        elif operator == "*":
            hasil.config(text= number1 * number2)
        elif operator == "/":
            if number2 != 0:
                hasil.config(text= number1 / number2)
            else: 
                hasil.config(text = "angka tidak bisa dibagi dengan 0")
        else:
            hasil.config(text ="operator tidak di kenali")
    except ValueError:
        hasil.config(text="masukan angka yang valid")

root = tk.Tk()
root.title("calculator")
root.geometry("500x200")

tk.Label(root, text="masukan angka ke 1 : ").pack()
entry_number1 = tk.Entry(root)
entry_number1.pack()

tk.Label(root, text="masukan operator +, -, *, / : ").pack()
entry_operator = tk.Entry(root)
entry_operator.pack()

tk.Label(root, text="masukan angka ke 2 : ").pack()
entry_number2 = tk.Entry(root)
entry_number2.pack()

tk.Button(root, text="cek", command=calculator).pack(pady=10)

hasil= tk.Label(root, text="")
hasil.pack()

root.mainloop()