import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
st.header("Plotly Demonstration")
df = px.data.gapminder().query("continent=='Oceania'")
st.write(df)
#Simple Line chart
st.header("Simple Line chart")
fig = px.line(df, x="year", y="lifeExp", color='country')
st.plotly_chart(fig)
df = pd.DataFrame(dict(
    x = [1, 3, 2, 4],
    y = [1, 2, 3, 4]
))
fig = px.line(df, x="x", y="y", title="Unsorted Input") 
st.plotly_chart(fig)
fig= px.line(df.sort_values(by='x'),x="x", y="y", title="sorted Input",markers=True)
st.plotly_chart(fig)


st.write("Advanced Line chart")
df = px.data.gapminder().query("country in ['Canada', 'Botswana']")
fig = px.line(df, x="lifeExp", y="gdpPercap", color="country", text="year")
fig.update_traces(textposition="bottom right")
st.plotly_chart(fig)

st.header("Different Type of charts")
np.random.seed(1)

N = 100
random_x = np.linspace(0, 1, N)
random_y0 = np.random.randn(N) + 5
random_y1 = np.random.randn(N)
random_y2 = np.random.randn(N) - 5

# Create traces
fig = go.Figure()
fig.add_trace(go.Scatter(x=random_x, y=random_y0,
                    mode='lines',
                    name='line chart'))
fig.add_trace(go.Scatter(x=random_x, y=random_y1,
                    mode='lines+markers',
                    name='lines+markers'))
fig.add_trace(go.Scatter(x=random_x, y=random_y2,
                    mode='markers', name='markers'))
st.plotly_chart(fig)
#Titanic Dataset
df= pd.read_csv("titanic_data.csv")

df['Age'].fillna(int(df["Age"].mean()),inplace=True)
st.write(df)
fig=px.line(df[0:50],y='PassengerId',x='Age',markers=True)
st.plotly_chart(fig)

fig=px.box(df,y='Age',points='all')
st.plotly_chart(fig)