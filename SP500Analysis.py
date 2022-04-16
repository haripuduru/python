#!/usr/bin/env python
# coding: utf-8

# In[7]:


#importing required  python libraries

import pandas as pd
import numpy as np
from datetime import datetime as dt
import yfinance as yf
import matplotlib.pyplot as plt

#reading CPI index data using python data frame
cpi_df = pd.read_excel("CPI_INDEX.xlsx")

#using yfinance, importing  S&P 500 data
#Monthly interval Data 

plt.style.use('seaborn')
gspc = yf.Ticker('^GSPC')
gspc_df = gspc.history(interval ='1mo',start = '1991-01-01',end = '2021-12-31')

#Exporting S&p 500 close price
gspc_df["Close"].to_excel("closeprice.xlsx",index=False)


#Plotting both S&P 500 and CPI data on the same plot using dual axis plot

fig,ax1=plt.subplots()
ax2=ax1.twinx()
color1= 'green'
color2= 'red'
ax1.set_ylabel('S&P 500_Close_Price',color ='r')
ax2.set_ylabel('CPI_Monthly_Data',color ='g')
ax1.spines['left'].set_color(color2)
ax1.spines['left'].set_color(color1)
ax2.plot(cpi_df['Date'],cpi_df['CPI'],color ='g')
ax1.plot(cpi_df['Date'],gspc_df['Close'],color='r')
plt.grid()
plt.show()

# Plotting CPI Perecent Change

fig, ax = plt.subplots(figsize=(16, 8))
cpi_df['CPI_pct_change'] = cpi_df['CPI'].pct_change().copy()
plt.plot(cpi_df['Date'], cpi_df['CPI_pct_change'], c='green')

plt.grid()
plt.axhline(0)
plt.show()

#Plotting S&P500 perecent change

fig, ax3 = plt.subplots(figsize=(16,8))
gspc_df['gspc_pct_change']= gspc_df['Close'].pct_change().copy()
plt.plot(cpi_df['Date'],gspc_df['gspc_pct_change'],c='red')
plt.grid()
plt.axhline(0)
plt.show()

#Correlation between CPI and S&P closing price
print("The Correlation Matrix of CPI and S&P 500 is")
corr_df = pd.read_excel("Corr_Price_CPI.xlsx")
print(corr_df.corr(method='pearson'))




# In[ ]:




