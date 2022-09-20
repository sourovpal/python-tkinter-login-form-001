from cmath import cos
import tkinter as tk
import tkinter.ttk as ttk

root = tk.Tk()

root.title("Hello")

root.geometry("240x100")
root.resizable(False, False)


root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=3)
# User name label
username_label = ttk.Label(root, text="Username")
username_label.grid(row=0, column=0, sticky=tk.W, padx=5, pady=5)
# Username input field
username_input = ttk.Entry(root)
username_input.grid(row=0, column=1, sticky="we", padx=10, pady=5)
# Password label
password_label = ttk.Label(root, text="Password")
password_label.grid(row=1, column=0, sticky=tk.W, padx=5, pady=5)
# Password input field
password_input = ttk.Entry(root)
password_input.grid(row=1, column=1, sticky="we", padx=10, pady=5)
# Login button
login_btn = ttk.Button(root, text="Login")
login_btn.grid(row=2,column=1, columnspan=2, sticky="e", padx=10, pady=5)

if __name__ == '__main__':
    root.mainloop()
