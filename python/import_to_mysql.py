import csv
import mysql.connector

# Connect to MySQL
connection = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="",
    database="hr_analytics"
)

cursor = connection.cursor()

# Clear existing data
cursor.execute("TRUNCATE TABLE employees")

# CSV file
csv_file = "../hr_data.csv"

# Insert query
insert_query = """
INSERT INTO employees (
    EmployeeID,
    Age,
    Gender,
    Department,
    JobRole,
    Education,
    ExperienceYears,
    MonthlySalary,
    PerformanceScore,
    AttendanceRate,
    Overtime,
    JobSatisfaction,
    YearsAtCompany,
    Attrition
)
VALUES (
    %s, %s, %s, %s, %s, %s, %s,
    %s, %s, %s, %s, %s, %s, %s
)
"""

with open(csv_file, "r", encoding="utf-8") as file:
    reader = csv.reader(file)

    # Skip header
    next(reader)

    rows = list(reader)

cursor.executemany(insert_query, rows)

connection.commit()

print(f"Successfully imported {cursor.rowcount} employees!")

cursor.close()
connection.close()
