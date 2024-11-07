import pandas as pd
import plotly.express as px

# Load data
df = pd.read_csv('all_transactions.csv', delimiter=';')

# Create the sunburst chart
fig = px.sunburst(df, path=['Category(1)', 'Category(2)'], values='Amount',
                  title="Spending Breakdown by Category (October 2024)")
fig.update_traces(textinfo="label+percent parent")

# Save the chart as a PNG image
fig.write_image("sunburst_output/sunburst_chart.png", format="png", width=800, height=800)


# Load data
df = pd.read_csv('hsbc_transactions.csv', delimiter=';')

# Create the sunburst chart
fig = px.sunburst(df, path=['Category(1)', 'Category(2)'], values='Amount',
                  title="HSBC Spending Breakdown by Category (October 2024)")
fig.update_traces(textinfo="label+percent parent")

# Save the chart as a PNG image
fig.write_image("sunburst_output/sunburst_chart_hsbc.png", format="png", width=800, height=800)


# Load data
df = pd.read_csv('citi_transactions.csv', delimiter=';')

# Create the sunburst chart
fig = px.sunburst(df, path=['Category(1)', 'Category(2)'], values='Amount',
                  title="Citi Spending Breakdown by Category (October 2024)")
fig.update_traces(textinfo="label+percent parent")

# Save the chart as a PNG image
fig.write_image("sunburst_output/sunburst_chart_citi.png", format="png", width=800, height=800)


# Load data
df = pd.read_csv('hangseng_transactions.csv', delimiter=';')

# Create the sunburst chart
fig = px.sunburst(df, path=['Category(1)', 'Category(2)'], values='Amount',
                  title="Hang Seng Bank Spending Breakdown by Category (October 2024)")
fig.update_traces(textinfo="label+percent parent")

# Save the chart as a PNG image
fig.write_image("sunburst_output/sunburst_chart_hangseng.png", format="png", width=800, height=800)