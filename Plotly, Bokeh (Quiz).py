#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go


# 1.นาย A,B,C,D,E มีรายได้ 10,000 20,000 30,000 40,000 60,000 ต่อเดือนในปี 2020 ตามลำดับ ทุกๆปีเงินเดือนจะเพิ่ม 7% จงสร้าง DataFrame เก็บเงินเดือนของทั้ง 5 นาย ในปี 2016,2017,2018,2019,2020 

# In[49]:


salary_2020 = np.array([10000,20000,30000,40000,60000])
salary_2019 = np.round(salary_2020*0.93,2)
salary_2018 = np.round(salary_2019*0.93,2)
salary_2017 = np.round(salary_2018*0.93,2)
salary_2016 = np.round(salary_2017*0.93,2)


# In[50]:


all_salary = [salary_2020.tolist(),salary_2019.tolist(),salary_2018.tolist(),salary_2017.tolist(),
              salary_2016.tolist()]
all_salary


# In[51]:


df0 = pd.DataFrame(all_salary, index = [2020,2019,2018,2017,2016], columns = ['A','B','C','D','E'])
dft = df0.T
dft


# 2.ใช้ข้อมูลจากข้อ 1 สร้าง Bar Plot ให้แกน X เป็นชื่อ และแกน Y เป็นเงินของปี 2017 คูณ 2 และสลับแกน (สองกราฟ) และปรับให้แกน X เอียง -45 องศา

# In[52]:


fig = px.bar(dft, x = dft.index , y = 2017)
fig.update_layout(xaxis_tickangle = -45)
fig.show()


# In[6]:


fig = px.bar(dft, x = 2017 , y = dft.index)
fig.update_layout(xaxis_tickangle = -45)
fig.show()


# 3.จากข้อ 2 ให้ตั้งชื่อกราฟให้เหมาะสม เป็นชื่อแกน X Y ให้เหมาะสมและให้ไล่สีจากเงินเดือนปี 2016 รวมถึงเมื่อนำเม้าส์ไปวาง จะแสดงเงินเดือนเงินเดือนของแต่ละปี และเงินเดือนเฉลี่ย (จะเพิ่ม column ใน DataFrame หรือจะคำนวณแยกก็ได้) 

# In[7]:


dft['avg'] = dft.mean(axis = 1).round(2)
dft['avg']


# In[8]:


dft


# In[9]:


fig = px.bar(dft, x = dft.index , y = 2017, title = 'Salaries in year 2017',
            hover_data = [2020,2019,2018,2016,'avg'],
            color = 2016)
fig.update_layout(xaxis_tickangle = -45)
fig.show()


# ให้ Import ไฟล์ Titanic จากบทเรียน Pandas เข้าสู่ Jupyter Notebook

# In[10]:


df = pd.read_csv('../Desktop/DataCamp/train.csv')
df.head()


# 4.สร้าง Line Graph โดยให้แกน Y เป็นราคาเฉลี่ยของค่าโดยสารของแต่ละอายุ และแกน X เป็นอายุ พร้อมทั้งแก้ชื่อแกน ตั้งชื่อกราฟให้เหมาะสม

# In[11]:


df1 = df.groupby('Age').mean()
df1.head()


# In[12]:


fig = px.line(df1, y ='Fare', x = df1.index, title = 'Average fare per age', labels = {'x':'Age'})
fig


# 5.สร้าง Line Graph โดยให้แกน Y เป็นราคาเฉลี่ยของค่าโดยสารของแต่ละชั้นโดยสาร และแกน X เป็นชั้นโดยสาร พร้อมทั้งแก้ชื่อแกน ตั้งชื่อกราฟให้เหมาะสม

# In[13]:


df2 = df.groupby('Pclass').mean()
df2


# In[14]:


fig = px.line(df2, y ='Fare', x = df2.index, title = 'Average fare per class', labels = {'x':'class'})
fig


# 6.สร้าง Pie Chart หา Sum ของราคาค่าโดยสารแต่ละอายุ

# In[15]:


fig = px.pie(df, values = 'Fare', names = 'Age', title = 'Pie Chart')
fig


# 7.สร้าง Pie Chart หา Mean ของราคาค่าโดยสารแต่ละอายุ

