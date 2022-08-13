import streamlit as st
from predict_page import show_predict_page
from explore_page import show_explore_page
from blog_page import show_blog_page



page = st.sidebar.radio("Select a page",
("intro",
"explore", 
"predict",))

if page == "predict":
    show_predict_page()

if page == "explore":
    show_explore_page()

else:
    show_blog_page()

    