## Automated Data Pipeline (ADP): CSV-File Cleanup
import pandas as pd
from tkinter import filedialog


## Step 1: Import Dataset
filepath = filedialog.askopenfilename(
    title="Select a File",
    filetypes=(("csv files", "*.csv"), ("all files", "*.*"))
)

# Check, if User canceled the Process
if not filepath:
    print("Process canceled")
else:
    try:
        df = pd.read_csv(filepath)
        print("File loaded successful")
    except FileNotFoundError:
        print("File not found")
    except Exception as e:
        print(f"An error has occurred: {e}")

    
## Step 2: Fix Column-Names
df.columns = (
    df.columns
    .str.strip()
    .str.lower()
    .str.replace(" ", "")
    .str.replace("[()€$%-_]", "", regex=True)
)


## Step 3: Fix the Date-Columns
date_cols = ["orderdate", "shipingdate", "shipdate", "date", "joindate"]

for col in date_cols:
    try:
        df[col] = pd.to_datetime(df[col], errors= "coerce", format="mixed")
    except:
        continue


## Step 4: Fix Currency-Columns
money_cols = ["unitprice", "price", "shippingcost", "cost", "ordertotal", "order", "sale", "sales", "salary", "total"]

for col in money_cols:
    try:
        df[col] = (
            df[col]
            .astype(str)
            .str.replace("$", "", regex=False)
            .str.replace("USD", "", regex=False)
            .str.replace("€", "", regex=False)
            .str.strip()
        )
        df[col] = pd.to_numeric(df[col], errors="coerce")
    except:
        continue


## Step 5: Fix Percentage-related Columns
percentage_cols = ["discount", "taxrate", "tax", "taxes"]

for col in percentage_cols:
    try:
        df[col] = (
            df[col]
            .astype(str)
            .str.replace("%", "", regex=False)
            .str.strip()
        )
        df[col] = pd.to_numeric(df[col], errors="coerce")
        df.loc[df[col] > 1, col] = df[col] / 100
    except:
        continue


## Step 6: Fix Quantity-related Columns
quantity_cols = ["quantity", "amount", "age"]

for col in quantity_cols:
    try:
        df[col] = pd.to_numeric(df[col], errors="coerce")
        df[col] = df[col].fillna(1)
    except:
        continue


## Step 7: Fix Text-related Columns
text_cols = [
    "city", "country", "region","state", "saleschannel","category","subcategory","notes","customername", "segment", "productname",
    "firstname", "lastname", "departmentregion", "status", "phone", "performancescore", "remotework", "product", "paymentmethod"
    ]

for col in text_cols:
    try:
        df[col] = (
            df[col]
            .str.strip()
            .str.lower()
            .str.replace(" ", "_")
            .str.replace("-", "_")
            .str.replace("[()€$%]", "", regex=True)
        )
    except:
        continue


## Step 8: Remove Duplicates
df.shape
df = df.drop_duplicates()
df.shape


## Step 9: Final Inspection
df.info()


## Step 10: Export Clean CSV-File
filepath = filepath.rsplit("/")
filename = filepath[-1]
df.to_csv("cleaned_" + filename, index=False)