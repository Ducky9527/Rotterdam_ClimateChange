import pandas as pd

#import Rotterdam data & parse the dates

df = pd.read_csv('rotterdam_temparature/data/RD1980_2022.csv', parse_dates = ["YYYYMMDD"])

#clean up the dataset by removing unnecessary rows
df = df.drop(columns = ["STN", "TNH", "TXH"])



#add a separate column for "year", "month", "dat"
df['Year'] = df['YYYYMMDD'].dt.year
df['Month'] = df['YYYYMMDD'].dt.month
df['Day'] = df['YYYYMMDD'].dt.day

#rearrange columns
df = df[["YYYYMMDD","Year", "Month","Day", "TG", "TX"]]
df = df.rename(columns={"TG" : "AVG", "TX" : "Max", "TN" : "Min"})



#select the summer
#  testing the code by sampling
df = df[df.Month.isin([6, 7, 8])].sort_index(ascending=True).sample(5)

#works, remove the sampling part
df = df[df.Month.isin([6, 7, 8])]

#reset index for the extracted data
#df.reset_index(drop=True, inplace=True)
df = df.set_index("YYYYMMDD")

#df = df.reset_index(drop=True)
print(df)



# generate a new csv
df.to_csv("RD1980_2022_summer", index = False)
