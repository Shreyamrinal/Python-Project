import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

# Load the dataset
data = pd.read_csv('dataset.csv')


# Print the first 5 rows of the dataset
print(data.head())

# Check for missing values
print("Missing Values:")
print(data.isnull().sum())

# Visualize missing data heatmap
plt.figure(figsize=(10, 6))
sns.heatmap(data.isnull(), cbar=False, cmap='viridis')
plt.title('Missing Data Heatmap')
plt.show()

# Fill missing values with column mean (for numeric columns)
data.fillna(data.mean(numeric_only=True), inplace=True)

# Print the first 5 rows of the dataset after data cleaning
print(data.head())

# Print the summary statistics of the dataset
print(data.describe())

# Identify the numerical columns in the dataset
numerical_cols = data.select_dtypes(include=np.number)

# Print the correlation matrix for the numerical columns
print(numerical_cols.corr())

# Visualize the correlation matrix using a heatmap
plt.figure(figsize=(10, 6))
sns.heatmap(numerical_cols.corr(), annot=True, cmap='coolwarm', square=True)
plt.title('Correlation Matrix')
plt.show()

# Identify outliers using the IQR method
Q1 = numerical_cols["Mean estimate of current perception for Household's Inflation Expectations"].quantile(0.25)
Q3 = numerical_cols["Mean estimate of current perception for Household's Inflation Expectations"].quantile(0.75)
IQR = Q3 - Q1

outliers = numerical_cols[(numerical_cols["Mean estimate of current perception for Household's Inflation Expectations"] < (Q1 - 1.5 * IQR)) | 
                         (numerical_cols["Mean estimate of current perception for Household's Inflation Expectations"] > (Q3 + 1.5 * IQR))]
print('Outliers:')
print(outliers)

# Visualize the outliers using a boxplot
plt.figure(figsize=(10, 6))
sns.boxplot(y="Mean estimate of current perception for Household's Inflation Expectations", data=data)
plt.title('Outlier Detection with IQR Method')
plt.show()

# Perform statistical analysis and hypothesis testing (2018 vs 2022)
perception_2018 = data[data['srcYear'] == 2018]["Mean estimate of current perception for Household's Inflation Expectations"]
perception_2022 = data[data['srcYear'] == 2022]["Mean estimate of current perception for Household's Inflation Expectations"]

# Perform independent t-test
t_stat, p_value = stats.ttest_ind(perception_2018.dropna(), perception_2022.dropna())
print(f"T-Statistic: {t_stat}, P-Value: {p_value}")

if p_value < 0.05:
    print("Significant difference in inflation perception between 2018 and 2022.")
else:
    print("No significant difference in inflation perception between 2018 and 2022.")

# Task 1: Explore the relationship between inflation perception and other variables
plt.figure(figsize=(10, 6))
sns.scatterplot(x='srcYear', y="Mean estimate of current perception for Household's Inflation Expectations", data=data)
plt.title('Relationship between Inflation Perception and Year')
plt.show()

# Task 2: Compare inflation perception across different states
plt.figure(figsize=(14, 8))  # Increase figure size
sns.barplot(x='Mean estimate of current perception for Household\'s Inflation Expectations', 
            y='srcStateName', data=data)  # Removed ci parameter
plt.title('Inflation Perception across States')
plt.xlabel('Mean Inflation Perception (%)')
plt.ylabel('States')
plt.grid(axis='x')  # Optional: add grid lines for better readability
plt.show()

# Task 3: Analyze the impact of various factors on inflation perception
plt.figure(figsize=(14, 8))
sns.lineplot(data=data, x='srcYear', 
             y="Mean estimate of current perception for Household's Inflation Expectations", 
             hue='srcStateName', marker='o')
plt.title('Inflation Perception Over Time by State')
plt.xlabel('Year')
plt.ylabel('Mean Inflation Perception (%)')
plt.legend(title='State', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.grid()
plt.show()