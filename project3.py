import mysql.connector
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Establishing connection to MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="abhi1234",  
    database="project2"        
)

# Load employee data from MySQL into Pandas DataFrame
query = "SELECT * FROM employees"
df = pd.read_sql(query, conn)

# Close the connection
conn.close()

# Display first few rows of the data
print("Employee Data:")
print(df.head())

# Data Preprocessing (handling any nulls, data types, etc.)
df['exit_status'] = df['exit_status'].map({0: 'Active', 1: 'Left'})  # Mapping exit status for better visualization
df['gender'] = df['gender'].map({'Male': 'Male', 'Female': 'Female'})

# Data Analysis & Visualization

# 1. Attrition by Salary
plt.figure(figsize=(10, 6))
sns.boxplot(x='exit_status', y='salary', data=df)
plt.title("Employee Attrition by Salary")
plt.show()

# 2. Tenure vs. Attrition
plt.figure(figsize=(10, 6))
sns.boxplot(x='exit_status', y='tenure', data=df)
plt.title("Employee Attrition by Tenure")
plt.show()

# 3. Performance Score vs. Attrition
plt.figure(figsize=(10, 6))
sns.boxplot(x='exit_status', y='performance_score', data=df)
plt.title("Employee Attrition by Performance Score")
plt.show()

# 4. Attrition Rate by Department
plt.figure(figsize=(10, 6))
sns.countplot(x='department', hue='exit_status', data=df)
plt.title("Employee Attrition Rate by Department")
plt.xticks(rotation=45)
plt.show()

# 5. Gender Distribution in Attrition
plt.figure(figsize=(10, 6))
sns.countplot(x='gender', hue='exit_status', data=df)
plt.title("Gender Distribution in Employee Attrition")
plt.show()
