import sqlite3
import pandas as pd

def create_db():
    conn = sqlite3.connect('finance_manager.db')
    cursor = conn.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS income (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        date TEXT,
        amount REAL,
        category TEXT,
        description TEXT
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS expenses (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        date TEXT,
        amount REAL,
        category TEXT,
        description TEXT
    )
    ''')

    conn.commit()
    conn.close()

def add_income(date, amount, category, description):
    conn = sqlite3.connect('finance_manager.db')
    cursor = conn.cursor()
    cursor.execute('''
    INSERT INTO income (date, amount, category, description)
    VALUES (?, ?, ?, ?)
    ''', (date, amount, category, description))
    conn.commit()
    conn.close()

def add_expense(date, amount, category, description):
    conn = sqlite3.connect('finance_manager.db')
    cursor = conn.cursor()
    cursor.execute('''
    INSERT INTO expenses (date, amount, category, description)
    VALUES (?, ?, ?, ?)
    ''', (date, amount, category, description))
    conn.commit()
    conn.close()

def get_incomes():
    conn = sqlite3.connect('finance_manager.db')
    df = pd.read_sql_query("SELECT * FROM income", conn)
    conn.close()
    return df

def get_expenses():
    conn = sqlite3.connect('finance_manager.db')
    df = pd.read_sql_query("SELECT * FROM expenses", conn)
    conn.close()
    return df