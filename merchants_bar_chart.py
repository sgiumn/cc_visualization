import pandas as pd
import matplotlib.pyplot as plt

# Load data from CSV with semicolon delimiter
df = pd.read_csv('all_transactions.csv', delimiter=';')

# Group by both merchant and credit card, summing the spending for each combination
merchant_card_spending = df.groupby(['Vendor/Merchant', 'Credit Card'])['Amount'].sum().unstack(fill_value=0)

# Sort merchants by total spending to get the top 10 merchants
top_merchants = merchant_card_spending.sum(axis=1).sort_values(ascending=False).head(10)
top_merchant_card_spending = merchant_card_spending.loc[top_merchants.index]

# Plotting the stacked bar chart
top_merchant_card_spending.plot(kind='bar', stacked=True, figsize=(12, 8), color=['#1f77b4', '#ff7f0e', '#2ca02c'])  # Custom colors for each card
plt.title("Top 10 Merchants by Spending with Credit Card Breakdown (October 2024)")
plt.xlabel("Merchant")
plt.ylabel("Total Spending (HKD)")
plt.xticks(rotation=45, ha='right')  # Rotate merchant names for readability
plt.legend(title="Credit Card")
plt.tight_layout()  # Adjust layout for better fit
plt.savefig("barchart_output/barchart.png", format="png", dpi=600)
