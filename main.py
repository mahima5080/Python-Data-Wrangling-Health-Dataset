import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Load Dataset
df = pd.read_csv('data.csv')

# 2. Fix Date Format & Convert to Datetime
df['Date'] = pd.to_datetime(df['Date'].astype(str).str.replace("'", "").str.strip(), errors='coerce')

# 3. Handle Missing Values
# Drop rows where Date is missing (Row 22)
df.dropna(subset=['Date'], inplace=True)

# Impute missing Calories (Rows 18 and 28) with column median
df['Calories'] = df['Calories'].fillna(df['Calories'].median())

# 4. Correct Outliers / Data Entry Errors
# Row 7 duration of 450 minutes is capped/corrected to 45 minutes
df.loc[df['Duration'] > 120, 'Duration'] = 45

# 5. Remove Duplicates
df.drop_duplicates(inplace=True)

# 6. Create New Column (Feature Engineering)
df['Calorie_Burn_Rate'] = (df['Calories'] / df['Duration']).round(2)

# Save Cleaned Dataset
df.to_csv('cleaned_health_data.csv', index=False)
print("Data Cleaning Complete! Cleaned dataset saved to 'cleaned_health_data.csv'.")
print("\nCleaned Dataset Head:")
print(df.head())

# 7. Data Visualization
plt.figure(figsize=(8, 5))
sns.scatterplot(data=df, x='Duration', y='Calories', hue='Pulse', size='Maxpulse', palette='viridis', sizes=(50, 200))
plt.title('Workout Duration vs Calories Burned', fontsize=12, fontweight='bold')
plt.xlabel('Duration (minutes)')
plt.ylabel('Calories Burned')
plt.grid(True, linestyle='--', alpha=0.5)
plt.tight_layout()
plt.show()