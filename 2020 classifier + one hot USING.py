#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import seaborn as sn
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import pickle
import xlrd
import sklearn
from sklearn.model_selection import train_test_split
from sklearn.model_selection import RandomizedSearchCV
from sklearn.model_selection import GridSearchCV
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import accuracy_score
from sklearn import metrics
from sklearn.datasets import load_iris
from sklearn import preprocessing
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import confusion_matrix
from sklearn.utils.multiclass import unique_labels
#from sklearn.metrics import plot_confusion_matrix
from sklearn.neural_network import MLPClassifier
from sklearn.preprocessing import OneHotEncoder


from sklearn import tree
import xlsxwriter
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
dataset = pd.ExcelFile(r'D:\Result\LSTM\Colab\Hi accurancy\Data 1000 epoach.xlsx')
#dataset = pd.ExcelFile(r'D:\Result\LSTM\Reg.xlsx')
dataset.sheet_names


# In[2]:


data = dataset.parse('2018+2019')
#data = dataset.parse('2018+2019 condition')
#data = dataset.parse('2019 condition')
#H19 = dataset.parse('2020 predict final')
H19 = dataset.parse('2020 LSTM predict')
#H19 = dataset.parse('2020 prediction keep')
A = dataset.parse('2019')
print (data)
print(type(data))
data.shape


# In[3]:


A = A.replace(to_replace = 'Condition 1',value = 1)
A = A.replace(to_replace = 'Condition 2',value = 2)
A = A.replace(to_replace = 'Condition 3',value = 3)
A = A.replace(to_replace = 'Condition 4',value = 4)
A = A.replace(to_replace = 'Condition 5',value = 5)
A = A.replace(to_replace = 'Condition 6',value = 6)
A = A.replace(to_replace = 'Condition 7',value = 7)
A = A.replace(to_replace = 'Condition 8',value = 8)
A = A.replace(to_replace = 'Condition 9',value = 9)


# In[4]:


# data = data.replace(to_replace = 'Condition 1',value = 1)
# data = data.replace(to_replace = 'Condition 2',value = 2)
# data = data.replace(to_replace = 'Condition 3',value = 3)
# data = data.replace(to_replace = 'Condition 4',value = 4)
# data = data.replace(to_replace = 'Condition 5',value = 5)
# data = data.replace(to_replace = 'Condition 6',value = 6)
# data = data.replace(to_replace = 'Condition 7',value = 7)
# data = data.replace(to_replace = 'Condition 8',value = 8)
# data = data.replace(to_replace = 'Condition 9',value = 9)


# In[5]:


#data = data.drop(['A', 'B', 'C', 'D', 'E', ], axis=1)
data = data.drop(['H_Index','Overall HI'], axis=1)
#data = data.drop(['2018_%Im'], axis=1)
#data = data.drop(['1_General', '2_Active Part', '3_insulation Oil', '4_Bushing', '5_Surge arrester','6_OLTC','7_DGA'], axis=1)
#data = data.drop(['General_Final Score','Active_Final Score','Oil_Final Score','Bushing_Final_Score','ARS_Final Score','OLTC_Final Score','DGA_Final Score'], axis=1)


# In[6]:


# H19 = H19.replace(to_replace = 'Condition 1',value = 1)
# H19 = H19.replace(to_replace = 'Condition 2',value = 2)
# H19 = H19.replace(to_replace = 'Condition 3',value = 3)
# H19 = H19.replace(to_replace = 'Condition 4',value = 4)
# H19 = H19.replace(to_replace = 'Condition 5',value = 5)
# H19 = H19.replace(to_replace = 'Condition 6',value = 6)
# H19 = H19.replace(to_replace = 'Condition 7',value = 7)
# H19 = H19.replace(to_replace = 'Condition 8',value = 8)
# H19 = H19.replace(to_replace = 'Condition 9',value = 9)


# In[7]:


#data = data.drop(['A', 'B', 'C', 'D', 'E', ], axis=1)
H19 = H19.drop(['H_Index','Overall HI'], axis=1)
#H19 = H19.drop(['2018_%Im'], axis=1)
# H19 = H19.drop(['1_General', '2_Active Part', '3_insulation Oil', '4_Bushing', '5_Surge arrester','6_OLTC','7_DGA'], axis=1)
# H19 = H19.drop(['General_Final Score','Active_Final Score','Oil_Final Score','Bushing_Final_Score','ARS_Final Score','OLTC_Final Score','DGA_Final Score'], axis=1)


# In[8]:


# np_data =data.to_numpy()
# np_data =data
y = data['Condition']
X = data.drop(['Condition'], axis=1)
print(y)
y2 = H19['Condition']
X2 = H19.drop(['Condition'], axis=1)

y3 = A['Condition']
# y = data[:,0]
# X = data[:,1:data.shape[1]]
print("x",X)
print("y",y)


# In[9]:


from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder


lec = LabelEncoder()
y = lec.fit_transform(y)
y = y.reshape(-1,1)

ohe = OneHotEncoder(sparse=False)
y = ohe.fit_transform(y)
y


   


# In[10]:


# np_data =data.to_numpy()
# np_data =data
y = data['Condition']
X = data.drop(['Condition'], axis=1)

y2 = H19['Condition']
X2 = H19.drop(['Condition'], axis=1)
# y = data[:,0]
# X = data[:,1:data.shape[1]]
#print("x",X)
print("y",y)


# In[11]:



# min_max_scaler = preprocessing.MinMaxScaler()
# data_minmax = min_max_scaler.fit_transform(X )
# X = data_minmax[:,1:data.shape[1]]


# # H19_data =H19.to_numpy()
# # H19_data =H19
# # min_max_scaler = preprocessing.MinMaxScaler()
# # H19_minmax = min_max_scaler.fit_transform(H19_data )

# # y2 = H19_minmax[:,0]
# # X2 = H19_minmax[:,1:data_minmax.shape[1]]


# In[12]:


min_max_scaler = preprocessing.MinMaxScaler()
X = min_max_scaler.fit_transform(X)
X2 = min_max_scaler.fit_transform(X2)


# In[13]:


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)

print('Train set shape', X_train.shape)
print('Validation set shape', X_test.shape)
print('Train set shape', y_train.shape)
print('Validation set shape', y_test.shape)


# In[14]:


# print('Train set shape', X_train_series.shape)
# print('Validation set shape', X_valid_series.shape)


# In[15]:


from sklearn.svm import SVC
SVR = SVC() # Linear Kernel
#Train the model using the training sets
SVR.fit(X_train, y_train)
# SVR.fit(HI_X2_train, HI_y2_train)
#SVR.fit(X, y)
#Predict the response for test dataset
#HI_y_pred  = SVR.predict(HI_X_test)
con_pred  = SVR.predict(X_test)
print("result_test")
print(y_test)
print("result")
print(con_pred)
print("K")
type(con_pred)
print("K")
type(y_test)


# In[16]:


params = SVR.get_params()
print("parameter ",params)
print("Results of SVM")
print("Accuracy:",metrics.accuracy_score(y_test,con_pred))
print(metrics.classification_report(y_test,con_pred))
C = metrics.confusion_matrix(y_test,con_pred)
print("confusion metric ",C)


# In[17]:


print("SVM Eva")
q = pd.DataFrame({'Actual': y_test, 'Predicted': con_pred.flatten()})
q


# In[18]:


row = len(y_test.index)
A = np.arange(0, row, 1).tolist()

plt.plot(A,y_test, color='blue' , label='Actual')
plt.plot(A, con_pred, color='red', label='Predict')
plt.plot(figsize=(16,10))
plt.legend(loc="lower right")
plt.ylim((0,10))
plt.grid(which='major', linestyle='-', linewidth='0.3', color='green')
plt.grid(which='minor', linestyle=':', linewidth='0.5', color='black')
plt.xlabel('Power Transformer')
plt.ylabel('Maintenance Condition')
plt.title('Maintenance Condition prediction using Support Vector Machines')
plt.show()


# In[19]:


