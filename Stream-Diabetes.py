#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pickle
import streamlit as st


# In[9]:


import pickle

with open("diabetes_model.sav", "rb") as f:
    diabetes_model = pickle.load(f)


# In[17]:


st.title('Data Mining Prediksi Diabetes')


# In[65]:


col1, col2 = st.columns(2)
with col1 : 
    Pregnancies = st.text_input ('Pregnancies')

with col2 : 
    Glucose = st.text_input ('Glucose')

with col1 :
    BloodPressure = st.text_input ('Blood Pressure')

with col2 :
    SkinThickness = st.text_input ('SkinThickness')

with col1 :
    Insulin = st.text_input ('Insulin')

with col2 :
    BMI = st.text_input ('BMI')

with col1 :
    DiabetesPedigreeFunction = st.text_input ('Diabetes Pedigree Function')

with col2 :
    Age = st.text_input ('Age')


# In[67]:


diabetes_diagnosis = ''


# In[69]:


if st.button('Test Prediksi Diabetes'):
    diabetes_diagnosis = diabetes_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness,
                                                   Insulin, BMI, DiabetesPedigreeFunction, Age]])
    if diabetes_diagnosis[0] == 1:
        diabetes_diagnosis = "Pasien terkena diabetes"
    else:
        diabetes_diagnosis = "Pasien tidak terkena diabetes"


# In[63]:


st.success(diabetes_diagnosis)


# In[ ]:




