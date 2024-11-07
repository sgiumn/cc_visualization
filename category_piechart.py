import pandas as pd
import matplotlib.pyplot as plt


# Load data from CSV with semicolon delimiter
df = pd.read_csv('all_transactions.csv', delimiter=';')
# Group by category and sum the amounts
category_distribution = df.groupby('Category(2)')['Amount'].sum()

# Plotting the pie chart
plt.figure(figsize=(8, 8))
plt.pie(category_distribution, labels=category_distribution.index, autopct='%1.1f%%', startangle=140)
plt.title("Spending Distribution by Category (October 2024)")
plt.savefig("piechart_output/piechart_spec.png", format="png", dpi=600)



# Load data from CSV with semicolon delimiter
df = pd.read_csv('all_transactions.csv', delimiter=';')
# Group by category and sum the amounts
category_distribution = df.groupby('Category(1)')['Amount'].sum()

# Plotting the pie chart
plt.figure(figsize=(8, 8))
plt.pie(category_distribution, labels=category_distribution.index, autopct='%1.1f%%', startangle=140)
plt.title("Spending Distribution by Category (October 2024)")
plt.savefig("piechart_output/piechart_simple.png", format="png", dpi=600)



# Load data from CSV with semicolon delimiter
df = pd.read_csv('hsbc_transactions.csv', delimiter=';')
# Group by category and sum the amounts
category_distribution = df.groupby('Category(1)')['Amount'].sum()

# Plotting the pie chart
plt.figure(figsize=(8, 8))
plt.pie(category_distribution, labels=category_distribution.index, autopct='%1.1f%%', startangle=140)
plt.title("HSBC Spending Distribution by Category (October 2024)")
plt.savefig("piechart_output/piechart_hsbc_simple.png", format="png", dpi=600)

# Load data from CSV with semicolon delimiter
df = pd.read_csv('hsbc_transactions.csv', delimiter=';')
# Group by category and sum the amounts
category_distribution = df.groupby('Category(2)')['Amount'].sum()

# Plotting the pie chart
plt.figure(figsize=(8, 8))
plt.pie(category_distribution, labels=category_distribution.index, autopct='%1.1f%%', startangle=140)
plt.title("HSBC Spending Distribution by Category (October 2024)")
plt.savefig("piechart_output/piechart_hsbc_spec.png", format="png", dpi=600)




# Load data from CSV with semicolon delimiter
df = pd.read_csv('citi_transactions.csv', delimiter=';')
# Group by category and sum the amounts
category_distribution = df.groupby('Category(1)')['Amount'].sum()

# Plotting the pie chart
plt.figure(figsize=(8, 8))
plt.pie(category_distribution, labels=category_distribution.index, autopct='%1.1f%%', startangle=140)
plt.title("Citi Spending Distribution by Category (October 2024)")
plt.savefig("piechart_output/piechart_citi_simple.png", format="png", dpi=600)

# Load data from CSV with semicolon delimiter
df = pd.read_csv('citi_transactions.csv', delimiter=';')
# Group by category and sum the amounts
category_distribution = df.groupby('Category(2)')['Amount'].sum()

# Plotting the pie chart
plt.figure(figsize=(8, 8))
plt.pie(category_distribution, labels=category_distribution.index, autopct='%1.1f%%', startangle=140)
plt.title("Citi Spending Distribution by Category (October 2024)")
plt.savefig("piechart_output/piechart_citi_spec.png", format="png", dpi=600)




# Load data from CSV with semicolon delimiter
df = pd.read_csv('hangseng_transactions.csv', delimiter=';')
# Group by category and sum the amounts
category_distribution = df.groupby('Category(1)')['Amount'].sum()

# Plotting the pie chart
plt.figure(figsize=(8, 8))
plt.pie(category_distribution, labels=category_distribution.index, autopct='%1.1f%%', startangle=140)
plt.title("Hang Seng Bank Spending Distribution by Category (October 2024)")
plt.savefig("piechart_output/piechart_hangseng_simple.png", format="png", dpi=600)

# Load data from CSV with semicolon delimiter
df = pd.read_csv('hangseng_transactions.csv', delimiter=';')
# Group by category and sum the amounts
category_distribution = df.groupby('Category(2)')['Amount'].sum()

# Plotting the pie chart
plt.figure(figsize=(8, 8))
plt.pie(category_distribution, labels=category_distribution.index, autopct='%1.1f%%', startangle=140)
plt.title("Hang Seng Bank Spending Distribution by Category (October 2024)")
plt.savefig("piechart_output/piechart_hangseng_spec.png", format="png", dpi=600)