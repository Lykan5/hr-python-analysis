import matplotlib.pyplot as plt
import pandas as pd

data = {
    "EmpID": [101, 102, 103, 104, 105, 106, 107, 108],
    "Name": ["Arun", "Priya", "Rahul", "Sneha", "Vikram", "Meena", "Karan", "Divya"],
    "Department": ["IT", "HR", "Finance", "IT", "Sales", "HR", "Finance", "IT"],
    "Age": [28, 32, 45, 26, 38, 29, 41, 30],
    "Experience": [3, 8, 20, 2, 15, 5, 18, 6],
    "Salary": [50000, 60000, 120000, 45000, 90000, 55000, 110000, 65000],
    "PerformanceScore": [4.2, 4.5, 4.8, 3.9, 4.6, 4.3, 4.7, 4.4],
    "Attrition": ["No", "No", "No", "Yes", "No", "Yes", "No", "No"]
}

df = pd.DataFrame(data)

print("\n📊 FULL HR DATA")
print(df)

print("\n💰 Average Salary by Department")
print(df.groupby("Department")["Salary"].mean())

print("\n🏆 Highest Paid Employee")
print(df.loc[df["Salary"].idxmax()])

print("\n🚪 Employees who left")
print(df[df["Attrition"] == "Yes"])

print("\n⭐ Top Performers (Score > 4.5)")
print(df[df["PerformanceScore"] > 4.5])

print("\n📊 Experience vs Salary")
print(df[["Name", "Experience", "Salary"]].sort_values(by="Experience", ascending=False))

# Visualization - department-wise average salary
plt.figure()
df.groupby("Department")["Salary"].mean().plot(kind="bar")
plt.title("Average Salary by Department")
plt.xlabel("Department")
plt.ylabel("Salary")
plt.savefig("department_salary.png")  # saves file
plt.show()

# Visualization - attrition count
plt.figure()
df["Attrition"].value_counts().plot(kind="bar")
plt.title("Attrition Count")
plt.savefig("attrition_chart.png")
plt.show()

# Visualization - experience vs salary
plt.figure()
plt.scatter(df["Experience"], df["Salary"])
plt.title("Experience vs Salary")
plt.savefig("experience_salary.png")
plt.show()

# Export full dataset to Excel
df.to_excel("hr_report.xlsx", index=False)
print("\n📁 HR report exported successfully!")
summary = df.groupby("Department")["Salary"].mean()
summary.to_excel("department_salary_summary.xlsx")
print("📊 Summary report exported!")