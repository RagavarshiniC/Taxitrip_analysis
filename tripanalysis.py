#Import The Necessary Libraries
import pandas as pd
import numpy as np
import datetime
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns
import calendar
data=pd.read_csv('/content/Uber Drives - .csv')
data.head()

#Check for Mising Values
data.isnull().any()
data.isnull().sum()

#dropping missing values
data=data.dropna()
data.isnull().sum()

data['START_DATE*'] = pd.to_datetime(data['START_DATE*'], format="%m/%d/%Y %H:%M")
data['END_DATE*'] = pd.to_datetime(data['END_DATE*'], format="%m/%d/%Y %H:%M")

hour=[]
day=[]
dayofweek=[]
month=[]
weekday=[]
for x in data['START_DATE*']:
    hour.append(x.hour)
    day.append(x.day)
    dayofweek.append(x.dayofweek)
    month.append(x.month)
    weekday.append(calendar.day_name[dayofweek[-1]])
data['HOUR']=hour
data['DAY']=day
data['DAY_OF_WEEK']=dayofweek
data['MONTH']=month
data['WEEKDAY']=weekday
data.head()

#Categories
data['CATEGORY*'].value_counts()
sns.countplot(x='CATEGORY*',data=data)

#How long do people travel with Uber?
data['MILES*'].plot.hist()

#What Hour Do Most People Take Uber?
hours = data['START_DATE*'].dt.hour.value_counts()
hours.plot(kind='bar',color='red',figsize=(10,5))
plt.xlabel('Hours')
plt.ylabel('Frequency')
plt.title('Number of trips Vs hours')

#Check The Purpose Of Trips
data['PURPOSE*'].value_counts().plot(kind='bar',figsize=(10,5),color='brown')

#Which Day Has The Highest Number Of Trips
data['WEEKDAY'].value_counts().plot(kind='bar',figsize=(10,5),color='blue')

#What Are The Number Of Trips Per Each Day?
data['DAY'].value_counts().plot(kind='bar',figsize=(10,5),color='green')

#What Are The Trips In The Month
data['MONTH'].value_counts().plot(kind='bar',figsize=(10,5),color='black')

#The starting points of trips. Where Do People Start Boarding Their Trip From Most?
data['START*'].value_counts().plot(kind='bar',figsize=(25,10),color='blue')

