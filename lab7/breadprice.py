import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv('breadprice.csv')

# Drop any rows where all month columns are empty
df.dropna(subset=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 
                  'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'], how='all', inplace=True)

# Convert all month columns to numeric (in case of empty strings or NaNs)
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
          'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
df[months] = df[months].apply(pd.to_numeric, errors='coerce')

# Calculate average price for each year
df['AveragePrice'] = df[months].mean(axis=1)

# Plot the average bread price per year
plt.figure(figsize=(10, 6))
plt.plot(df['Year'], df['AveragePrice'], marker='o')
plt.title('Average Bread Price Per Year')
plt.xlabel('Year')
plt.ylabel('Average Price')
plt.grid(True)
plt.tight_layout()
plt.show()