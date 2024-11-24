import streamlit as st

st.set_page_config(layout="wide")

col1,col2, = st.columns(2)

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