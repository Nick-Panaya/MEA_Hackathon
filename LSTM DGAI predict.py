#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
#import seaborn as sn
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import pickle
import xlrd
import sklearn
from sklearn.model_selection import train_test_split
from sklearn.model_selection import RandomizedSearchCV
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import mean_squared_error

import xlsxwriter
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
dataset = pd.ExcelFile(r'C:\Users\LENOVO\PycharmProjects\PT data_2018_2019_C+S_time.xlsx')
dataset.sheet_names

data = dataset.parse('2018 DGA')
H19 = dataset.parse('2019 DGA')
print (data)
print(type(data))
data.shape


# In[2]:



data = data.replace(to_replace = 'Condition 1',value = 1)
data = data.replace(to_replace = 'Condition 2',value = 2)
data = data.replace(to_replace = 'Condition 3',value = 3)
data = data.replace(to_replace = 'Condition 4',value = 4)
data = data.replace(to_replace = 'Condition 5',value = 5)
data = data.replace(to_replace = 'Condition 6',value = 6)
data = data.replace(to_replace = 'Condition 7',value = 7)
data = data.replace(to_replace = 'Condition 8',value = 8)
data = data.replace(to_replace = 'Condition 9',value = 9)


# In[3]:


data = data.replace(to_replace = 'ไม่ปกติ',value=0)
data = data.replace(to_replace = 'ปกติ',value=1)
data = data.replace(to_replace = 'ไม่มี',value=1)# General การรั่วซึม
data = data.replace(to_replace = 'ซึม',value=1) # General การรั่วซึม
data = data.replace(to_replace = 'ไม่มีการรั่วซึม',value=1)# General การรั่วซึม CR
data = data.replace(to_replace = 'ขดลวด',value=0)   # General การรั่วซึม CR
data = data.replace(to_replace = '0 : ไม่รั่วซึม',value=1)# General การรั่วซึม CS
data = data.replace(to_replace = '1 : ไม่รั่วซึม',value=1)# General การรั่วซึม CS
data = data.replace(to_replace = '1 : ซึม',value=0)   # General การรั่วซึม CS
data = data.replace(to_replace = 'ไม่สะอาด',value=0)
data = data.replace(to_replace = 'สะอาด',value=1)
data = data.replace(to_replace = 'ไม่เปลี่ยน',value=0)# General Silica gel
data = data.replace(to_replace = 'เปลี่ยน',value=1) # General Silica gel
data = data.replace(to_replace = 'ไม่ใส',value=0)# OLTC สภาพน้ำมัน
data = data.replace(to_replace = 'ใส',value=1) # OLTC สภาพน้ำมัน
data = data.replace(to_replace = 'ไม่เปิด',value=0)# General สถานะวาล์ว ครีบระบายความร้อย
data = data.replace(to_replace = 'ปิด',value=0) # General สถานะวาล์ว ครีบระบายความร้อย
data = data.replace(to_replace = 'เปิด',value=1) # General สถานะวาล์ว ครีบระบายความร้อย
data = data.replace(to_replace = 'ไม่ทำ',value=0)# ทำความสะอาด OLTC Driver
data = data.replace(to_replace = 'ทำ',value=1) # ทำความสะอาด OLTC Driver
data = data.replace(to_replace = 'Normal',value=5) # DGA
data = data.replace(to_replace = 'T1',value=3) # DGA
data = data.replace(to_replace = 'PD',value=3) # DGA
data = data.replace(to_replace = 'T2',value=1) # DGA
data = data.replace(to_replace = 'T3',value=1) # DGA
data = data.replace(to_replace = 'D1',value=1) # DGA
data = data.replace(to_replace = 'D2',value=1) # DGA
data = data.replace(to_replace = 'DT',value=1) # DGA
data = data.replace(to_replace = 'nd',value= 0) # DGA
data = data.replace(to_replace = ' ',value = 0)
data = data.replace(to_replace = '-',value = 0)
data = data.replace(to_replace = 'เปิด test tap ไม่ได้',value = 0)
data = data.replace(to_replace = 'ปลดสายไม่ได้',value = 0)
data = data.replace(to_replace = 'เปิด tap ไม่ได้',value = 0)
data = data.replace(to_replace = 'Dyn1',value = 1)
data = data.replace(to_replace = 'test tap ไม่ได้',value = 0)
data = data.replace(to_replace = 'N/A',value = 0)
data = data.replace(to_replace = 'NaN',value = 0)
data = data.replace(to_replace = '0',value = 0)
data = data.replace(to_replace = 'test ไม่ได้',value = 0) #Gen
data = data.replace(to_replace = '#VALUE!',value = 0) #Gen
data = data.replace(to_replace = '#DIV/0!',value = 0) #Gen
data = data.replace(to_replace = 'test ไม่ได้ (Bushing)',value = 0) #Gen
data = data.replace(to_replace = 'Condition 1',value = 1)
data = data.replace(to_replace = 'Condition 2',value = 2)
data = data.replace(to_replace = 'Condition 3',value = 3)
data = data.replace(to_replace = 'Condition 4',value = 4)
data = data.replace(to_replace = 'Condition 5',value = 5)
data = data.replace(to_replace = 'Condition 6',value = 6)
data = data.replace(to_replace = 'Condition 7',value = 7)
data = data.replace(to_replace = 'Condition 8',value = 8)
data = data.replace(to_replace = 'Condition 9',value = 9)
data = data.replace(to_replace = 'YNyn0+d1',value = 1)
data = data.replace(to_replace = 'Good',value = 3)
data = data.replace(to_replace = 'normal',value = 2)
data = data.replace(to_replace = 'Bad',value = 1)
data = data.dropna()


# In[4]:


data = data.drop(['A', 'B', 'C', 'D', 'E', ], axis=1)
data = data.drop(['7_DGA'], axis=1)
#data = data.drop(['1_General', '2_Active Part', '3_insulation Oil', '4_Bushing', '5_Surge arrester','6_OLTC','7_DGA'], axis=1)
#data = data.drop(['General_Final Score','Active_Final Score','Oil_Final Score','Bushing_Final_Score','ARS_Final Score','OLTC_Final Score','DGA_Final Score'], axis=1)


# In[5]:



H19 = H19.replace(to_replace = 'Condition 1',value = 1)
H19 = H19.replace(to_replace = 'Condition 2',value = 2)
H19 = H19.replace(to_replace = 'Condition 3',value = 3)
H19 = H19.replace(to_replace = 'Condition 4',value = 4)
H19 = H19.replace(to_replace = 'Condition 5',value = 5)
H19 = H19.replace(to_replace = 'Condition 6',value = 6)
H19 = H19.replace(to_replace = 'Condition 7',value = 7)
H19 = H19.replace(to_replace = 'Condition 8',value = 8)
H19 = H19.replace(to_replace = 'Condition 9',value = 9)


# In[6]:


H19 = H19.replace(to_replace = 'ไม่ปกติ',value=0)
H19 = H19.replace(to_replace = 'ปกติ',value=1)
H19 = H19.replace(to_replace = 'ไม่มี',value=1)# General การรั่วซึม
H19 = H19.replace(to_replace = 'ซึม',value=1) # General การรั่วซึม
H19 = H19.replace(to_replace = 'ไม่มีการรั่วซึม',value=1)# General การรั่วซึม CR
H19 = H19.replace(to_replace = 'ขดลวด',value=0)   # General การรั่วซึม CR
H19 = H19.replace(to_replace = '0 : ไม่รั่วซึม',value=1)# General การรั่วซึม CS
H19 = H19.replace(to_replace = '1 : ไม่รั่วซึม',value=1)# General การรั่วซึม CS
H19 = H19.replace(to_replace = '1 : ซึม',value=0)   # General การรั่วซึม CS
H19 = H19.replace(to_replace = 'ไม่สะอาด',value=0)
H19 = H19.replace(to_replace = 'สะอาด',value=1)
H19 = H19.replace(to_replace = 'ไม่เปลี่ยน',value=0)# General Silica gel
H19 = H19.replace(to_replace = 'เปลี่ยน',value=1) # General Silica gel
H19 = H19.replace(to_replace = 'ไม่ใส',value=0)# OLTC สภาพน้ำมัน
H19 = H19.replace(to_replace = 'ใส',value=1) # OLTC สภาพน้ำมัน
H19 = H19.replace(to_replace = 'ไม่เปิด',value=0)# General สถานะวาล์ว ครีบระบายความร้อย
H19 = H19.replace(to_replace = 'ปิด',value=0) # General สถานะวาล์ว ครีบระบายความร้อย
H19 = H19.replace(to_replace = 'เปิด',value=1) # General สถานะวาล์ว ครีบระบายความร้อย
H19 = H19.replace(to_replace = 'ไม่ทำ',value=0)# ทำความสะอาด OLTC Driver
H19 = H19.replace(to_replace = 'ทำ',value=1) # ทำความสะอาด OLTC Driver
H19 = H19.replace(to_replace = 'Normal',value=5) # DGA
H19 = H19.replace(to_replace = 'T1',value=3) # DGA
H19 = H19.replace(to_replace = 'PD',value=3) # DGA
H19 = H19.replace(to_replace = 'T2',value=1) # DGA
H19 = H19.replace(to_replace = 'T3',value=1) # DGA
H19 = H19.replace(to_replace = 'D1',value=1) # DGA
H19 = H19.replace(to_replace = 'D2',value=1) # DGA
H19 = H19.replace(to_replace = 'DT',value=1) # DGA
H19 = H19.replace(to_replace = 'nd',value= 0) # DGA
H19 = H19.replace(to_replace = ' ',value = 0)
H19 = H19.replace(to_replace = '-',value = 0)
H19 = H19.replace(to_replace = 'เปิด test tap ไม่ได้',value = 0)
H19 = H19.replace(to_replace = 'ปลดสายไม่ได้',value = 0)
H19 = H19.replace(to_replace = 'เปิด tap ไม่ได้',value = 0)
H19 = H19.replace(to_replace = 'Dyn1',value = 1)
H19 = H19.replace(to_replace = 'test tap ไม่ได้',value = 0)
H19 = H19.replace(to_replace = 'N/A',value = 0)
H19 = H19.replace(to_replace = 'NaN',value = 0)
H19 = H19.replace(to_replace = '0',value = 0)
H19 = H19.replace(to_replace = 'test ไม่ได้',value = 0) #Gen
H19 = H19.replace(to_replace = '#VALUE!',value = 0) #Gen
H19 = H19.replace(to_replace = '#DIV/0!',value = 0) #Gen
H19 = H19.replace(to_replace = 'test ไม่ได้ (Bushing)',value = 0) #Gen
H19 = H19.replace(to_replace = 'Condition 1',value = 1)
H19 = H19.replace(to_replace = 'Condition 2',value = 2)
H19 = H19.replace(to_replace = 'Condition 3',value = 3)
H19 = H19.replace(to_replace = 'Condition 4',value = 4)
H19 = H19.replace(to_replace = 'Condition 5',value = 5)
H19 = H19.replace(to_replace = 'Condition 6',value = 6)
H19 = H19.replace(to_replace = 'Condition 7',value = 7)
H19 = H19.replace(to_replace = 'Condition 8',value = 8)
H19 = H19.replace(to_replace = 'Condition 9',value = 9)
H19 = H19.replace(to_replace = 'YNyn0+d1',value = 1)
H19 = H19.replace(to_replace = 'Good',value = 3)
H19 = H19.replace(to_replace = 'normal',value = 2)
H19 = H19.replace(to_replace = 'Bad',value = 1)
H19 = H19.dropna()


# In[7]:


H19 = H19.drop(['A', 'B', 'C', 'D', 'E' ], axis=1)
H19 = H19.drop(['7_DGA'], axis=1)
# H19 = H19.drop(['1_General', '2_Active Part', '3_insulation Oil', '4_Bushing', '5_Surge arrester','6_OLTC','7_DGA'], axis=1)
# H19 = H19.drop(['General_Final Score','Active_Final Score','Oil_Final Score','Bushing_Final_Score','ARS_Final Score','OLTC_Final Score','DGA_Final Score'], axis=1)


# In[8]:


import seaborn as sns
corr = data.corr()
ax = sns.heatmap(
    corr, 
    vmin=0, vmax=1, center=0,
    cmap=sns.diverging_palette(20, 220, n=200),
    square=True
)
ax.set_xticklabels(
    ax.get_xticklabels(),
    rotation=90,
    horizontalalignment='right'
);


# In[9]:


data.describe()


# In[10]:


from sklearn.utils import shuffle
from sklearn.linear_model import LinearRegression
 
import matplotlib.pyplot as plt  
import seaborn as seabornInstance 
from sklearn.model_selection import train_test_split 

from sklearn import metrics

get_ipython().run_line_magic('matplotlib', 'inline')

from sklearn import preprocessing


# In[11]:


print("Min:", np.min(data))
print("Max:", np.max(data))


# In[12]:


np_data =data.to_numpy()
np_data =data
min_max_scaler = preprocessing.MinMaxScaler()
data_minmax = min_max_scaler.fit_transform(np_data )
y = data_minmax[:,0]
X = data_minmax[:,1:data_minmax.shape[1]]


H19_data =H19.to_numpy()
H19_data =H19
min_max_scaler = preprocessing.MinMaxScaler()
H19_minmax = min_max_scaler.fit_transform(H19_data )

y2 = H19_minmax[:,0]
X2 = H19_minmax[:,1:data_minmax.shape[1]]


# In[13]:


print("x",X)

print("x",X.shape)
print("y",y)
print("Y",y.shape)


# In[14]:


X_train, X_valid, Y_train, Y_valid = train_test_split(X, y2, test_size=0.3, random_state=0)

print('Train set shape', X_train.shape)
print('Validation set shape', X_valid.shape)


# In[15]:


# print(X_valid.shape)
# print(Y_valid.shape)
# print (X_valid)
# print (Y_valid)


# In[16]:


import tensorflow as tf


# In[17]:


import warnings


import matplotlib.pyplot as plt
from keras import optimizers
from keras.utils import plot_model
from keras.models import Sequential, Model
from keras.layers.convolutional import Conv1D, MaxPooling1D
from keras.layers import Dense, LSTM, RepeatVector, TimeDistributed, Flatten, Dropout
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
from keras.models import Sequential

get_ipython().run_line_magic('matplotlib', 'inline')
warnings.filterwarnings("ignore")


# # Set seeds to make the experiment more reproducible.
# from tensorflow import set_random_seed
# from numpy.random import seed
# set_random_seed(1)
# seed(1)

#from tensorflow import random.set_seed
from numpy.random import seed
tf.random.set_seed(1)
seed(1)


# In[18]:


X_train_series = X_train.reshape((X_train.shape[0], X_train.shape[1], 1))
X_valid_series = X_valid.reshape((X_valid.shape[0], X_valid.shape[1], 1))
X2_test_series = X2.reshape((X2.shape[0], X2.shape[1], 1))
X_test_series = X.reshape((X.shape[0], X.shape[1], 1))
print('Train set shape', X_train_series.shape)
print('Validation set shape', X_valid_series.shape)


# In[19]:


# epochs = 1000
# batch = 500
# lr = 0.000001
# adam = optimizers.Adam(lr)


# In[20]:


# look_back = 15

# # train_generator = TimeseriesGenerator(close_train, close_train, length=look_back, batch_size=20)     
# # test_generator = TimeseriesGenerator(close_test, close_test, length=look_back, batch_size=1)
# from keras.models import Sequential
# from keras.layers import LSTM, Dense

