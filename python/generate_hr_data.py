import pandas as pd
import numpy as np

np.random.seed(42)

n = 1000

departments = [
    "IT",
    "HR",
    "Finance",
    "Sales",
    "Marketing",
    "Operations"
]

job_roles = [
    "Software Engineer",
    "HR Executive",
    "Financial Analyst",
    "Sales Executive",
    "Marketing Specialist",
    "Operations Manager"
]

genders = ["Male", "Female"]

education = [
    "High School",
    "Bachelor's",
    "Master's",
    "PhD"
]

data = {
    "EmployeeID": [
        f"E{1000 + i}"
        for i in range(1, n + 1)
    ],

    "Age": np.random.randint(21, 60, n),

    "Gender": np.random.choice(
        genders,
        n
    ),

    "Department": np.random.choice(
        departments,
        n
    ),

    "JobRole": np.random.choice(
        job_roles,
        n
    ),

    "Education": np.random.choice(
        education,
        n
    ),

    "ExperienceYears": np.random.randint(
        0, 21, n
    ),

    "MonthlySalary": np.random.randint(
        25000,
        150000,
        n
    ),

    "PerformanceScore": np.random.randint(
        1,
        6,
        n
    ),

    "AttendanceRate": np.round(
        np.random.uniform(65, 100, n),
        2
    ),

    "Overtime": np.random.choice(
        ["Yes", "No"],
        n,
        p=[0.3, 0.7]
    ),

    "JobSatisfaction": np.random.randint(
        1,
        6,
        n
    ),

    "YearsAtCompany": np.random.randint(
        0,
        16,
        n
    ),

    "Attrition": np.random.choice(
        ["Yes", "No"],
        n,
        p=[0.18, 0.82]
    )
}

df = pd.DataFrame(data)

df.to_csv(
    "../hr_data.csv",
    index=False
)

print("HR dataset created successfully!")
print(f"Total employees: {len(df)}")
print(df.head())
