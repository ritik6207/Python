
import sqlite3

# ==========================================
# 1. DATABASE CONNECTION
# ==========================================

conn = sqlite3.connect('test.db.sqlite3')
cur = conn.cursor()

print("Database connected successfully!")


# ==========================================
# 2. CREATE TABLE
# ==========================================

qry = """
CREATE TABLE IF NOT EXISTS Employee (
    EmpID INTEGER PRIMARY KEY AUTOINCREMENT,
    FIRST_NAME TEXT(20),
    LAST_NAME TEXT(20),
    AGE INTEGER,
    SEX TEXT(1),
    INCOME FLOAT
);
"""

try:
    cur.execute(qry)
    conn.commit()
    print("Employee table created successfully!")
except sqlite3.Error as e:
    print("Table creation error:", e)


# ==========================================
# 3. INSERT - ADD MULTIPLE EMPLOYEES
# ==========================================

employees = [
    ('Mac', 'Mohan', 20, 'M', 2000),
    ('Rahul', 'Sharma', 25, 'M', 35000),
    ('Priya', 'Verma', 23, 'F', 40000),
    ('Amit', 'Kumar', 28, 'M', 50000),
    ('Neha', 'Singh', 24, 'F', 45000)
]

try:
    cur.executemany("""
        INSERT INTO Employee
        (FIRST_NAME, LAST_NAME, AGE, SEX, INCOME)
        VALUES (?, ?, ?, ?, ?)
    """, employees)

    conn.commit()
    print("\nMultiple employees inserted successfully!")

except sqlite3.Error as e:
    conn.rollback()
    print("Insert error:", e)


# ==========================================
# 4. SELECT - DISPLAY ALL EMPLOYEES
# ==========================================

print("\n========== ALL EMPLOYEES ==========")

cur.execute("SELECT * FROM Employee")

records = cur.fetchall()

for row in records:
    print(row)


# ==========================================
# 5. WHERE - FIND EMPLOYEE BY ID
# ==========================================

print("\n========== FIND EMPLOYEE BY ID ==========")

emp_id = 2

cur.execute(
    "SELECT * FROM Employee WHERE EmpID = ?",
    (emp_id,)
)

employee = cur.fetchone()

if employee:
    print("Employee Found:", employee)
else:
    print("Employee not found!")


# ==========================================
# 6. UPDATE - UPDATE EMPLOYEE INCOME
# ==========================================

print("\n========== UPDATE EMPLOYEE INCOME ==========")

emp_id = 2
new_income = 60000

try:
    cur.execute("""
        UPDATE Employee
        SET INCOME = ?
        WHERE EmpID = ?
    """, (new_income, emp_id))

    conn.commit()

    if cur.rowcount > 0:
        print("Employee income updated successfully!")
    else:
        print("Employee ID not found!")

except sqlite3.Error as e:
    conn.rollback()
    print("Update error:", e)


# ==========================================
# 7. DELETE - DELETE EMPLOYEE
# ==========================================

print("\n========== DELETE EMPLOYEE ==========")

emp_id = 5

try:
    cur.execute(
        "DELETE FROM Employee WHERE EmpID = ?",
        (emp_id,)
    )

    conn.commit()

    if cur.rowcount > 0:
        print("Employee deleted successfully!")
    else:
        print("Employee ID not found!")

except sqlite3.Error as e:
    conn.rollback()
    print("Delete error:", e)


# ==========================================
# 8. DISPLAY FINAL EMPLOYEE RECORDS
# ==========================================

print("\n========== FINAL EMPLOYEE RECORDS ==========")

cur.execute("SELECT * FROM Employee")

for row in cur.fetchall():
    print(row)


# ==========================================
# 9. CLOSE DATABASE CONNECTION
# ==========================================

cur.close()
conn.close()

print("\nDatabase connection closed!")