# model = Sequential()
# model.add(
#     LSTM(10,
#         activation='relu',
#         input_shape=(look_back,1))
# )
# model.add(Dense(1))
# model.compile(optimizer='adam', loss='mse')

# num_epochs = 25
# model.fit(X_train_series, epochs=num_epochs, verbose=1)


# In[21]:


print("x",X_train_series.shape)
Y_train= np.asarray(Y_train)
print("Y",Y_train.shape)


# In[22]:


# # reshape from [samples, timesteps] into [samples, timesteps, features]
# X_train = X_train.reshape((X_train.shape[0], X_train.shape[1], 1))
# #X_valid = X_valid.reshape((X_valid.shape[0], X_valid.shape[1], 1))
# Y_train= np.asarray(Y_train)
# print('Train set shape', X_train_series.shape)
# print('Validation set shape', X_valid_series.shape)

# create and fit the LSTM network
look_back = 1
# model.add(LSTM(50, activation='relu', input_shape=(n_steps, n_features)))
# model.add(Dense(1))
# model.compile(optimizer='adam', loss='mse')
model = Sequential()
model.add(LSTM(4, input_shape=(X_train.shape[1], look_back)))
model.add(Dense(1))
model.compile(loss='mean_squared_error', optimizer='adam')
model.fit(X_train_series,Y_train, epochs=100, batch_size=1, verbose=2)
# # make predictions
trainPredict = model.predict(X_train_series)
# testPredict = model.predict(X_valid_series)


# In[23]:


# def Network_ii(IN, OUT, TIME_PERIOD, EPOCHS, BATCH_SIZE, LTSM_SHAPE):
 
#     length = len(OUT)
#     train_x = IN[:int(0.9 * length)]
#     validation_x = IN[int(0.9 * length):]
#     train_y = OUT[:int(0.9 * length)]
#     validation_y = OUT[int(0.9 * length):]

#     # Define Network & callback:
#     train_x = train_x.reshape(train_x.shape[0],3, 5)
#     validation_x = validation_x.reshape(validation_x.shape[0],3, 5)
    

#     model = Sequential()
#     model.add(LSTM(units=128, return_sequences= True, input_shape=(train_x.shape[1],3)))
#     model.add(LSTM(units=128))
#     model.add(Dense(units=1))
#     model.compile(optimizer='adam', loss='mean_squared_error')

#     train_y = np.asarray(train_y)
#     validation_y = np.asarray(validation_y)
#     history = model.fit(train_x, train_y, batch_size=BATCH_SIZE, epochs=EPOCHS, validation_data=(validation_x, validation_y))

#     # Score model
#     score = model.evaluate(validation_x, validation_y, verbose=0)
#     print('Test loss:', score)
#     # Save model
#     model.save(f"models/new_model")


# In[24]:


from sklearn import metrics
from sklearn.metrics import mean_squared_error


# In[25]:


y_pred = model.predict(X_valid_series)
y_pred


# In[26]:


print(Y_valid.shape)
print(Y_valid)
Yt = Y_valid.reshape(-1,1)
#Yt = Y_valid
print(Yt.shape)
print(Yt)
print("size Yt", Yt.shape)
print("size x valid",X_valid.shape)
print(X_valid)


# In[27]:


actual = np.append(Yt, X_valid, axis=1)
print(actual.shape)
print(actual)
#actual = actual.reshape(1,-1)
#print(actual.shape)
#print(actual)

actual_sample = min_max_scaler.inverse_transform(actual)
print(actual_sample.shape)
print(actual_sample)


# In[28]:


print(y_pred.shape)
print(y_pred)
yt = y_pred.reshape(-1,1)
print(yt.shape)
print(yt)

print(X_valid.shape)
print(X_valid)


# In[29]:


aPred = np.append(yt, X_valid, axis=1)
print(aPred.shape)
print(aPred)



actual_pred = min_max_scaler.inverse_transform(aPred)
print(actual.shape)
print(actual_pred)


# In[30]:


from sklearn.metrics import mean_absolute_error
from sklearn.metrics import mean_squared_error 

cor = np.corrcoef(actual, aPred)
print("Correlation <Corr>:", cor[0][1])

mae = mean_absolute_error(actual, aPred)
print("Mean Absolute Error <MAE> (Forecast):", mae)

rmse = np.sqrt(mean_squared_error(actual, aPred))
print("Root Mean Squared Error <RMSE>:", rmse)

mse = mean_squared_error(actual, aPred)
print("Mean Square Error <MSE>:", mse)

mpe_sum = ((actual - aPred)/actual)
mpe = mpe_sum/len(actual)
print("Mean Percentage Error <MPE>:", mpe[0][0])

forecast_errors = [actual[i]-aPred[i] for i in range(len(actual))]
#print('Forecast Errors:',forecast_errors)

A = np.mean(np.abs(forecast_errors))*100
print('Mean Absolute Forecast Error <MAPE>:', A)

r2 = metrics.r2_score(actual, aPred)
print('R-squared coefficient  <R2>:', r2)


# In[31]:


actual = actual_sample[:,0]
predict = actual_pred[:,0]


# In[32]:


q = pd.DataFrame({'Actual': actual.flatten(), 'Predicted': predict.flatten()})
q


# In[33]:


print("Min:", np.min(q))
print("Max:", np.max(q))


# In[34]:


q.to_csv('test_result(csv)', index=False)


# In[35]:


#df2 = q.tail(150)
df2 = q
df2.plot(kind='line',figsize=(16,10))
plt.xlabel('Power Transformer',fontsize=15)
plt.ylabel('DGA Index',fontsize=15)
plt.title('DGA index prediction',fontsize=15)
plt.grid(which='major', linestyle='-', linewidth='0.5', color='green')
plt.grid(which='minor', linestyle=':', linewidth='0.5', color='black')
plt.show()


# In[36]:


#-------------------------------------------------------------2018 predict 2019(all)


# In[ ]:





# In[37]:


y_pred_result = model.predict(X_test_series)
y_pred_result


# In[38]:


print(y2.shape)
print(y2)
Yt = y2.reshape(-1,1)
#Yt = Y_valid
print(Yt.shape)
print(Yt)
print("size Yt", Yt.shape)
print("size x valid",X.shape)
print(X)


# In[39]:


actual = np.append(Yt, X, axis=1)
print(actual.shape)
print(actual)
#actual = actual.reshape(1,-1)
#print(actual.shape)
#print(actual)

actual_sample = min_max_scaler.inverse_transform(actual)
print(actual_sample.shape)
print(actual_sample)


# In[40]:


print(y_pred_result.shape)
print(y_pred_result)
yt = y_pred_result.reshape(-1,1)
print(yt.shape)
print(yt)

print(X.shape)
print(X)


# In[41]:


aPred = np.append(yt, X, axis=1)
print(aPred.shape)
print(aPred)



actual_pred = min_max_scaler.inverse_transform(aPred)
print(actual.shape)
print(actual_pred)
print(actual_pred.shape)
print(aPred.shape)
print(actual.shape)


# In[42]:


from sklearn.metrics import mean_absolute_error
from sklearn.metrics import mean_squared_error 

cor = np.corrcoef(actual, aPred)
print("Correlation <Corr>:", cor[0][1])

mae = mean_absolute_error(actual, aPred)
print("Mean Absolute Error <MAE> (Forecast):", mae)

rmse = np.sqrt(mean_squared_error(actual, aPred))
print("Root Mean Squared Error <RMSE>:", rmse)

mse = mean_squared_error(actual, aPred)
print("Mean Square Error <MSE>:", mse)

mpe_sum = ((actual - aPred)/actual)
mpe = mpe_sum/len(actual)
print("Mean Percentage Error <MPE>:", mpe[0][0])

forecast_errors = [actual[i]-aPred[i] for i in range(len(actual))]
#print('Forecast Errors:',forecast_errors)

A = np.mean(np.abs(forecast_errors))*100
print('Mean Absolute Forecast Error <MAPE>:', A)


r2 = metrics.r2_score(actual, aPred)
print('R-squared coefficient  <R2>:', r2)


# In[43]:


actual = actual_sample[:,0]
predict = actual_pred[:,0]
print("actual size",actual .shape)
print("actual sample size",actual_sample .shape)
print("predict size",predict .shape)
print("result size",y_pred_result .shape)


# In[44]:


q = pd.DataFrame({'Actual': actual.flatten(), 'Predicted': predict.flatten()})
q


# In[45]:


q.to_csv('test_result(csv)', index=False)


# In[46]:


df2 = q.tail(150)
df2.plot(kind='line',figsize=(16,10))
plt.grid(which='major', linestyle='-', linewidth='0.5', color='green')
plt.grid(which='minor', linestyle=':', linewidth='0.5', color='black')
plt.show()


# In[ ]:





# In[47]:


#-------------------------------------------------------------2019 predict 2020(all)
#----------- use as result


# In[ ]:





# In[48]:


y_pred_result = model.predict(X2_test_series)
y_pred_result


# In[49]:


print(y2.shape)
print(y2)
Yt = y2.reshape(-1,1)
#Yt = Y_valid
print(Yt.shape)
print(Yt)
print("size Yt", Yt.shape)
print("size x valid",X2.shape)
print(X2)


# In[50]:


actual = np.append(Yt, X2, axis=1)
print(actual.shape)
print(actual)
#actual = actual.reshape(1,-1)
#print(actual.shape)
#print(actual)

actual_sample = min_max_scaler.inverse_transform(actual)
print(actual_sample.shape)
print(actual_sample)


# In[51]:


print(y_pred_result.shape)
print(y_pred_result)
yt = y_pred_result.reshape(-1,1)
print(yt.shape)
print(yt)

print(X2.shape)
print(X2)


# In[52]:


aPred = np.append(yt, X2, axis=1)
print(aPred.shape)
print(aPred)



actual_pred = min_max_scaler.inverse_transform(aPred)
print(actual.shape)
print(actual_pred)
print(actual_pred.shape)
print(aPred.shape)
print(actual.shape)


# In[53]:


from sklearn.metrics import mean_absolute_error
from sklearn.metrics import mean_squared_error 

cor = np.corrcoef(actual, aPred)
print("Correlation <Corr>:", cor[0][1])

mae = mean_absolute_error(actual, aPred)
print("Mean Absolute Error <MAE> (Forecast):", mae)

rmse = np.sqrt(mean_squared_error(actual, aPred))
print("Root Mean Squared Error <RMSE>:", rmse)

mse = mean_squared_error(actual, aPred)
print("Mean Square Error <MSE>:", mse)

mpe_sum = ((actual - aPred)/actual)
mpe = mpe_sum/len(actual)
print("Mean Percentage Error <MPE>:", mpe[0][0])

forecast_errors = [actual[i]-aPred[i] for i in range(len(actual))]
#print('Forecast Errors:',forecast_errors)

A = np.mean(np.abs(forecast_errors))*100
print('Mean Absolute Forecast Error <MAPE>:', A)


r2 = metrics.r2_score(actual, aPred)
print('R-squared coefficient  <R2>:', r2)


# In[54]:


actual = actual_sample[:,0]
predict = actual_pred[:,0]
print("actual size",actual .shape)
print("actual sample size",actual_sample .shape)
print("predict size",predict .shape)
print("result size",y_pred_result .shape)


# In[55]:


q = pd.DataFrame({'Actual': actual.flatten(), 'Predicted': predict.flatten()})
q


# In[56]:


q.to_csv('test_result(csv)', index=False)


# In[57]:


