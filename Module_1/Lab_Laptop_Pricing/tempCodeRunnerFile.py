import pandas as pd
import numpy as np
from pyodide.http import pyfetch

file_path = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DA0101EN-Coursera/laptop_pricing_dataset_base.csv"
async def download(url, filename):
    response = await pyfetch(url)
    if response.status == 200:
        with open(filename, "wb") as f:
            f.write(await response.bytes())


await download(file_path, "laptops.csv")
file_name="laptops.csv"

df = pd.read_csv(file_name)