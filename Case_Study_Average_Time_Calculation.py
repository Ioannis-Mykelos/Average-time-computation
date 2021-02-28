#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
from datetime import datetime, timedelta
import matplotlib.pyplot as plt
data=pd.read_csv("case_data.csv")

# We created an new Dataframe with the event category only for lesson.
data_2=data[data["event_category"]!="lesson"]

# We sorted the table by tstamp and device_id in an ascending order.
sortedata_2=data_2.sort_values(by=['tstamp', "device_id"], ascending=True)
# print(sortedata_2)


# In[3]:


""" Made a list with the unique device_id's """
list_device_id=[]
for item in data["device_id"]:
    list_device_id.append(item)
list_device_id=list(dict.fromkeys(list_device_id))
print(len(list_device_id))


# In[4]:


""" Create a list with elements the time stamps, with lenght = 182,136"""
from datetime import datetime, timedelta
time_spent_list_for_each_device_id=[]
time_spent_list=[]
time_stamp_list=[]

for item in list_device_id:
    data_3=data_2[data_2["device_id"]==item]
    for i,j in data_3.iterrows():
        time_stamp_list.append(j[2])
r=len(time_stamp_list)
print(r)


# In[5]:


"""Compute the sum of hours spent in each device id"""
sum_of_hours_list=[]
for item in list_device_id:
    data_3=data_2[data_2["device_id"]==item]
    temp_time_stamp_list=[]
    for i,j in data_3.iterrows():
        temp_time_stamp_list.append(j[2])
    r=len(temp_time_stamp_list)
    time_spent_list_for_each_device_id=[]
    for i in range(r-1):
        tmin=temp_time_stamp_list[i]
        tmax=temp_time_stamp_list[i+1]
        tdelta_for_each_device_id = datetime.strptime(tmax,'%Y-%m-%d %H:%M:%S') - datetime.strptime(tmin,'%Y-%m-%d %H:%M:%S')
        if tdelta_for_each_device_id<timedelta(minutes = 10) and tdelta_for_each_device_id>=timedelta(minutes = 0):
            time_spent_list_for_each_device_id.append(tdelta_for_each_device_id)
        elif tdelta_for_each_device_id>=timedelta(minutes = 10):
            time_spent_list_for_each_device_id.append(timedelta(minutes = 10))
    
    temp_total=sum(time_spent_list_for_each_device_id,timedelta())
    """for i in range(len(time_spent_list_for_each_device_id)):
        temp_total=temp_total+time_spent_list_for_each_device_id[i]"""
    
    total_1=temp_total/(len(time_spent_list_for_each_device_id)+1)
    sum_of_hours_list.append(total_1)       
         
                
print(len(sum_of_hours_list))           
print(type(sum_of_hours_list[0]))        


# In[6]:


