

#Importing Data
import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.stattools import adfuller

#Importing data

data = pd.DataFrame(pd.read_csv('C:/Users/megersa/Desktop/Python_project/data_ts.csv', index_col=0,parse_dates=True)) # importing data

#Descriptive


data.describe() # summary of descritive statistics

#Plots
plt.plot(data.cpi,  color='r', label='cpi')
plt.plot(data.ipi,  color='b', label='ipi')
plt.plot(data.asset/10e10,  color='y', label='asset')
plt.plot(data.fedfund*10,  color='b', label='fedfund')
plt.legend()
plt.xlabel("Date")
plt.ylabel("Values")
plt.title("Plots of varaibles")
# To load the display window
plt.show()

data['cpi'].plot()
data['ipi'].plot()
plt.title("Plots of varaibles")
plt.legend()

figure, axis = plt.subplots(2, 2)
  
axis[0, 0].plot(data.ipi)
axis[0, 0].set_title("IPI")
  
axis[0, 1].plot(data.cpi)
axis[0, 1].set_title("cpi")
  
axis[1, 0].plot(data.fedfund)
axis[1, 0].set_title("Tangent Function")
  
axis[1, 1].plot(data.asset)
axis[1, 1].set_title("asset")
  
# Combine all the operations and display
plt.show()

fig, ax =plt.subplots(4)
fig.suptitle('two plots stacked veritcaly')
ax[0].plot(data.ipi)
ax[1].plot(data.cpi)
ax[2].plot(data.fedfund)
ax[3].plot(data.asset)
plt.show()

fig, ax =plt.subplots(4)
fig.suptitle('two plots stacked veritcaly')
ax[0].plot(data.ipi)
ax[1].plot(data.cpi)
ax[2].plot(data.fedfund)
ax[3].plot(data.asset)
plt.show()

fig, ax =plt.subplots(4)
fig.suptitle('two plots stacked veritcaly')
ax[0].plot(data.ipi)
ax[1].plot(data.cpi)
ax[2].plot(data.fedfund)
ax[3].plot(data.asset)
plt.show()


# ADF Test
result = adfuller(data.ipi.values, autolag='AIC')
print(f'ADF Statistic: {result[0]}')
print(f'p-value: {result[1]}')
for key, value in result[4].items():
    print('Critial Values:')
    print(f'   {key}, {value}')
	
	# Simple Linear Regression
df=pd.DataFrame(data)
import statsmodels.api as sm

x = df.ipi
y = df.fedfund

m1 = sm.OLS(y, x).fit()
m1_hat = m1.predict(x) 
 
print_m1 = m1.summary()
print(print_m1)

#Multiple Linear Regression
import statsmodels.api as sm
df=pd.DataFrame(data)

x = df[['ipi', 'cpi', 'asset']]
y = df['fedfund']

m1 = sm.OLS(y, x).fit()
m1_hat = m1.predict(x) 
 
print_m1 = m1.summary()
print(print_m1)
data.dtypes
