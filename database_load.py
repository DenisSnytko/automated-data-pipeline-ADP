import pandas as pd
import sqlite3
from tkinter import filedialog

##Connect to Database
datapath = filedialog.askopenfilename(
    title="Select a Database",
    filetypes=(("db files", "*.db"), ("all files", "*.*"))
)

if not datapath:
    print("Process canceled")
else:
    try:
        conn = sqlite3.connect(datapath)
        print("Database connected")

        ##Import Dataset
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
                df.to_sql("sales", conn, if_exists="replace", index=False)
            except FileNotFoundError:
                print("File not found")
            except Exception as e:
                print(f"An error has occurred: {e}")
        
    except FileNotFoundError:
        print("Database not found")
    except Exception as e:
        print(f"An error has occurred: {e}")