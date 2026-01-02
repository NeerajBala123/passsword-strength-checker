import tkinter as tk
from tkinter import ttk
import string

def check_strength():
    password = entry.get()

    has_letter = any(c.isalpha() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(c in string.punctuation for c in password)

    if len(password) < 6:
        strength.set("Weak Password")
        strength_label.config(fg="red")
        progress['value'] = 25
    elif len(password) >= 6 and has_letter and has_digit and not has_special:
        strength.set("Medium Password")
        strength_label.config(fg="orange")
        progress['value'] = 60
    elif len(password) >= 8 and has_letter and has_digit and has_special:
        strength.set("Strong Password")
        strength_label.config(fg="green")
        progress['value'] = 100
    else:
        strength.set("Medium Password")
        strength_label.config(fg="orange")
        progress['value'] = 60

def toggle_password():
    if entry.cget("show") == "":
        entry.config(show="*")
        toggle_btn.config(text="Show")
    else:
        entry.config(show="")
        toggle_btn.config(text="Hide")

# Main Window
window = tk.Tk()
window.title("Password Strength Checker")
window.geometry("420x260")
window.configure(bg="#f2f2f2")

# Title
tk.Label(
    window,
    text="🔐 Password Strength Checker",
    font=("Arial", 16, "bold"),
    bg="#f2f2f2"
).pack(pady=10)

# Password Label
tk.Label(
    window,
    text="Enter your password:",
    font=("Arial", 11),
    bg="#f2f2f2"
).pack()

# Password Entry Frame
entry_frame = tk.Frame(window, bg="#f2f2f2")
entry_frame.pack(pady=5)

entry = tk.Entry(entry_frame, width=30, font=("Arial", 11), show="*")
entry.pack(side="left", padx=5)

toggle_btn = tk.Button(
    entry_frame,
    text="Show",
    command=toggle_password
)
toggle_btn.pack(side="left")

# Check Button
tk.Button(
    window,
    text="Check Strength",
    command=check_strength,
    font=("Arial", 11),
    bg="#4CAF50",
    fg="white",
    width=15
).pack(pady=10)

# Strength Label
strength = tk.StringVar()
strength_label = tk.Label(
    window,
    textvariable=strength,
    font=("Arial", 12, "bold"),
    bg="#f2f2f2"
)
strength_label.pack()

# Progress Bar
progress = ttk.Progressbar(
    window,
    length=250,
    mode="determinate"
)
progress.pack(pady=10)

window.mainloop()
