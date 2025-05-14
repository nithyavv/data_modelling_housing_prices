import pandas as pd

try:
    df = pd.read_csv('housing.csv')
    print(df.head())
except FileNotFoundError:
    print("Error: 'housing.csv' not found. Please ensure the file is in the current working directory or provide the correct path.")
    df = None # Assign None to df in case of error
except Exception as e:
    print(f"An unexpected error occurred: {e}")
    df = None

# Examine the data types of each column
print("\nData types of each column:\n", df.dtypes)

# Generate descriptive statistics for numerical columns, handling potential errors
try:
    numerical_stats = df.describe(include='number')
    print(numerical_stats)
except Exception as e:
    print(f"\nAn error occurred while generating descriptive statistics: {e}")
    # Attempt to identify the problematic columns and exclude them
    for col in df.columns:
      try:
        df[col].astype(float)
      except:
        print(f"Column '{col}' has mixed data types and was excluded from descriptive statistics.")
# Identify columns with missing values
missing_values = df.isnull().sum()
missing_percentage = (missing_values / len(df)) * 100
missing_data = pd.DataFrame({'Missing Values': missing_values, 'Percentage': missing_percentage})
print (missing_data)

# Analyze unique values in 'ocean_proximity'
ocean_proximity_counts = df['ocean_proximity'].value_counts()
print (ocean_proximity_counts)

# Summarize findings
print("Summary:")
print("Missing Values Analysis:")
print(missing_data)
print("\nUnique Values in 'ocean_proximity':")
print(ocean_proximity_counts)
