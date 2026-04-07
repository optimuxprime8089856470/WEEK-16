import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv("logs.csv")

df.columns=df.columns.str.strip()

df["timestamp"]=pd.to_datetime(df["timestamp"])

df=df.dropna()
df=df.drop_duplicates()

#login attack per ip

ip_counts=df["ip"].value_counts()

print("\n Top ip:", ip_counts.head())

#status code

status_counts=df["status"].value_counts()

print("\nstatus code: \n",status_counts)


#timebased attack

df["hour"]=df["timestamp"].dt.hour
hourly_attacks=df.groupby("hour").size()

print("\n Hourly activity:\n",hourly_attacks)

#visualisation top ip

plt.figure()
ip_counts.head(10).plot(kind="bar")
plt.title("Top 10 ip by requests")
plt.xlabel("ip address")
plt.ylabel("number of requests")
plt.xticks(rotation=45)
plt.show()

# visualization of status code
plt.figure()
status_counts.plot(kind="bar")
plt.title("status code data")
plt.xlabel("status code")
plt.ylabel("count")
plt.show()

#visualization of attack in time

plt.figure()
hourly_attacks.plot(kind="line")
plt.title("Request per hour")
plt.xlabel("hour of day")
plt.ylabel("Number of requests")
plt.grid()
plt.show()