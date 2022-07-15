import pandas as pd

# import Rotterdam data & parse the date


# the data was downloaded from "https://daggegevens.knmi.nl/" 
# STN         LON(east)   LAT(north)  ALT(m)      NAME
# 344         4.447       51.962      -4.30       Rotterdam   
# TG        : Daily mean temperature in (0.1 degrees Celsius)
# TN        : Minimum temperature (in 0.1 degrees Celsius)
# TX        : Maximum temperature (in 0.1 degrees Celsius)
# TNH = the hour when the temp was the lowest
# TXH = the hour when the temp was the highest
df = pd.read_csv('rotterdam_temparature/RD1980_2022.csv', parse_dates = ["YYYYMMDD"])

# clean up the dataset by removing unnecessary rows
df = df.drop(columns = ["STN", "TNH", "TXH"])

# add a separate column for "year" 
# because we will need this column for counting how many days in a year 
# fulfill the criteria that 
# (1) the avg temp of the day was above 25C, or 
# (2) the highest temp of the day was above 30C
df['Year'] = df['YYYYMMDD'].dt.year


#filtering out the days that fulfill either of the two criteria
dff_1 = df.loc[(df["TX"] > 300) | (df["TG"] > 250)]
print(dff_1)

#filtering out the days that fulfill the two criteria
dff_2 = df.loc[(df["TX"] > 300) & (df["TG"] > 250)]
print(dff_2)


#count how many days each year(from 1980 to 2022 today) fulfill either of the two criteria  
dff_count_1 = dff_1.groupby(["Year"])["Year"].count()
print(dff_count_1)


#count how many days each year(from 1980 to 2022 today) fulfill the two criteria  
dff_count_2 = dff_2.groupby(["Year"])["Year"].count()
print(dff_count_2)