df2 = q.tail(150)
df2.plot(kind='line',figsize=(16,10))
plt.grid(which='major', linestyle='-', linewidth='0.5', color='green')
plt.grid(which='minor', linestyle=':', linewidth='0.5', color='black')
plt.show()


# In[ ]:


# y_pred_result = model.predict(X2_test_series)
# y_pred_result

# print(y2.shape)
# print(y2)
# Yt = y2.reshape(-1,1)
# #Yt = Y_valid
# print(Yt.shape)
# print(Yt)
# print("size Yt", Yt.shape)
# print("size x valid",X2.shape)
# print(X2)

# actual = np.append(Yt, X2, axis=1)
# print(actual.shape)
# print(actual)
# #actual = actual.reshape(1,-1)
# #print(actual.shape)
# #print(actual)

# actual_sample = min_max_scaler.inverse_transform(actual)
# print(actual_sample.shape)
# print(actual_sample)

# print(y_pred_result.shape)
# print(y_pred_result)
# yt = y_pred_result.reshape(-1,1)
# print(yt.shape)
# print(yt)

# print(X2.shape)
# print(X2)

# aPred = np.append(yt, X2, axis=1)
# print(aPred.shape)
# print(aPred)



# actual_pred = min_max_scaler.inverse_transform(aPred)
# print(actual.shape)
# print(actual_pred)
# print(actual_pred.shape)
# print(aPred.shape)
# print(actual.shape)

# from sklearn.metrics import mean_absolute_error
# from sklearn.metrics import mean_squared_error 

# cor = np.corrcoef(actual, aPred)
# print("Correlation <Corr>:", cor[0][1])

# mae = mean_absolute_error(actual, aPred)
# print("Mean Absolute Error <MAE> (Forecast):", mae)

# rmse = np.sqrt(mean_squared_error(actual, aPred))
# print("Root Mean Squared Error <RMSE>:", rmse)

# mse = mean_squared_error(actual, aPred)
# print("Mean Square Error <MSE>:", mse)

# mpe_sum = ((actual - aPred)/actual)
# mpe = mpe_sum/len(actual)
# print("Mean Percentage Error <MPE>:", mpe[0][0])

# forecast_errors = [actual[i]-aPred[i] for i in range(len(actual))]
# #print('Forecast Errors:',forecast_errors)

# A = np.mean(np.abs(forecast_errors))*100
# print('Mean Absolute Forecast Error <MAPE>:', A)


# r2 = metrics.r2_score(actual, aPred)
# print('R-squared coefficient  <R2>:', r2)

# actual = actual_sample[:,0]
# predict = actual_pred[:,0]
# print("actual size",actual .shape)
# print("actual sample size",actual_sample .shape)
# print("predict size",predict .shape)
# print("result size",y_pred_result .shape)

# q = pd.DataFrame({'Actual': actual.flatten(), 'Predicted': predict.flatten()})
# q

# q.to_csv('test_result(csv)', index=False)

# df2 = q.tail(150)
# df2.plot(kind='line',figsize=(16,10))
# plt.grid(which='major', linestyle='-', linewidth='0.5', color='green')
# plt.grid(which='minor', linestyle=':', linewidth='0.5', color='black')
# plt.show()


# In[ ]:


#---------------------------------


# In[ ]:





# In[ ]:


y = y.reshape((-1))
look_back = 7
def predict(num_prediction, model):
    prediction_list = y[-look_back:]
    
    for _ in range(num_prediction):
        x = prediction_list[-look_back:]
        x = x.reshape((1, look_back, 1))
        out = model.predict(x)[0][0]
        prediction_list = np.append(prediction_list, out)
    prediction_list = prediction_list[look_back-1:]
        
    return prediction_list
    
def predict_dates(num_prediction):
    last_date = df['Date'].values[-1]
    prediction_dates = pd.date_range(last_date, periods=num_prediction+1).tolist()
    return prediction_dates

num_prediction = 2
forecast = predict(num_prediction, model)
forecast_dates = predict_dates(num_prediction)


# In[ ]:




