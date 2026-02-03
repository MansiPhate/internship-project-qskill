import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Get absolute path of this file (data_analysis.py)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Build path to CSV file safely
csv_path = os.path.join(BASE_DIR, "..", "data", "student.csv")

# Load CSV
data = pd.read_csv(csv_path)

#display data
print("Dataset:")
print(data)

#Calculate average marks
average_marks = data[["Maths", "Science", "English"]].mean()
print("\nAverage marks:")
print(average_marks)

#Bar chart for average marks
average_marks.plot(kind='bar')
plt.title("Average Marks")
plt.ylabel("Subjects")
plt.xlabel("Marks")
plt.show()

#Scatter plot (Maths vs Science)
plt.scatter(data["Maths"], data["Science"])
plt.title("Maths vs Science")
plt.xlabel("Maths")
plt.ylabel("Science")
plt.show()

#Heatmap for correlation
sns.heatmap(data[["Maths", "Science", "English"]].corr(), annot=True)
plt.title("Correlation Heatmap")
plt.show()