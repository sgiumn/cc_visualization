import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Load data from CSV with semicolon delimiter
df = pd.read_csv('sample_data_v3.csv', delimiter=';')

# Convert the 'Date' column to datetime format
df['Date'] = pd.to_datetime(df['Date'])

# Set Date as index and add columns for day, week, and month
df['day'] = df['Date'].dt.day
df['weekday'] = df['Date'].dt.weekday
df['week'] = df['Date'].dt.isocalendar().week
df['month'] = df['Date'].dt.month

# Filter for the desired month (October, in this case)
df = df[df['Date'].dt.month == 10]

# Calculate total spending per day
daily_spending = df.groupby(df['Date'].dt.date)['Amount'].sum().reset_index()
daily_spending['Date'] = pd.to_datetime(daily_spending['Date'])
daily_spending.set_index('Date', inplace=True)

# Generate a date range for the entire month (October 2024)
date_range = pd.date_range(start="2024-10-01", end="2024-10-31", freq='D')

# Reindex the daily spending DataFrame to include all days, filling missing with 0
daily_spending = daily_spending.reindex(date_range, fill_value=0)
daily_spending.index.name = 'Date'

# Create new columns for day, weekday, and week for each date
daily_spending['day'] = daily_spending.index.day
daily_spending['weekday'] = daily_spending.index.weekday
daily_spending['week'] = daily_spending.index.isocalendar().week

# Pivot the data to get a calendar-style matrix (weeks as rows, weekdays as columns)
calendar_spending = daily_spending.pivot(index="week", columns="weekday", values="Amount")

# Set weekday labels
calendar_spending.columns = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

# Logarithmic transformation to reduce impact of large values
log_spending = np.log1p(calendar_spending)

# Plotting the heatmap in calendar format
plt.figure(figsize=(10, 6), facecolor='none')
sns.heatmap(
    log_spending,  # Use log-transformed data
    annot=calendar_spending,  # Annotate with original values
    fmt=".0f",
    cmap="mako",  # Darker colormap for better low-value contrast
    cbar_kws={'label': 'Log of Daily Spending (HKD)', 'ticks': [0, 2, 4, 6, 8]},
    annot_kws={"size": 14},  # Set annotation font size
    linewidths=0.5,
    linecolor='grey'
)

# Dark mode adjustments for mobile readability
plt.title("", color="white", fontsize=24, pad=20)
plt.xlabel("", color="white", fontsize=18)
plt.ylabel("", color="white", fontsize=18)
plt.xticks(fontsize=16, color='white')
plt.yticks(fontsize=16, color='white')

# Save the plot as a transparent PNG
plt.tight_layout()
plt.savefig("calendar_output/calendar_all_mobile_dark_log.png", format="png", dpi=300, transparent=True)
