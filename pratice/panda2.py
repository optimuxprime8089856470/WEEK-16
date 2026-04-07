import pandas as pd
import numpy as np

# s=pd.Series()
# print("pandas Series:", s)
# data= np.array(["g", "e", "e", "k", "s"])

# s=pd.Series(data)
# print("pandas Series:",s)


# df=pd.DataFrame()
# print(df)
# lst=["darwish", "muhammed ", "sinan", "salman"]
# df=pd.DataFrame(lst)
# print(df)


# df=pd.read_csv("nba.csv")
# print(df.info())

#selecting and filetering data

# df=pd.read_csv("nba.csv", index_col="Name")
# ages=df[df["Age"]> 30]
# print(type(ages))
# print(ages)

#Adding and removing columns

df=pd.read_csv("nba.csv", index_col="Name")

df["salary after tax"]= df["Salary"] * 0.7
print(df)