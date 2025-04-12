📊 Inflation Perception Analysis (2018 vs 2022)

This project involves exploratory data analysis and statistical testing on household inflation expectations using survey data across different states and years in India. It focuses on identifying trends, outliers, and relationships in inflation perception, particularly comparing the years 2018 and 2022.

Output:

![image](https://github.com/user-attachments/assets/3cbc919f-d42b-45d5-a95f-91d2871a084a)

![image](https://github.com/user-attachments/assets/ee537289-1cf4-4aa3-888e-03b0aeaeee57)

![image](https://github.com/user-attachments/assets/c57a3a91-5953-4a0d-871a-1315aa4e3acb)

![image](https://github.com/user-attachments/assets/8da1c361-18db-4f46-9786-49afaf44a772)

![image](https://github.com/user-attachments/assets/fbf52741-2613-4cfa-81ca-6e833e6a4de0)

![image](https://github.com/user-attachments/assets/8e419164-b708-4e99-8b8f-331bb839b7d8)







🧠 Objectives
Clean and preprocess the dataset

Visualize missing data and handle it appropriately

Detect outliers using the IQR method

Explore relationships between inflation perception and various factors

Compare inflation perception across years and states

Perform hypothesis testing to check for significant changes over time

📁 Dataset
The dataset is read from a CSV file named 6720_source_data.csv which includes:

srcYear: Year of the survey

srcStateName: State name

Mean estimate of current perception for Household's Inflation Expectations: Key numeric variable for inflation perception

Other numeric and categorical features related to household inflation expectations

🧹 Data Cleaning
Missing values are visualized using a heatmap.

Missing numerical values are filled using column-wise mean imputation.

📈 Exploratory Data Analysis
Summary statistics and correlation matrix for numerical columns

Correlation heatmap to identify strong/weak relationships

Boxplot and IQR method to identify outliers in inflation perception

📊 Visualizations
Scatter plot: Relationship between perception and year

Bar chart: Mean inflation perception across different states

Line chart: Trend of perception over time for each state

📐 Statistical Analysis
A two-sample independent t-test is used to compare the inflation perception between 2018 and 2022:

python
Copy
Edit
stats.ttest_ind(perception_2018, perception_2022)
p-value < 0.05 indicates a statistically significant difference in perception between the two years.

📌 Key Python Libraries Used
pandas for data handling

numpy for numerical operations

matplotlib and seaborn for visualizations

scipy.stats for hypothesis testing

🧪 How to Run
Clone this repository

Place your dataset file as 6720_source_data.csv in the root directory

Run the script in any Python environment with the required libraries installed

bash
Copy
Edit
pip install pandas numpy matplotlib seaborn scipy
🔍 Future Improvements
Automate outlier removal or flagging

Add interactive plots using Plotly

Incorporate time-series analysis methods

📃 License
This project is open-source and available under the MIT License.

