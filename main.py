import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import re

df=pd.read_csv('titanic_data.csv')

st.header("Data set")

with st.sidebar:
    st.image('download.jpg')
    st.title("Titanic Data set Analysis")
df['Title'] = df['Name'].apply(lambda x: re.search('([A-Z][a-z]+)\.', x).group(1))
df['Title'] = df['Title'].replace('Mlle', 'Miss')
df['Title'] = df['Title'].replace('Mme', 'Mrs')
df.loc[(~df['Title'].isin(['Mr', 'Mrs', 'Miss', 'Master'])), 'Title'] = 'Rare Title'
plot=sns.countplot(data=df,x='Title', hue='Survived')
df['Fsize'] = df['SibSp'] + df['Parch']+1

sex=st.selectbox("Sex",['male','female'])
st.bar_chart(data=df,x='Sex',y='Survived')
st.line_chart(data=df,x='Age',y='Survived')
df['Age'].fillna(int(df['Age'].mean()),inplace=True)
df['bins'] = pd.cut(x=df['Age'], bins=[1, 20, 40, 60, 80, 100])
st.write(df['bins'].unique())
st.write(df)