row = len(y_test.index)
A = np.arange(0, row, 1).tolist()

plt.scatter(A,y_test, color='blue' , label='Actual')
plt.scatter(A, con_pred, color='red', label='Predict',marker='x')
plt.plot(figsize=(16,10))
plt.legend(loc="lower right")
plt.ylim((0,10))
plt.grid(which='major', linestyle='-', linewidth='0.3', color='green')
plt.grid(which='minor', linestyle=':', linewidth='0.5', color='black')
plt.xlabel('Power Transformer')
plt.ylabel('Maintenance Condition')
plt.title('Maintenance Condition prediction using Support Vector Machines')
plt.show()


# In[20]:


con_pred2  = SVR.predict(X2)


# In[21]:


print('SVC 2020')
q = pd.DataFrame({'Actual': y3, 'Predicted': con_pred2.flatten()})
q


# In[22]:


#-----------------------------------------


# In[ ]:





# In[23]:


from sklearn.neighbors import KNeighborsClassifier
knnC = KNeighborsClassifier()
knnC.fit(X_train, y_train)
con_pred = knnC.predict(X_test)
print("y_test")
print(y2)
print("perdict")
print(con_pred)



# In[24]:


print("KNN Eva")
q = pd.DataFrame({'Actual': y_test, 'Predicted': con_pred.flatten()})
q


# In[25]:


params = knnC.get_params()
print("parameter ",params)
print("Results of KNN")
print("Accuracy:",metrics.accuracy_score(y_test,con_pred))
print(metrics.classification_report(y_test,con_pred))
C = metrics.confusion_matrix(y_test,con_pred)
print("confusion metric ",C)


# In[26]:


row = len(y_test.index)
A = np.arange(0, row, 1).tolist()
plt.plot(A, con_pred, color='red', label='Predict')
plt.plot(A,y_test, color='blue' , label='Actual')
plt.plot(figsize=(16,10))
plt.legend(loc="lower right")
plt.ylim((0,10))
plt.grid(which='major', linestyle='-', linewidth='0.3', color='green')
plt.grid(which='minor', linestyle=':', linewidth='0.5', color='black')
plt.xlabel('Power Transformer')
plt.ylabel('Maintenance Condition')
plt.title('Maintenance Condition prediction using k_Nearest neighbor')
plt.show()


# In[27]:


row = len(y_test.index)
A = np.arange(0, row, 1).tolist()

plt.scatter(A,y_test, color='blue' , label='Actual')
plt.scatter(A, con_pred, color='red', label='Predict',marker='x')
plt.plot(figsize=(16,10))
plt.legend(loc="lower right")
plt.ylim((0,10))
plt.grid(which='major', linestyle='-', linewidth='0.3', color='green')
plt.grid(which='minor', linestyle=':', linewidth='0.5', color='black')
plt.xlabel('Power Transformer')
plt.ylabel('Maintenance Condition')
plt.title('Maintenance Condition prediction using k_Nearest neighbor')
plt.show()


# In[28]:


con_pred = knnC.predict(X2)


# In[29]:


print('Knn 2020')
q = pd.DataFrame({'Actual': y3, 'Predicted': con_pred2.flatten()})
q


# In[ ]:





# In[30]:


#------------------------------------------


# In[31]:


from sklearn.tree import DecisionTreeClassifier
DecisionClass = DecisionTreeClassifier(criterion="entropy")
#DecisionClass = DecisionTreeClassifier()
DecisionClass.fit(X_train, y_train)
con_pred = DecisionClass.predict(X_test)
#HI_y_pred = DecisionClass.predict(X)
print("y_test")
print(y2)
print("result")
print(con_pred)


# In[32]:


print("Decision Eva")
q = pd.DataFrame({'Actual': y_test, 'Predicted': con_pred.flatten()})
q


# In[33]:


params = DecisionClass.get_params()
print("parameter ",params)
print("Results of Decision tree")
print("Accuracy:",metrics.accuracy_score(y_test,con_pred))
print(metrics.classification_report(y_test,con_pred))
C = metrics.confusion_matrix(y_test,con_pred)
print("confusion metric ",C)


