import plotly.express as px
import pandas as pd

# Load data
df = pd.read_csv('sample_data_v3.csv', delimiter=';')

# Create the sunburst chart
fig = px.sunburst(df, path=['Category(1)', 'Category(2)'], values='Amount',
                  )

# Dark mode styling adjustments
fig.update_layout(
    paper_bgcolor='rgba(0,0,0,0)',  # Transparent background
    plot_bgcolor='rgba(0,0,0,0)',
    font=dict(color='white', size=18),  # White, larger font
    title=dict(font=dict(size=24))  # Larger title font
)

fig.update_traces(textinfo="label+percent parent", marker=dict(line=dict(color='black', width=1)))

# Save the chart as a transparent PNG image
fig.write_image("sunburst_output/sunburst_chart_dark.png", format="png", width=800, height=800)
