import pandas as pd
import matplotlib.pyplot as plt
from database import get_incomes, get_expenses

def generate_report():
    incomes = get_incomes()
    expenses = get_expenses()

    total_income = incomes['amount'].sum()
    total_expense = expenses['amount'].sum()
    net_savings = total_income - total_expense

    print(f"Общий доход: ${total_income}")
    print(f"Общие расходы: ${total_expense}")
    print(f"Экономия: ${net_savings}")

    plt.figure(figsize=(10, 5))

    plt.subplot(1, 2, 1)
    incomes.groupby('category')['amount'].sum().plot(kind='pie', autopct='%1.1f%%')
    plt.title('Распределение доходов по категориям')

    plt.subplot(1, 2, 2)
    expenses.groupby('category')['amount'].sum().plot(kind='pie', autopct='%1.1f%%')
    plt.title('Распределение расходов по категориям')

    plt.show()