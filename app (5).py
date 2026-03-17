import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

@st.cache_data
def load_data():
    return pd.read_csv("/content/netflix_user_behavior_dataset[1].csv")

df = load_data()

st.title("🎬 Netflix User Behavior App")

st.subheader("Dataset Overview")
st.write(df.shape)
st.dataframe(df.head())

# Watch Time
if 'Watch Time (Hours)' in df.columns:
    st.subheader("Watch Time Distribution")
    fig, ax = plt.subplots()
    sns.histplot(df['Watch Time (Hours)'], ax=ax)
    st.pyplot(fig)

# Genre
if 'Favorite Genre' in df.columns:
    st.subheader("Genre Popularity")
    fig, ax = plt.subplots()
    df['Favorite Genre'].value_counts().plot(kind='bar', ax=ax)
    st.pyplot(fig)

# User Prediction
st.subheader("User Type Prediction")

watch_time = st.slider("Watch Time", 0, 100, 10)

if watch_time > 40:
    st.success("Binge Watcher")
elif watch_time > 20:
    st.success("Regular Viewer")
else:
    st.success("Casual Viewer")
