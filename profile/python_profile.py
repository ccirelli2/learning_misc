import cProfile
import pstats
import io
from pstats import SortKey
import pandas as pd


# Create Instance of Profile Class
pr=cProfile.Profile()
# Enable Class to start collecting data
pr.enable()
# Functions
df=pd.DataFrame({})
df['A']=[1,2,3,4]
df=df.transpose()
print(df)
# Disable Class to stop collecting data
pr.disable()
# Create Format For Statistics
s=io.StringIO()
sortby=SortKey.CUMULATIVE
ps=pstats.Stats(pr, stream=s).sort_stats(sortby)
# Print Status to Stdout
ps.print_stats()
print(s.getvalue())




