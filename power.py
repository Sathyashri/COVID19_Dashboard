import pandas as pd
file_path = r"C:\Users\sathy\OneDrive\Documents\COVID-19\worldometer_coronavirus_daily_data.csv"
covid_data = pd.read_csv(file_path)
print("✅ File loaded successfully!")
print("\n--- Shape ---")
print(covid_data.shape)
print("\n--- Column names ---")
print(covid_data.columns.tolist())
print("\n--- Missing values (top 10 columns) ---")
print(covid_data.isnull().sum().head(10))
print("\n--- Sample rows ---")
print(covid_data.head(5))