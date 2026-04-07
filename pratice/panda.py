import pandas as pd
#list
# list1=["darwish", "muhammed ", "sinan", "salman"]
# df=pd.DataFrame(list1)
# print(df)

#dictionary
# data={"name":["darwish", "muhammed", "sinan", "salman"],
#       "age":[20, 21, 22, 23],
#       "city":["amman", "irbid", "zarqa", "aqaba"]}
# df=pd.DataFrame(data)
# print(df)

#column selection
# data={"name":["darwish", "muhammed", "sinan", "salman"],
#       "age": [20, 21, 22, 23],
#       "city": ["puthussery", "kerala", "kondotty", "kannur"],
#       "qualification": ["bsc", "msc", "phd", "diploma"]}

# df=pd.DataFrame(data)
# print(df[["name", "qualification"]])


#row selection
# data=pd.read_csv("nba.csv", index_col="Name")

# #retreiving row by loc method
# first=data.loc["Avery Bradley"]
# second=data.loc["R.J. Hunter"]

# print(first, "\n\n", second)

#row selection by multiple rows

# data=pd.read_csv("nba.csv", index_col="Name")

# rows=data.loc[["Avery Bradley", "R.J. Hunter"]]

# print(type(rows))
# print(rows)

#Extracting multiple rows with same index

# data=pd.read_csv("nba.csv", index_col="Team")
# rows=data.loc["Utah Jazz"]
# print(type(rows))
# print(rows)

#Extracting rows between two index labels

data=pd.read_csv("nba.csv", index_col="Name")

rows=data.loc["Avery Bradley": "R.J. Hunter"]
print(type(rows))
print(rows)
