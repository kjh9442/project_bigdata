#!/usr/bin/env python
# coding: utf-8

# In[1]:


import warnings
warnings.filterwarnings('ignore')
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import folium


# In[2]:


bus = pd.read_csv('./data/경기도_광주시_버스정류장_08_25_2021.csv', encoding='euc-kr', engine='python')
bus.shape


# In[3]:


bus.head()


# In[4]:


# 중복된 버스정류장 확인
bus.duplicated(['도로구간번호'])


# In[5]:


# 중복된 버스정류장 개수 확인
bus.duplicated(['도로구간번호']).sum()


# In[6]:


# 중복으로 들어가있는 버스정류장 제거
bus = bus.drop_duplicates('도로구간번호')


# In[7]:


# 필요한 column만 사용하기
bus_columns = ['도로구간번호','정류장명', '정류장종류','위도', '경도']
df_bus =  bus[bus_columns]
df_bus


# In[8]:


df_bus.dtypes


# In[9]:


# 연산에 사용할 데이터가 아니기 때문에 object(문자열)형태로 변경한다.
df_bus['도로구간번호'] = df_bus['도로구간번호'].astype(str)


# In[10]:


df_bus.dtypes


# In[11]:


# 불필요한 인덱스 제거
df_bus.reset_index(drop=True)


# In[12]:


# folium을 이용한 지도 시각화
map_bus = folium.Map(location=[df_bus['위도'].mean(), df_bus['경도'].mean()], zoom_start=12)
for i in df_bus.index:
    bus_name = df_bus.loc[i, '정류장명']
    popup = folium.Popup(bus_name, max_width=200)
    folium.Marker(location=[df_bus.loc[i, '위도'], df_bus.loc[i, '경도']], popup=popup).add_to(map_bus)
map_bus.save('./output/bus_map.html')
map_bus


# In[13]:


# seaborn을 이용한 시각화
plt.figure(figsize=[16, 12])
sns.scatterplot(data=df_bus, x='경도', y='위도', hue='정류장종류', s=30)


# In[ ]:




