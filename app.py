# app.py
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="CORD-19 Data Explorer", layout="wide")

# Load data
df = pd.read_csv("metadata.csv")
df['publish_time'] = pd.to_datetime(df['publish_time'], errors='coerce')
df['year'] = df['publish_time'].dt.year
df['title'] = df['title'].fillna("")

# Title & description
st.title("🔬 CORD-19 Data Explorer")
st.write("Interactive exploration of COVID-19 research papers metadata.")

# Sidebar filter
years = st.slider("Select publication year range:",
                  int(df['year'].min()) if df['year'].notnull().any() else 2019,
                  int(df['year'].max()) if df['year'].notnull().any() else 2022,
                  (2020, 2021))

filtered_df = df[(df['year'] >= years[0]) & (df['year'] <= years[1])]

st.subheader("📊 Sample of Data")
st.dataframe(filtered_df[['title', 'authors', 'journal', 'publish_time']].head(20))

# Visualizations
st.subheader("📈 Publications per Year")
year_counts = filtered_df['year'].value_counts().sort_index()
fig, ax = plt.subplots()
ax.bar(year_counts.index, year_counts.values, color="skyblue")
ax.set_title("Publications per Year")
st.pyplot(fig)

st.subheader("🏛️ Top Journals")
top_journals = filtered_df['journal'].value_counts().head(10)
fig, ax = plt.subplots()
ax.barh(top_journals.index, top_journals.values, color="green")
ax.set_title("Top 10 Journals")
st.pyplot(fig)

st.subheader("☁️ Word Cloud of Titles")
st.image("title_wordcloud.png", use_column_width=True)

st.success("App ready! Adjust the filters to explore the dataset.")
