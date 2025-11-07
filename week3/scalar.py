import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import StandardScaler
import pandas as pd 
shopping=pd.read_csv("shopping.csv")
print(shopping)


print("Min Max Scaler")
numeric_col=shopping.select_dtypes(include='number').columns
scaler=MinMaxScaler()
shopping_normalized=pd.DataFrame(scaler.fit_transform(shopping[numeric_col]),columns=numeric_col)
print(shopping_normalized.head())

print("Standard Scaler")

numeric_col1=shopping.select_dtypes(include="number").columns
scaler=StandardScaler()
shopping_standardized=pd.DataFrame(scaler.fit_transform(shopping[numeric_col1]),columns=numeric_col1)
print(shopping_standardized.head())

plt.figure(figsize=(8,6))
plt.hist(shopping['Avg_Price'],bins=10)
plt.title("Histogram")
plt.xlabel("Avg_Price")
plt.ylabel("Frequency")

plt.show()