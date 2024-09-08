import tkinter as tk
from tkinter import messagebox
from database import create_db, add_income, add_expense
from analysis import generate_report

# Создание бд
create_db()


# Кнопки
def submit_income():
    date = entry_income_date.get()
    amount = float(entry_income_amount.get())
    category = entry_income_category.get()
    description = entry_income_description.get()

    add_income(date, amount, category, description)
    messagebox.showinfo("Info", "Доходы успешно добавлены!")


def submit_expense():
    date = entry_expense_date.get()
    amount = float(entry_expense_amount.get())
    category = entry_expense_category.get()
    description = entry_expense_description.get()

    add_expense(date, amount, category, description)
    messagebox.showinfo("Info", "Расходы успешно добавлены!")


def show_report():
    generate_report()


# Окно приложения
root = tk.Tk()
root.title("Менеджер по персональным финансам")

# Ввод доходов
tk.Label(root, text="Дата доходов").grid(row=0, column=0)
entry_income_date = tk.Entry(root)
entry_income_date.grid(row=0, column=1)

tk.Label(root, text="Сумма").grid(row=1, column=0)
entry_income_amount = tk.Entry(root)
entry_income_amount.grid(row=1, column=1)

tk.Label(root, text="Категория").grid(row=2, column=0)
entry_income_category = tk.Entry(root)
entry_income_category.grid(row=2, column=1)

tk.Label(root, text="Описание").grid(row=3, column=0)
entry_income_description = tk.Entry(root)
entry_income_description.grid(row=3, column=1)

tk.Button(root, text="Добавить доходы", command=submit_income).grid(row=4, column=0, columnspan=2)

# Ввод расходов
tk.Label(root, text="Дата расходов").grid(row=5, column=0)
entry_expense_date = tk.Entry(root)
entry_expense_date.grid(row=5, column=1)

tk.Label(root, text="Сумма").grid(row=6, column=0)
entry_expense_amount = tk.Entry(root)
entry_expense_amount.grid(row=6, column=1)

tk.Label(root, text="Категория").grid(row=7, column=0)
entry_expense_category = tk.Entry(root)
entry_expense_category.grid(row=7, column=1)

tk.Label(root, text="Описание").grid(row=8, column=0)
entry_expense_description = tk.Entry(root)
entry_expense_description.grid(row=8, column=1)

tk.Button(root, text="Добавить расходы", command=submit_expense).grid(row=9, column=0, columnspan=2)

# Кнопка для создания отчета
tk.Button(root, text="Сгенерировать отчет", command=show_report).grid(row=10, column=0, columnspan=2)

# Запуск основного цикла
root.mainloop()