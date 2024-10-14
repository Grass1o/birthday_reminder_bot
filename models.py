import sqlite3  

def get_connection():  
    return sqlite3.connect('db/database.db')  

def add_employee(user_id, full_name, date_of_birth):  
    with get_connection() as conn:  
        cursor = conn.cursor()  
        cursor.execute("INSERT INTO employees (user_id, full_name, date_of_birth) VALUES (?, ?, ?)", (user_id, full_name, date_of_birth))  
        conn.commit()  

def remove_employee(user_id, employee_id):  
    with get_connection() as conn:  
        cursor = conn.cursor()  
        cursor.execute("DELETE FROM employees WHERE id = ? AND user_id = ?", (employee_id, user_id))  
        conn.commit()  

def get_employees(user_id):  
    with get_connection() as conn:  
        cursor = conn.cursor()  
        cursor.execute("SELECT full_name, date_of_birth FROM employees WHERE user_id = ?", (user_id,))  
        return ["{} - {}".format(row[0], row[1]) for row in cursor.fetchall()]  

def init_db():  
    with get_connection() as conn:  
        cursor = conn.cursor()  
        cursor.execute('''CREATE TABLE IF NOT EXISTS employees (  
            id INTEGER PRIMARY KEY AUTOINCREMENT,  
            user_id INTEGER,  
            full_name TEXT,  
            date_of_birth TEXT  
        )''')  
        conn.commit()
