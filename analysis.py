# analysis.py
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud
from datetime import datetime

# Load dataset
df = pd.read_csv("metadata.csv")

# Basic info
print("Shape of dataset:", df.shape)
print("\nData types:\n", df.dtypes)
print("\nMissing values:\n", df.isnull().sum().head())

# Clean data
df['publish_time'] = pd.to_datetime(df['publish_time'], errors='coerce')
df['year'] = df['publish_time'].dt.year
df['title'] = df['title'].fillna("")

# Analysis 1: Publications per year
year_counts = df['year'].value_counts().sort_index()
plt.figure(figsize=(8,5))
sns.barplot(x=year_counts.index, y=year_counts.values, color="skyblue")
plt.title("Publications by Year")
plt.xlabel("Year")
plt.ylabel("Count")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("pubs_per_year.png")
plt.close()

# Analysis 2: Top Journals
top_journals = df['journal'].value_counts().head(10)
plt.figure(figsize=(8,5))
sns.barplot(y=top_journals.index, x=top_journals.values, palette="viridis")
plt.title("Top 10 Journals")
plt.xlabel("Number of Papers")
plt.ylabel("Journal")
plt.tight_layout()
plt.savefig("top_journals.png")
plt.close()

# Analysis 3: Word cloud of titles
text = " ".join(title for title in df['title'])
wordcloud = WordCloud(width=800, height=400, background_color="white").generate(text)
wordcloud.to_file("title_wordcloud.png")

print("✅ Analysis complete. Charts saved as:")
print("- pubs_per_year.png")
print("- top_journals.png")
print("- title_wordcloud.png")
