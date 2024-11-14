import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.ticker import MaxNLocator

# Load data
df = pd.read_csv('sample_data_v3.csv', delimiter=';')

# Group by Broad Category and Credit Card, then sum the Amounts
card_spending = df.groupby(['Category(1)', 'Credit Card'])['Amount'].sum().unstack(fill_value=0)

# Define custom colors for each credit card
credit_card_colors = {
    'HSBC Credit Card': '#1f77b4',    # blue
    'Hang Seng Credit Card': '#ff7f0e', # orange
    'Citi Credit Card': '#2ca02c'      # green
}

# Map colors to the columns (credit cards) in card_spending DataFrame
colors = [credit_card_colors[card] for card in card_spending.columns]

# Plot the stacked bar chart with specified colors
plt.figure(figsize=(10, 6), facecolor='none')  # Transparent background
ax = card_spending.plot(kind='bar', stacked=True, color=colors, figsize=(10, 6), ax=plt.gca())

# Dark mode adjustments and font settings for readability
ax.set_title("", color="white", fontsize=24)  # Large title
ax.tick_params(axis='x', labelsize=18, colors='white')  # Larger x-axis tick labels
ax.tick_params(axis='y', labelsize=18, colors='white')  # Larger y-axis tick labels

# Reduce the number of ticks on the y-axis for readability
ax.yaxis.set_major_locator(MaxNLocator(nbins=5))  # Limit to 5 major ticks

# Transparent legend background and white text
legend = ax.legend(title="", bbox_to_anchor=(1.05, 1), loc='upper left', facecolor='none')
for text in legend.get_texts():
    text.set_color("white")
    text.set_fontsize('xx-large')
legend.get_title().set_color("white")

# Remove x and y axis titles for a cleaner look
ax.set_xlabel("")
ax.set_ylabel("")

plt.tight_layout()
plt.savefig("barchart_output/stacked_bar_chart_by_card_custom_colors_mobile_dark.png", format="png", dpi=300, transparent=True)
