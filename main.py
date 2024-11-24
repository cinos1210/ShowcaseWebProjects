import streamlit as st
import pandas as pd

st.Page("main.py",title="Arturo Cruz")

st.set_page_config(layout="wide")

col1,col2= st.columns(2)

with col1:
    st.image("images/ProfilePhoto.jpg")

with col2:
    st.title("Arturo Cruz")
    content = """Hi, I'm Arturo I am a self-learner programmer and a game developer.
     I graduate in 2024 and since then I've been  working on multiple projects related
     to web development with unreal engine, unity and godot among others.
     I have experience working on VR, AR and MR games and applications, working with the 
     most advance framework and technologies, providing my work to many clients in the past 
     3 years."""

    st.info(content)

content2 = """Below you can find my projects. Feel free to contact me"""
st.write(content2)



col3, empty_col,col4 = st.columns(3)

col3, empty_col, col4 = st.columns([1.5,0.5,1.5])

df = pd.read_csv("data.csv",sep=";")

with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])
        img = f"images/{row["image"]}"
        st.image(img)
        description = row["description"]
        st.write(description)
        st.write(f"[Source Code]({row["url"]})")

with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])
        img = f"images/{row["image"]}"
        st.image(img)
        st.write(description)
        st.write(f"[Source Code]({row["url"]})")