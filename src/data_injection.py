import  numpy as np
import pandas as pd

from sklearn.model_selection import train_test_split

import os

df=pd.read_csv(r"C:\Users\redhu\OneDrive\Desktop\diabetes.csv")

train_data,test_data=train_test_split(df,test_size=0.20,random_state=42)

data_path=os.path.join('data','raw')
os.makedirs(data_path,exist_ok=True)

train_data.to_csv(os.path.join(data_path,'train_data.csv'))
test_data.to_csv(os.path.join(data_path,'test_data.csv'))
