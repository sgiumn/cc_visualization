import pandas as pd
import matplotlib.pyplot as plt

# Load data from CSV with semicolon delimiter
df = pd.read_csv('october_transactions.csv', delimiter=';')

# Group by category and sum the amounts
category_distribution = df.groupby('Category')['Amount'].sum()

# Plotting the pie chart
plt.figure(figsize=(8, 8))
plt.pie(category_distribution, labels=category_distribution.index, autopct='%1.1f%%', startangle=140)
plt.title("Spending Distribution by Category (October 2024)")
plt.show()
