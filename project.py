#!/usr/bin/env python
# coding: utf-8

# In[1]:


import warnings
warnings.filterwarnings('ignore')
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import folium
plt.rcParams['font.family'] = 'NanumGothicCoding'
plt.rcParams['font.size'] = 12


# In[2]:


bus = pd.read_csv('./data/경기도_광주시_버스정류장_08_25_2021.csv', encoding='euc-kr', engine='python')
bus.shape


# In[3]:


bus.head()


# In[4]:


bus.columns


# In[5]:


df_bus = bus[['도로구간번호', '법정구역', '정류장명', '정류장종류', '위도', '경도', '비고']]
df_bus


# In[6]:


df_bus.dtypes


# In[7]:


# 연산에 사용할 데이터가 아니기 때문에 object(문자열)형태로 변경한다.
df_bus['도로구간번호'] = df_bus['도로구간번호'].astype(str)


# In[8]:


df_bus.dtypes


# In[9]:


# folium을 이용한 지도 시각화
map_bus = folium.Map(location=[df_bus['위도'].mean(), df_bus['경도'].mean()], zoom_start=12)
for i in df_bus.index:
    # 택시 정류장인 경우 아이콘의 색상을 'red'로 한다.
    if df_bus['정류장명'][i] == 'TAXI정류장':
        bus_name = df_bus.loc[i, '정류장명']
        popup = folium.Popup(bus_name, max_width=200)
        folium.Marker(location=[df_bus.loc[i, '위도'], df_bus.loc[i, '경도']], popup=popup, icon=folium.Icon(color='red')).add_to(map_bus)
    # 현장에는 정류장이 없으나 BIS시스템 상에 존재하는 정류장은 아이콘의 색상을 'green'으로 한다.
    elif df_bus['비고'][i] == '현장에는 정류장이 없으나 BIS시스템 상에 존재하는 정류장':
        bus_name = df_bus.loc[i, '정류장명']
        popup = folium.Popup(bus_name, max_width=200)
        folium.Marker(location=[df_bus.loc[i, '위도'], df_bus.loc[i, '경도']], popup=popup, icon=folium.Icon(color='green')).add_to(map_bus)
    else:
        bus_name = df_bus.loc[i, '정류장명']
        popup = folium.Popup(bus_name, max_width=200)
        folium.Marker(location=[df_bus.loc[i, '위도'], df_bus.loc[i, '경도']], popup=popup).add_to(map_bus)

map_bus.save('./output/bus_map.html')
map_bus


# In[10]:


# seaborn을 이용한 시각화
# 법정구역별로 정류장색을 나눴다
plt.figure(figsize=[16, 12])
sns.scatterplot(data=df_bus, x='경도', y='위도', hue='법정구역', s=50)
plt.savefig('./output/project.png')


# In[ ]:





# In[ ]:





# In[ ]:




