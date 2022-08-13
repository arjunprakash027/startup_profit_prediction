import streamlit as st

def show_blog_page():
    with open('intro.txt') as f:
        contents = f.read()
        with st.expander("where to spend as an startup"):
            st.write(contents)

    with open('rnd_budget.txt',encoding ='utf8') as k:
        rnd = k.read()
        with st.expander("how to allocate rnd budget"):
            st.write(rnd)

    with open('marketing_budget.txt',encoding ='utf8') as l:
        mark = l.read()
        with st.expander("how to allocate marketing budget"):
            st.write(mark)
    
    with open('admin_budget.txt',encoding ='utf8') as a:
        admin = a.read()
        with st.expander("how to allocate administration budget"):
            st.write(admin)
    
    