import tkinter as tk
from tkinter import messagebox
from datetime import datetime

def check_age():
    date_str = entry_birthdate.get().strip()
    if not date_str:
        messagebox.showwarning("Предупреждение", "Введите дату рождения.")
        return

    try:
        birth = datetime.strptime(date_str, "%d.%m.%Y")
        today = datetime.today()
        age = today.year - birth.year
        if (today.month, today.day) < (birth.month, birth.day):
            age -= 1
        text_result.config(text=f"Ваш возраст: {age} полных лет.")
    except ValueError:
        messagebox.showerror("Ошибка", "Неверный формат даты.\nИспользуйте ДД.ММ.ГГГГ (например, 15.04.1990)")
        text_result.config(text="Ошибка: неверный формат даты.")
        entry_birthdate.delete(0, tk.END)
        entry_birthdate.focus()

def clear_fields():
    entry_birthdate.delete(0, tk.END)
    text_result.config(text="Здесь будет результат проверки")
    entry_birthdate.focus()

root = tk.Tk()
root.title("Проверка возраста")
root.geometry("560x420")
root.resizable(False, False)

label_title = tk.Label(
    root,
    text="Проверка возраста по дате рождения",
    font=("Arial", 16, "bold")
)
label_title.pack(pady=15)

label_birthdate = tk.Label(
    root,
    text="Введите дату рождения (ДД.ММ.ГГГГ):",
    font=("Arial", 12)
)
label_birthdate.pack()

entry_birthdate = tk.Entry(
    root,
    width=32,
    font=("Arial", 12)
)
entry_birthdate.pack(pady=10)

button_check = tk.Button(
    root,
    text="Проверить возраст",
    font=("Arial", 12),
    width=20,
    command=check_age
)
button_check.pack(pady=5)

button_clear = tk.Button(
    root,
    text="Очистить",
    font=("Arial", 12),
    width=20,
    command=clear_fields
)
button_clear.pack(pady=5)

text_result = tk.Label(
    root,
    text="Здесь будет результат проверки",
    font=("Arial", 11),
    wraplength=500,
    justify="left"
)
text_result.pack(pady=20)

root.mainloop()