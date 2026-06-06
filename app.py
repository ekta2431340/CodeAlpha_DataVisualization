import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.title("Netflix Data Visualization Dashboard")

df = pd.read_csv("netflix_titles.csv")

st.subheader("Dataset Preview")
st.dataframe(df.head())

# Movies vs TV Shows

st.subheader("Movies vs TV Shows")
fig, ax = plt.subplots()
sns.countplot(x='type', data=df, ax=ax)
st.pyplot(fig)

# Top Countries

st.subheader("Top 10 Countries")
fig, ax = plt.subplots(figsize=(10,5))
df['country'].value_counts().head(10).plot(kind='bar', ax=ax)
st.pyplot(fig)

# Top Ratings

st.subheader("Top Ratings")
fig, ax = plt.subplots(figsize=(10,5))
sns.countplot(y='rating', data=df,
order=df['rating'].value_counts().index[:10], ax=ax)
st.pyplot(fig)

# Release Trend

st.subheader("Release Year Trend")
fig, ax = plt.subplots(figsize=(10,5))
df['release_year'].value_counts().sort_index().tail(20).plot(ax=ax)
st.pyplot(fig)