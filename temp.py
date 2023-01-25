# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import streamlit as smt 
import pandas as pd 
import seaborn as se 


smt.title('datavisualization')
smt.subheader("data analaysis using python & streamlit")

upload = smt.file_uploader("upload the dataset and csv format")
if upload is not None:
    data=pd.read_csv(upload)

#  3. Show Dataset
if upload is not None:
    if smt.checkbox("Preview dataset"):
        if smt.button('head'):
            smt.write(data.head())
        if smt.button("tail"):
            smt.write(data.tail())

# 4. Check DataType of Each Column

if upload is not None:
    if smt.checkbox('data type of each column'):
        smt.text('data types')
        smt.write(data.dtypes)
        

# 5. Find Shape of Our Dataset (Number of Rows And Number of Columns)
if upload is not None:
    data_shape = smt.radio("What Dimension Do You Want To Check?",('Rows','Columns'))
    if data_shape=='Rows':
        smt.text("Number of Rows")
        smt.write(data.shape[0])
    if data_shape=='Columns':
        smt.text("Number of Columns")
        smt.write(data.shape[1])
        
# 6. Find Null Values in The Dataset
if upload is not None:
    test = data.isnull().values.any()
    if test == True:
        if smt.checkbox('null value in the dataset'):
            se.heatmap(data.isnull())
            smt.pyplot()
    else:
        smt.success("Congratulations!!!,No Missing Values")
        
# 7. Find Duplicate Values in the dataset
if upload is not None:
    test = data.duplicated().any()
    if test == True:
        smt.warning("they dataset contain the some dublicated value")
        dub = smt.selectbox("Do You Want to Remove Duplicate Values?", \
                        ("Select One","Yes","No"))
        if dub == "Yes":
            data = data.drop_duplicates()
            smt.text("dublicate value are removed")
            smt.write(data)
        if dub == "No":
            smt.text("ok no problem")

# 8. Get Overall Statistics
if upload is not None:
    if smt.checkbox("Summary of The Dataset"):
        smt.write(data.describe(include='all'))
        
# # 9. About Section

if smt.button("About App"):
    smt.text("Built With Streamlit")
    smt.text("Thanks To Streamlit")


#  download updated file

if smt.button('Save DataFrame'):
    open('Netflix Dataset.csv','w').write(data.to_csv())
    smt.text("Saved To local Drive")
    