""" Convert all tdelta into hours, which are stings with length = 26,874"""
time_spent_list_hours=[]
for item in time_spent_list:
    item = '%02d:%02d:%02d.%06d' % (item.days*24 + item.seconds // 3600, (item.seconds % 3600) // 60, item.seconds % 60, item.microseconds)
    time_spent_list_hours.append(item)


# In[7]:


"""Compute the average time spent in eash lesson """

total_time_spent=[timedelta(minutes = 0)]
total_time_spent=sum(sum_of_hours_list,timedelta())
total_1=total_time_spent/(len(sum_of_hours_list)+1)

print("The average time spent in every lesson is : ",total_1)


# In[8]:


print(len(list_device_id))
print(len(sum_of_hours_list)) 


# In[13]:


import numpy as np
import datetime
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib.font_manager import FontProperties


# In[59]:


time_list1=sum_of_hours_list[0:30]
devids=list_device_id[0:30]

# specify a date to use for the times
zero = datetime.datetime(2021,1,1)
time = [zero + t for t in time_list1]

# convert datetimes to numbers
zero = mdates.date2num(zero)
time = [t-zero for t in mdates.date2num(time)]

f = plt.figure()
ax = f.add_subplot(1,1,1)

ax.bar(devids, time, bottom=zero)
ax.yaxis_date()
ax.yaxis.set_major_formatter(mdates.DateFormatter("%H:%M:%S"))

# add 10% margin on top (since ax.margins seems to not work here)
ylim = ax.get_ylim()
ax.set_ylim(None, ylim[1]+0.1*np.diff(ylim))

fontP = FontProperties()
fontP.set_size("large")
p1, = plt.plot([1, 2, 3],'r-', label='Mean')
plt.legend(handles=[p1], title='', bbox_to_anchor=(1.05, 1), loc='upper left', prop=fontP)

"""plt.axhline(y=timedelta(hours=2))"""
plt.title('Scatter plot device ids vs sum of hours spent')
plt.xlabel('Device id"s')
plt.ylabel('Time spent')


plt.show()


# In[60]:


time_list1=sum_of_hours_list[1050:1080]
devids=list_device_id[1050:1080]

# specify a date to use for the times
zero = datetime.datetime(2021,1,1)
time = [zero + t for t in time_list1]

# convert datetimes to numbers
zero = mdates.date2num(zero)
time = [t-zero for t in mdates.date2num(time)]

f = plt.figure()
ax = f.add_subplot(1,1,1)

ax.bar(devids, time, bottom=zero)
ax.yaxis_date()
ax.yaxis.set_major_formatter(mdates.DateFormatter("%H:%M:%S"))

# add 10% margin on top (since ax.margins seems to not work here)
ylim = ax.get_ylim()
ax.set_ylim(None, ylim[1]+0.1*np.diff(ylim))

fontP = FontProperties()
fontP.set_size("large")
p1, = plt.plot([1, 2, 3],'r-', label='Mean')
plt.legend(handles=[p1], title='', bbox_to_anchor=(1.05, 1), loc='upper left', prop=fontP)

"""plt.axhline(y=timedelta(hours=2))"""
plt.title('Scatter plot device ids vs sum of hours spent')
plt.xlabel('Device id"s')
plt.ylabel('Time spent')


plt.show()


# In[62]:


time_list1=sum_of_hours_list[2025:2055]
devids=list_device_id[2025:2055]

# specify a date to use for the times
zero = datetime.datetime(2021,1,1)
time = [zero + t for t in time_list1]

# convert datetimes to numbers
zero = mdates.date2num(zero)
time = [t-zero for t in mdates.date2num(time)]

f = plt.figure()
ax = f.add_subplot(1,1,1)

ax.bar(devids, time, bottom=zero)
ax.yaxis_date()
ax.yaxis.set_major_formatter(mdates.DateFormatter("%H:%M:%S"))

# add 10% margin on top (since ax.margins seems to not work here)
ylim = ax.get_ylim()
ax.set_ylim(None, ylim[1]+0.1*np.diff(ylim))

fontP = FontProperties()
fontP.set_size("large")
p1, = plt.plot([1, 2, 3],'r-', label='Mean')
plt.legend(handles=[p1], title='', bbox_to_anchor=(1.05, 1), loc='upper left', prop=fontP)

"""plt.axhline(y=timedelta(hours=2))"""
plt.title('Scatter plot device ids vs sum of hours spent')
plt.xlabel('Device id"s')
plt.ylabel('Time spent')


plt.show()


# In[63]:


for i in range(8):
    time_list1=sum_of_hours_list[1000*i:1000*i+1000]
    devids=list_device_id[1000*i:1000*i+1000]

    # specify a date to use for the times
    zero = datetime.datetime(2021,1,1)
    time = [zero + t for t in time_list1]

    # convert datetimes to numbers
    zero = mdates.date2num(zero)
    time = [t-zero for t in mdates.date2num(time)]

    f = plt.figure()
    ax = f.add_subplot(1,1,1)

    ax.bar(devids, time, bottom=zero)
    ax.yaxis_date()
    ax.yaxis.set_major_formatter(mdates.DateFormatter("%H:%M:%S"))

    # add 10% margin on top (since ax.margins seems to not work here)
    ylim = ax.get_ylim()
    ax.set_ylim(None, ylim[1]+0.1*np.diff(ylim))

    fontP = FontProperties()
    fontP.set_size("large")
    p1, = plt.plot([1, 2, 3],'r-', label='Mean')
    plt.legend(handles=[p1], title='', bbox_to_anchor=(1.05, 1), loc='upper left', prop=fontP)

    """plt.axhline(y=timedelta(hours=2))"""
    plt.title('Scatter plot device ids vs sum of hours spent')
    plt.xlabel('Device id"s')
    plt.ylabel('Time spent')


    plt.show()

    


# In[ ]:




