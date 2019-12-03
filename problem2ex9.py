import pandas as pd
data={'Box':['Box1','Box1','Box1','Box2','Box2','Box2'],'Dimension':['Length','Width','Height','Length','Width','Height'],'Grades':[6,4,2,5,3,4]}
messy=pd.DataFrame(data,columns=['Box','Dimension','Grades'])
tidy=messy.pivot_table(index=['Box'],columns='Dimension',values='Grades').reset_index()
v1=tidy.iloc[0,1]*tidy.iloc[0,2]*tidy.iloc[0,3]
v2=tidy.iloc[1,1]*tidy.iloc[1,2]*tidy.iloc[1,3]
tidy.insert(4,'Volume',[v1,v2])