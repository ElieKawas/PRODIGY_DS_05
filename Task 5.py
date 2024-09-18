import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv("C:/Users/hp/Desktop/Intership/Prodigy Task 5/US_Accidents_March23.csv")
print(df.head())
print(df.shape)

# Check for missing values
missing = df.isnull().sum()
print(missing)

print("Removing missing values:")
df = df.dropna()
missing = df.isnull().sum()
print(missing)

print(df.info())

# Visualization

# Top 20 cities with highest accidents
accident_per_city = df.City.value_counts()
accident_per_city[:20].sort_values(ascending=True).plot(kind='barh')
plt.title("Top 20 Cities with Highest Accidents")
plt.show()

# Accident severity
sns.countplot(x="Severity", data=df)
plt.title("Distribution of Accident Severity")
plt.xlabel("Severity")
plt.ylabel("Number of Accidents")
plt.show()

# Ensure Start_Time is in datetime format
df['Start_Time'] = pd.to_datetime(df['Start_Time'], errors='coerce')

# Extract year, month, and day from Start_Time
df['Year'] = df['Start_Time'].dt.year
df['Month'] = df['Start_Time'].dt.month
df['Day'] = df['Start_Time'].dt.day

# Plot number of accidents by year
accidents_per_year = df['Year'].value_counts().sort_index()
plt.figure(figsize=(10, 6))
accidents_per_year.plot(kind='bar', color='purple')
plt.title("Number of Accidents per Year")
plt.xlabel("Year")
plt.ylabel("Number of Accidents")
plt.show()

# Plot number of accidents by month
accidents_per_month = df['Month'].value_counts().sort_index()
plt.figure(figsize=(10, 6))
accidents_per_month.plot(kind='bar', color='orange')
plt.title("Number of Accidents per Month")
plt.xlabel("Month")
plt.ylabel("Number of Accidents")
plt.xticks(ticks=np.arange(12), labels=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
plt.show()

# Plot number of accidents by day
accidents_per_day_10 = df[df['Day'] <= 10]['Day'].value_counts().sort_index()

# Plot number of accidents for the first 10 days
plt.figure(figsize=(10, 6))
accidents_per_day_10.plot(kind='bar', color='green')
plt.title("Number of Accidents for the First 10 Days of the Month")
plt.xlabel("Day")
plt.ylabel("Number of Accidents")
plt.xticks(ticks=np.arange(1, 11), labels=np.arange(1, 11))
plt.show()

# Day/Night Distribution
pie, ax = plt.subplots(figsize=[6, 6])
labels = df.Sunrise_Sunset.value_counts().keys()
plt.pie(x=df.Sunrise_Sunset.value_counts(), autopct="%.1f%%", explode=[0.01]*len(labels), labels=labels, pctdistance=0.5)
plt.title("Day/Night Distribution of Accidents")
plt.show()

# Ensure Start_Time is in datetime format for final_data
df['Start_Time'] = pd.to_datetime(df['Start_Time'], errors='coerce')
df['Month'] = df['Start_Time'].dt.month
df['Year'] = df['Start_Time'].dt.year
df['Hour'] = df['Start_Time'].dt.hour
df['Weekday'] = df['Start_Time'].dt.weekday

# Yearly data subset
data_2016 = df[df['Start_Time'].dt.year == 2016]
data_2017 = df[df['Start_Time'].dt.year == 2017]
data_2018 = df[df['Start_Time'].dt.year == 2018]
data_2019 = df[df['Start_Time'].dt.year == 2019]
data_2020 = df[df['Start_Time'].dt.year == 2020]
data_2017_2019 = df[(df["Year"] >= 2017) & (df["Year"] <= 2019)]

fig, ax = plt.subplots(figsize=(10, 5))
c = sns.countplot(x="Year", data=df, orient='v', palette="crest")
plt.annotate('Data Not Available', xy=(-0.4, 500000), fontsize=11)
c.set_title("Number of Accidents by Year")
for i in ax.patches:
    count = '{:,.0f}'.format(i.get_height())
    x = i.get_x() + i.get_width() - 0.60
    y = i.get_height() + 10000
    ax.annotate(count, (x, y))
plt.show()
