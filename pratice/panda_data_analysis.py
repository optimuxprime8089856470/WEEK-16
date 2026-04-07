import pandas as pd
import numpy as np

# d={"First score": [100, 200, 300,np.nan,950],
#    "Second score": [51, 5451, 415, 652, np.nan],
#    "Third score": [41, 512, np.nan, 489, 985]}

# df=pd.DataFrame(d)
# mv=df.isnull()
# print(mv)

#filetering data basedon the the missing values

# df=pd.read_csv("employees.csv", index_col="First Name")

# bool_series=pd.isnull(df["Gender"])
# missing_gender_data=df[bool_series]
# print(missing_gender_data)


#using isna() method

# data={"Name": ["darwish", "muhammed", np.nan, "salman"],
#       "Age": [20, 21, np.nan, 23]}
# df=pd.DataFrame(data)
# print(df.isna())


#checking for non missing values using notnull() method

# data={"first score": [100, 200, 300, np.nan, 950],
#     "second score": [51, 5451, 415, 652, np.nan],
#     "third score": [41, 512, np.nan, 489, 985]}

# df=pd.DataFrame(data)
# print(df.notnull())

#fillna() method to fill the missing values

# data={"first score": [100, 200, 300, np.nan, 950],
#     "second score": [51, 5451, 415, 652, np.nan],
#     "third score": [41, 512, np.nan, 489, 985]}
# df=pd.DataFrame(data)
# print(df.fillna(0))

df=pd.read_csv("employees.csv", index_col="First Name")
df["Gender"]=df["Gender"].fillna("Transformers")
print(df.head(25))



