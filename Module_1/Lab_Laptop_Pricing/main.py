import pandas as pd
import numpy as np

url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DA0101EN-Coursera/laptop_pricing_dataset_base.csv"
headers = ["Manufacturer", "Category", "Screen", "GPU", "OS", "CPU_core", "Screen_Size_inch", "CPU_frequency", "RAM_GB", "Storage_GB_SSD", "Weight_kg", "Price"]


data = pd.read_csv(url, header = None)
df = pd.DataFrame(data)
df.columns = headers
df.replace('?',np.nan, inplace = True)

#Add headers
print(df.head(10)) 

#Retrive data types
print(df.dtypes)

#Description
print(df.describe(include='all'))

#Summary
print(df.info())
