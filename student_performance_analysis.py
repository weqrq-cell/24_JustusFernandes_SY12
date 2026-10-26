import matplotlib.pyplot as plt
import pandas as pd

# 1. Read the CSV file into a Pandas DataFrame
df = pd.read_csv("student.csv")

# 2. Display the first five records and dataset information
print("--- First 5 Records ---")
print(df.head())

print("\n--- Dataset Information ---")
print(df.info())

# 3. Calculate the average, maximum, and minimum marks
avg_marks = df["marks"].mean()
max_marks = df["marks"].max()
min_marks = df["marks"].min()

print(f"\nAverage Marks: {avg_marks}")
print(f"Maximum Marks: {max_marks}")
print(f"Minimum Marks: {min_marks}")

# 4. Identify students who scored more than 75 marks
top_students = df[df["marks"] > 75]
print("\n--- Students Scoring More Than 75 Marks ---")
print(top_students)

# 5. Generate a bar chart showing marks obtained by each student
plt.figure(figsize=(8, 5))
plt.bar(df["name"], df["marks"], color="skyblue")
plt.xlabel("Student Name")
plt.ylabel("Marks")
plt.title("Marks Obtained by Each Student")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 6. Generate a histogram showing the distribution of student marks
plt.figure(figsize=(8, 5))
plt.hist(df["marks"], bins=5, color="orange", edgecolor="black")
plt.xlabel("Marks")
plt.ylabel("Frequency")
plt.title("Distribution of Student Marks")
plt.tight_layout()
plt.show()

# 7. Generate a scatter plot showing the relationship between study hours and marks
plt.figure(figsize=(8, 5))
plt.scatter(df["study_hours"], df["marks"], color="green", s=100)
plt.xlabel("Study Hours")
plt.ylabel("Marks")
plt.title("Study Hours vs. Marks")
plt.grid(True)
plt.tight_layout()
plt.show()