# In[16]:


df3 = df.groupby('Age').mean()
df3.head()


# In[17]:


fig = px.pie(df3, values = 'Fare', names = df3.index , title = 'Pie Chart')
fig


# 8.สร้าง Pie Chart หา Mean ของราคาของคนที่มีมีนามสกุลซ้ำกัน (จากแบบฝึกหัด Pandas)

# In[18]:


df[['Last','First']] = df.Name.str.split(",",expand=True)


# In[64]:


df.head()


# In[77]:


duplicate = df[df['Last'].duplicated(keep = False)].sort_values('Last') 
duplicate.head()


# In[79]:


groupby_duplicate = duplicate.groupby('Last',as_index = False).mean()
groupby_duplicate


# In[81]:


fig = px.pie(groupby_duplicate, values = 'Fare', names = 'Last')
fig.show()


# 9. สร้าง Pie Chart หา Mean ของอายุของคนที่มีมีนามสกุลซ้ำกัน (จากแบบฝึกหัด Pandas) พร้อมทั้งตั้งชื่อและเปลี่ยนสี

# In[84]:


fig = px.pie(groupby_duplicate, values = 'Age', names = 'Last')
fig.show()


# 10. สร้าง Pie Chart หา Mean ของแต่ละจุดหมายปลายทาง (Embarked) พร้อมทั้งตั้งชื่อและเปลี่ยนสี

# In[24]:


df4 = df.groupby('Embarked').mean()
df4


# In[25]:


fig = px.pie(df4, values = 'Fare', names = df4.index, title = 'Pie Chart Avg Fare Per Embark', 
             color_discrete_sequence = px.colors.sequential.RdBu)
fig


# 11. สร้าง Bubble Chart ให้แกน X เป็นช่วงอายุ แกน Y เป็นราคาเฉลี่ย ขนาดตามจำนวนเฉลี่ยของพี่น้องและคู่สมรส (เช็คคอลัมน์) ในช่วงอายุนั้น พร้อมทั้งตั้งชื่อแกน X Y และชื่อกราฟ และไล่สีตามค่าเฉลี่ยของ Pclass

# In[26]:


df5 = df.groupby('Age').mean()
df5.head()


# In[27]:


fig = px.pie(df5, values = 'SibSp', names = df5.index, title = 'Pie Chart Avg Siblings and Spouse Per Age', 
             color_discrete_sequence = px.colors.sequential.Purp)
fig


# 12.สร้าง Box Plot ให้แกน X เป็นเพศ และ แกน Y เป็นราคา

# In[28]:


fig = px.box(df, x = 'Sex', y = 'Fare')
fig


# 13.สร้าง Box Plot ให้แกน X เป็นPclass และ แกน Y เป็นราคา

# In[29]:


fig = px.box(df, x = 'Pclass', y = 'Fare')
fig


# 14. สร้าง Box Plot ให้แกน X เป็นPclass และ แกน Y เป็นอายุ ให้ Points = all

# In[30]:


fig = px.box(df, x = 'Pclass', y = 'Age', points = 'all')
fig


# 15. สร้าง Box Plot ให้แกน X เป็น Survived แกน Y เป็นอายุ และสีเป็นเพศ 

# In[31]:


fig = px.box(df, x = 'Survived', y = 'Age', color = 'Sex')
fig


# 16. สร้าง barplot โดยให้ แกน X เป็นจุดหมายปลายทางและแกน Y เป็น std ของราคา

# In[32]:


df5 = df.groupby('Embarked').std()
df5.head()


# In[33]:


fig = px.bar(df5, x = df5.index, y = 'Fare')
fig


# 17. สร้าง barplot โดยให้ แกน X เป็นชั้นที่นั่ง และแกน Y เป็น Mean ของอายุ

# In[34]:


df6 = df.groupby('Pclass').mean()
df6.head()


# In[35]:


fig = px.bar(df6, x = df6.index, y = 'Age')
fig


# 18. สร้าง HeatMap โดย pivot table กำหนดให้ index เป็น Pclass และ column เป็นเพศ และ values เป็น ราคาเฉลี่ย

# In[36]:


df7 = df.pivot_table(index = 'Pclass', columns = 'Sex', values = 'Fare',aggfunc = np.mean)
df7


# In[37]:


fig = go.Figure(data = go.Heatmap(z=df7, x = df7.index, y=df7.columns, colorscale = 'Picnic'))
fig.show()


# 19. สร้าง Heatmap โดย Correlation ของทั้ง DataFrame และเปลี่ยนสี

# In[38]:


df_corr = df.corr()
df_corr


# In[39]:


fig = go.Figure(data = go.Heatmap(z=df_corr, x = df_corr.index, y = df_corr.columns, colorscale = 'Picnic'))
fig.show()


# 20. ใช้ไฟล์ 2011_us_ag_exports.csv สร้าง Choropleth ของอเมริกาโดยไล่สีตาม Cotton และเมื่อนำเม้าส์ไปวาง จะเห็นรายละเอียด total exports, total fruits, total veggies 

# In[40]:


df8 = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/2011_us_ag_exports.csv")
df8.head()


# In[41]:


for col in df8.columns:
    df8[col] = df8[col].astype(str)
    
df8['text'] = df8['state'] + '<br>' +             'total exports'+ df8['total exports']+ '<br>' +            'total fruits'+ df8['total fruits']+ '<br>' +            'total veggies'+ df8['total veggies']

df8.head()


# In[42]:


fig = go.Figure(data=go.Choropleth(
    locations =df8['code'], # Spatial coordinates
    z = df8['cotton'], # Data to be color-coded
    locationmode = 'USA-states', # set of locations match entries in `locations`
    colorscale = 'Reds',
    text = df8['text'],
    colorbar_title = "Millions USD",
))

fig.update_layout(
    title_text = '2011 US Agriculture Exports by State',
    geo_scope='usa', # limite map scope to USA
)

fig.show()


# 21. ใช้ไฟล์ 2011_us_ag_exports.csv สร้าง Choropleth ของอเมริกาโดยไล่สีตาม Total veggies และเมื่อนำเม้าส์ไปวาง จะเห็นรายละเอียด อัตราส่วน beef ต่อ pork เป็นเลขทศนิยม 2 ตำแหน่ง

# In[43]:


df8['beef'] = pd.to_numeric(df8['beef'])
df8['pork'] = pd.to_numeric(df8['pork'])


# In[44]:


df8['beef_pork_ratio'] = (df8['beef']/df8['pork']).round(2)
df8['beef_pork_ratio'].head()


# In[45]:


for col in df8.columns:
    df8[col] = df8[col].astype(str)
    
df8['text2'] = df8['state'] + '<br>' +             'beef pork ratio'+ df8['beef_pork_ratio']
df8.head()


# In[46]:


fig = go.Figure(data=go.Choropleth(
    locations =df8['code'], # Spatial coordinates
    z = df8['total veggies'], # Data to be color-coded
    locationmode = 'USA-states', # set of locations match entries in `locations`
    colorscale = 'Reds',
    text = df8['text2'],
    colorbar_title = "Millions USD",
))

fig.update_layout(
    title_text = '2011 US Agriculture Exports by State',
    geo_scope='usa', # limite map scope to USA
)

fig.show()


# 22. สุ่ม 10 States จากไฟล์ข้างต้น นำมาสร้าง Bar plot โดยแกน Y เป็น Total Exports และไล่สีตามอัตราส่วน cotton ต่อ Wheat พร้อมทั้งเปลี่ยนชื่อแกน และตั้งชื่อกราฟ (ถ้าอัตราส่วนหาค่าไม่ได้ให้ใช้ 0) 

# In[93]:


df9 = df8.sample(10)
df9.head()


# In[96]:


df9['cotton'] = pd.to_numeric(df9['cotton'])
df9['wheat'] = pd.to_numeric(df9['wheat'])


# In[99]:


df9['cotton_wheat_ratio'] = df9['cotton']/df9['wheat']
cotto_wheat = df9['cotton_wheat_ratio']
cotto_wheat[np.isnan(cotto_wheat)] = 0
cotto_wheat


# In[102]:


df9.head()


# In[114]:


fig = px.bar(df9, y ='total exports',x ='state',color = 'cotton_wheat_ratio', title = 'Total exports in 10 states',
            labels = {'total_exports':'total exports','state':'States'})
fig

