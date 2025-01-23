# -*- coding: utf-8 -*-
"""
Created on Wed Dec 20 15:01:26 2023

@author: sezzz
"""

import json
import pandas as pd
from urllib.request import urlopen
# file1 = open('c:\Jupyter\ML_Capstone\development\Texas_Zip_Codes.csv', 'r')
# Lines = file1.readlines()

count = 0
df=None
# Strips the newline character
alldata=[]
# hard code for my zip code==============================
Lines=['75093']
# end comment============================================
for line in Lines:
  if True or len(alldata)<1000:
    count += 1
    zip=line.strip()
    print("Line{}: {}".format(count, line.strip()))
    print(len(alldata))
    url = 'http://api.powertochoose.org/api/PowerToChoose/plans?zip_code='+zip
    with urlopen(url) as response:
      body = response.read()
 # print(body)

      json_data = json.loads(body)
  # print(json_data)
      mystr = json.dumps(json_data['data'])
      mydata = json.loads(mystr)
      for record in mydata:
        alldata.append(record)
# print(alldata)
# df=pd.read_json(alldata,orient='records')
df=pd.DataFrame(alldata)
print(df.columns)
print(df)
# for plan in mydata:
  # print(plan)
  # print("=========================================================================================================")
# saving the dataframe
df.to_csv('c:\Jupyter\ML_Capstone\development\\file1.csv',index=False)
            
   