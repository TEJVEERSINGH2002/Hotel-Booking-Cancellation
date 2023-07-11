#!/usr/bin/env python
# coding: utf-8

# # Buisness Problem

# In recent years, City Hotel and Resort Hotel have seen high cancellation rates. Each hotel is now dealing with a number of issues as a result, including fewer revenues and less than ideal hotel room use. Consequently, lowering cancellation rates is both hotels primary goal in order to increase thier efficiency in genrating revenue and for us to offer thorough buisness avise to address this problem.

# In[1]:


# create a Problem Statement.

# Identify the data you want to analyze.

# Explore and Clean the data.

# Analyze the data to get useful insights.

# Present the Data in terms of reports or dasshboards using visualization.


# # code started

# # Importing Libraries

# In[2]:


import pandas as pd
import numpy as np
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')
from matplotlib import pyplot as plt


# # Loading the dataset

# In[3]:


df = pd.read_csv("C:/Users/tejveerseoli/Downloads/hotel_bookings 2.csv")


# In[4]:


df


# # Exploratory Data Analysis and Data Cleaning

# In[5]:


df.head()


# In[6]:


df.tail()


# In[7]:


df.shape


# In[8]:


df.columns


# In[9]:


df.info()


# In[10]:


df['reservation_status_date'] = pd.to_datetime(df['reservation_status_date'])


# In[11]:


df.info()


# In[12]:


df.describe(include = 'object')


# In[13]:


for col in df.describe(include = 'object').columns:
    print(col)
    print(df[col].unique())
    print('-'*50)


# In[14]:


df.isnull().sum()


# In[15]:


df.drop(['company','agent'], axis =1,inplace = True)
df.dropna(inplace = True)


# In[16]:


df.isnull().sum()


# In[17]:


df.describe()


# In[18]:


df['adr'].plot(kind = 'box')


# In[19]:


df = df[df['adr']<5000]


# # Data Analysis and Visualizations

# In[20]:


cancelled_perc = df['is_canceled'].value_counts(normalize = True)
print(cancelled_perc)

plt.figure(figsize = (5,4))
plt.title("Reservation Status Count")
plt.bar(['Not canceled','Canceled'],df['is_canceled'].value_counts(),edgecolor = 'k', width = 0.7)
plt.show()


# In[21]:


plt.figure(figsize = (8,4))
ax1 = sns.countplot(x = 'hotel', hue = 'is_canceled', data = df, palette = 'Blues')
legend_labels,_= ax1. get_legend_handles_labels()
#ax1.legend(bbox_to_anchor(1,1))
plt.title('Reservation status in different hotels', size = 20)
plt.xlabel('hotel')
plt.ylabel('number of reservations')
plt.show()


# In[22]:


resort_hotel = df[df['hotel'] == 'Resort Hotel']
resort_hotel['is_canceled'].value_counts(normalize = True)


# In[23]:


city_hotel = df[df['hotel'] == 'City Hotel']
city_hotel['is_canceled'].value_counts(normalize = True)


# In[24]:


resort_hotel = resort_hotel.groupby('reservation_status_date')[['adr']].mean()
city_hotel = city_hotel.groupby('reservation_status_date')[['adr']].mean()


# In[25]:


plt.figure(figsize = (20,8))
plt.title('Average Daily Rate in City and Resort Hotel', fontsize = 30)
plt.plot(resort_hotel.index, resort_hotel['adr'], label = 'Resort Hotel')
plt.plot(city_hotel.index, city_hotel['adr'], label = 'City Hotel')
plt.legend(fontsize = 20)
plt.show()


# In[26]:


df['month'] = df['reservation_status_date'].dt.month
plt.figure(figsize = (16,8))
ax1 = sns.countplot(x = 'month', hue = 'is_canceled', data = df, palette = 'bright')
#legend_labels,_ax1. get_legend_labels()
#ax1.legend(bbox_to_anchor = (1,1))
plt.title('Reservation status per month', size = 20)
plt.xlabel('Month')
plt.ylabel('Number of Reservations')
plt.legend(['Not canceled','Canceled'])
plt.show()


# In[27]:


plt.figure(figsize = (15,8))
plt.title('ADR per month', fontsize = 30)
sns.barplot('month', 'adr', data = df[df['is_canceled'] == 1].groupby('month')[['adr']].sum().reset_index())

plt.show()


# In[28]:


cancelled_data = df[df['is_canceled'] == 1]
top_10_country = cancelled_data['country'].value_counts()[:10]
plt.figure(figsize = (8,8))
plt.title('Top 10 countries with reservation canceled')
plt.pie(top_10_country, autopct = '%.2f', labels = top_10_country.index)
plt.show()


# In[29]:


df['market_segment'].value_counts()


# In[30]:


df['market_segment'].value_counts(normalize = True)


