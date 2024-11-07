import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load data from CSV with semicolon delimiter
df = pd.read_csv('all_transactions.csv', delimiter=';')

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

# Plotting the heatmap in calendar format
plt.figure(figsize=(10, 6))
sns.heatmap(calendar_spending, annot=True, fmt=".0f", cmap="YlOrRd", cbar_kws={'label': 'Daily Spending (HKD)'})
plt.title("October 2024 Spending Calendar")
plt.xlabel("Day of Week")
plt.ylabel("Week of Month")
plt.savefig("calendar_output/calendar_all.png", format="png", dpi=600)




df = pd.read_csv('hsbc_transactions.csv', delimiter=';')

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

# Plotting the heatmap in calendar format
plt.figure(figsize=(10, 6))
sns.heatmap(calendar_spending, annot=True, fmt=".0f", cmap="YlOrRd", cbar_kws={'label': 'Daily Spending (HKD)'})
plt.title("HSBC October 2024 Spending Calendar")
plt.xlabel("Day of Week")
plt.ylabel("Week of Month")
plt.savefig("calendar_output/calendar_hsbc.png", format="png", dpi=600)


df = pd.read_csv('citi_transactions.csv', delimiter=';')

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

# Plotting the heatmap in calendar format
plt.figure(figsize=(10, 6))
sns.heatmap(calendar_spending, annot=True, fmt=".0f", cmap="YlOrRd", cbar_kws={'label': 'Daily Spending (HKD)'})
plt.title("Citi October 2024 Spending Calendar")
plt.xlabel("Day of Week")
plt.ylabel("Week of Month")
plt.savefig("calendar_output/calendar_citi.png", format="png", dpi=600)



df = pd.read_csv('hangseng_transactions.csv', delimiter=';')

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

# Plotting the heatmap in calendar format
plt.figure(figsize=(10, 6))
sns.heatmap(calendar_spending, annot=True, fmt=".0f", cmap="YlOrRd", cbar_kws={'label': 'Daily Spending (HKD)'})
plt.title("Hang Seng October 2024 Spending Calendar")
plt.xlabel("Day of Week")
plt.ylabel("Week of Month")
plt.savefig("calendar_output/calendar_hangseng.png", format="png", dpi=600)
