"""
Initialisations
"""
# Standard Library imports
from pathlib import Path

# Thirds Party Libraries
import pandas as pd
from plotnine import ggplot, aes, geom_bar, geom_col

# Globals
file_name = "us_names_by_decade.csv"
data_directory = "data"
file_path = Path.cwd() / data_directory / file_name

"""
Read in the data and do some basic analysis
"""

table = pd.read_csv(file_path)


print(table.filter())
