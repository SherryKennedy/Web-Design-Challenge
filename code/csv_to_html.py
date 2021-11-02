import pandas as pd
import os
# looking at difference of running .py file in VSCODE and .ipynb code in VSCODE

# note, .py file in VSCODE runs paths from the working directory
# Read the csv file in
print(os.getcwd())  # working directory 

# look where path running from is
MYDIR = os.path.dirname(__file__)
print(f'hello: {MYDIR}')

# Read cities.csv file 
df = pd.read_csv("data/cities.csv")

# Naming the index, works with index=False
df.index.name=None

# Save to file 
df.to_html('data.html', index=False, classes='table table-striped')
