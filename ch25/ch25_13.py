# ch25_13.py
import pandas as pd

course = ['Chinese', 'English', 'Math', 'Natural', 'Society']
x = pd.read_csv("out25_12a.csv",index_col=0)
y = pd.read_csv("out25_12b.csv",names=course)
print(x)
print(y)