# In[34]:


row = len(y_test.index)
A = np.arange(0, row, 1).tolist()
plt.plot(A, con_pred, color='red', label='Predict')
plt.plot(A,y_test, color='blue' , label='Actual')
plt.plot(figsize=(16,10))
plt.legend(loc="lower right")
plt.ylim((0,10))
plt.grid(which='major', linestyle='-', linewidth='0.3', color='green')
plt.grid(which='minor', linestyle=':', linewidth='0.5', color='black')
plt.xlabel('Power Transformer')
plt.ylabel('Maintenance Condition')
plt.title('Maintenance Condition prediction using Decision tree')
plt.show()


# In[35]:


row = len(y_test.index)
A = np.arange(0, row, 1).tolist()

plt.scatter(A,y_test, color='blue' , label='Actual')
plt.scatter(A, con_pred, color='red', label='Predict',marker='x')
plt.plot(figsize=(16,10))
plt.legend(loc="lower right")
plt.ylim((0,10))
plt.grid(which='major', linestyle='-', linewidth='0.3', color='green')
plt.grid(which='minor', linestyle=':', linewidth='0.5', color='black')
plt.xlabel('Power Transformer')
plt.ylabel('Maintenance Condition')
plt.title('Maintenance Condition prediction using Decision tree')
plt.show()


# In[36]:


con_pred2 = DecisionClass.predict(X2)


# In[37]:


print('Decision 2020')
q = pd.DataFrame({'Actual': y3, 'Predicted': con_pred2.flatten()})
q


# In[ ]:





# In[38]:


#------------------------------------------------------------


# In[39]:


from sklearn.ensemble import RandomForestRegressor
from sklearn.ensemble import RandomForestClassifier
regr = RandomForestClassifier()

regr.fit(X_train, y_train)
con_pred  = regr.predict(X_test)
#HI_y_pred  = regr.predict(X)

print("y_test")
print(y2)
print("result")
print(con_pred)


# In[40]:


print("Random EVa")
q = pd.DataFrame({'Actual': y_test, 'Predicted': con_pred.flatten()})
q


# In[41]:


params = regr.get_params()
print("parameter ",params)
print("Results of Random forest")
print("Accuracy:",metrics.accuracy_score(y_test,con_pred))
print(metrics.classification_report(y_test,con_pred))
C = metrics.confusion_matrix(y_test,con_pred)
print("confusion metric ",C)


# In[42]:


row = len(y_test.index)
A = np.arange(0, row, 1).tolist()
plt.plot(A, con_pred, color='red', label='Predict')
plt.plot(A,y_test, color='blue' , label='Actual')
plt.plot(figsize=(16,10))
plt.legend(loc="lower right")
plt.ylim((0,10))
plt.grid(which='major', linestyle='-', linewidth='0.3', color='green')
plt.grid(which='minor', linestyle=':', linewidth='0.5', color='black')
plt.xlabel('Power Transformer')
plt.ylabel('Maintenance Condition')
plt.title('Maintenance Condition prediction using Random forest')
plt.show()


# In[43]:


con_pred2  = regr.predict(X2)


# In[44]:


print('Random Forest 2020')
q = pd.DataFrame({'Actual': y3, 'Predicted': con_pred2.flatten()})
q


# In[45]:


row = len(y_test.index)
A = np.arange(0, row, 1).tolist()
plt.scatter(A,y_test, color='blue' , label='Actual')
plt.scatter(A, con_pred, color='red', label='Predict',marker='x')

plt.plot(figsize=(16,10))
plt.legend(loc="lower right")
plt.ylim((0,10))
plt.grid(which='major', linestyle='-', linewidth='0.3', color='green')
plt.grid(which='minor', linestyle=':', linewidth='0.5', color='black')
plt.xlabel('Power Transformer')
plt.ylabel('Maintenance Condition')
plt.title('Maintenance Condition prediction using Random forest')
plt.show()


# In[46]:


#____________________________________


# In[ ]:





# In[ ]:




