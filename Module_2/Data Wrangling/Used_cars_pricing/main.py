import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# File URL
file = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DA0101EN-SkillsNetwork/labs/Data%20files/auto.csv"

# Define headers for the data
headers = [
    "symboling", "normalized-losses", "make", "fuel-type", "aspiration", "num-of-doors", "body-style",
    "drive-wheels", "engine-location", "wheel-base", "length", "width", "height", "curb-weight", "engine-type",
    "num-of-cylinders", "engine-size", "fuel-system", "bore", "stroke", "compression-ratio", "horsepower",
    "peak-rpm", "city-mpg", "highway-mpg", "price"
]

# Load the dataset
df = pd.read_csv(file, names=headers)

# Section 1: Identify and handle missing values
# Convert "?" to NaN
df.replace("?", np.nan, inplace=True)

# Display the first 5 rows of the dataset
print(df.head(5))

# Evaluate missing data
missing_data = df.isnull()
print(f"Evaluating for missing data: {missing_data.head(5)}")

# Count missing values in each column
for column in missing_data.columns.values.tolist():
    print(column)
    print(missing_data[column].value_counts())
    print("")

# Calculate mean values for columns with missing values and fill them in
avg_norm_loss = df['normalized-losses'].astype("float").mean(axis=0)
df['normalized-losses'].replace(np.nan, avg_norm_loss, inplace=True)

avg_stroke = df["stroke"].astype("float").mean(axis=0)
df["stroke"].replace(np.nan, avg_stroke, inplace=True)

avg_horsepower = df['horsepower'].astype('float').mean(axis=0)
df['horsepower'].replace(np.nan, avg_horsepower, inplace=True)

avg_peakrpm = df['peak-rpm'].astype('float').mean(axis=0)
df['peak-rpm'].replace(np.nan, avg_peakrpm, inplace=True)

# Convert "horsepower" column to numeric, replacing non-numeric entries with NaN and then filling NaN with mean
df["horsepower"] = pd.to_numeric(df["horsepower"], errors="coerce")
df["horsepower"].fillna(df["horsepower"].mean(), inplace=True)

# Data transformation
# Convert "highway-mpg" to "highway-L/100km"
df["highway-mpg"] = 235 / df["highway-mpg"]
df.rename(columns={"highway-mpg": "highway-L/100km"}, inplace=True)

# Normalize "height" column by its maximum value
df['height'] = df['height'] / df['height'].max()

# Show normalized columns
print(df[["length", "width", "height"]].head())

# Plot histogram for "horsepower" column
plt.hist(df["horsepower"], bins=3)
plt.xlabel("horsepower")
plt.ylabel("count")
plt.title("Horsepower bins")
plt.show()

# Create dummy variables for the "aspiration" column
dummy_variable_2 = pd.get_dummies(df['aspiration'])
dummy_variable_2.rename(columns={'std': 'aspiration-std', 'turbo': 'aspiration-turbo'}, inplace=True)

# Concatenate dummy variables to the main dataframe and drop the original "aspiration" column
df = pd.concat([df, dummy_variable_2], axis=1)
df.drop('aspiration', axis=1, inplace=True)

# Display the first 5 rows of the updated dataframe
print(df.head())