# In[31]:


cancelled_df_adr = cancelled_data.groupby('reservation_status_date')[['adr']].mean()
cancelled_df_adr.reset_index(inplace = True)
cancelled_df_adr.sort_values('reservation_status_date', inplace = True)

not_cancelled_df = df[df['is_canceled'] == 0]
not_cancelled_df_adr = not_cancelled_df.groupby('reservation_status_date')[['adr']].mean()
not_cancelled_df_adr.reset_index(inplace = True)
not_cancelled_df_adr.sort_values('reservation_status_date', inplace = True)

plt.figure(figsize = (20,6))
plt.title('Average Daily Rate')
plt.plot(not_cancelled_df_adr['reservation_status_date'],not_cancelled_df_adr['adr'], label = 'not cancelled')
plt.plot(cancelled_df_adr['reservation_status_date'],cancelled_df_adr['adr'], label = 'cancelled')
plt.legend()


# In[32]:


cancelled_df_adr = cancelled_df_adr[(cancelled_df_adr['reservation_status_date']>'2016') & (cancelled_df_adr['reservation_status_date']<'2017-09')]
not_cancelled_df_adr = not_cancelled_df_adr[(not_cancelled_df_adr['reservation_status_date']>'2016') & (not_cancelled_df_adr['reservation_status_date']<'2017 - 09')]


# In[33]:


plt.figure(figsize = (20,6))
plt.title('Average Daily Rate', fontsize = 40)
plt.plot(not_cancelled_df_adr['reservation_status_date'],not_cancelled_df_adr['adr'],label = 'not cancelled')
plt.plot(cancelled_df_adr['reservation_status_date'],cancelled_df_adr['adr'], label = 'cancelled')
plt.legend(fontsize = 20)
plt.show()


# # Code Ended

# # Assumptions

# 1. No unusal occurence between 2015 and 2017 will have a sustantial impact on the data used.
# 2. The information is still current and can be used to analyze a hotel's possible plans in an efficent manner.
# 3. There are no unanticipated negatives to the hotel employing any advised techniques.
# 4. The hotels are not currently using any of suggested solutions.
# 5. The biggest factor affecting the effectiveness of earning income is booking cancellations.
# 6. Clients make hotel reservations the same year they make cancellations.

# # Research Question

# 1. What are the variables that affect hotel reservation cancellations?
# 2. How can we make hotel reservation cancelling better?
# 3. How will hotels be assisted in making price and promotional decisions?

# # Hypothesis

# 1. More cancellation occur when prices are higher.
# 2. When there is a longer waiting list customers tend to cancel more frequently.
# 3. The majority of clients are coming from offline travel agents to make their reservations.

# # Analysis and Findings

# 1. The accompanying bar graph shows the percentage of reservations that are canceled and those that are not. It is obvious that there are still a significant number of reservation that have not been canceled. There are still 37% of clients who canceled
# their reservation, which has significant impact on hotel's earning.

# 2. In comparison to resort hotels, city hotels have more bookings. It's possible that resort hotels are more expensive than those in cities.

# 1. Cancellation rates rise as the price does. In order to prevent cancellations of reservations, hotels could work on their pricing strategies and try to lower the rates for specific hotels based on locations. They can also provide some discount to the consumers.
# 
# 2. As the ratio of the cancellation and not cancellation of the resort hotel is higher in the resort hotel than the city hotels. So the hotels should provide as resonable discount on the room prices on weekends or on holidalys.
# 
# 3. In the month of January, hotels can start campaigns or marketing with a resonable amount to increase thier revenue as the cancellation is highest in this month.
# 
# 4. They can also increase the quality of thier hotels and their services mainly in Portugal to reduce the cancellaton rates.

# 3. The line graph above shows that, on certain days.the average daily rate for a city hotel is less than that of a resort hotel, and on other days, it is even less. It goes without saying that weeends and holidays may see a rise in resort hotel rates.

# 4. We have developed the grouped bar graph to analyze the month with the highest and lowest reservation levels according to reservation levels according to reservation status. As can be seen , both the number of confirmed reservations and the number of canceled reservation are largest in the mont of Agust. whereas January is the month with the most canceled reservations.

# 5. The pie chart shows the top 10 country which has highest reservation cancelled. The top country is Portgual with the highest number of cancellations.

# 6. Lets check the area form where guests are visiting the hotels and making reservatons. Is it coming from Direct or Groups, Online or offline Travel agents? Around 46% of the clients come from online tavel agencies, wheras 27% come from groups. Only 4% of clients book hotels directly by visiting them and making reservations.

# 7. As seen in the graph, reservations are cancelled when the average daily rate is higher than when it is not cancelled. It clearly proves all the above analysis, that the higher price leads to higher cancellation.

# # Suggestions

# In[ ]:




