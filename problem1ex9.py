# 
import pandas as pd
d1={'Student':['Ice Bear','Panda','Grizzly'],'Math':[80,95,79]}
d2={'Student':['Ice Bear','Panda','Grizzly'],'Electronics':[85,81,83]}
d3={'Student':['Ice Bear','Panda','Grizzly'],'GEAS':[90,79,93]}
d4={'Student':['Ice Bear','Panda','Grizzly'],'ESAT':[93,89,88]}

df1=pd.DataFrame(d1,columns=['Student','Math'])
df2=pd.DataFrame(d2,columns=['Student','Electronics'])
df3=pd.DataFrame(d3,columns=['Student','GEAS'])
df4=pd.DataFrame(d4,columns=['Student','ESAT'])

r1=pd.merge(df1,df2,on='Student')
r2=pd.merge(df3,df4,on='Student')
rt=pd.merge(r1,r2,on='Student')

x=pd.melt(rt,id_vars=['Student'],value_vars=['Math','Electronics','GEAS','ESAT'])
x_tidy=x.rename(columns={'variable':'Subject','value':'Grades'})
y=x_tidy.sort_values('Student').reset_index().drop(columns=['index'])