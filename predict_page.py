import streamlit as st
import pickle
import numpy as np

def load_model():
    with open('linear_startup.pkl','rb') as file:
        data = pickle.load(file)
    return data

data = load_model()

def show_predict_page():
    st.title('Startup profit prediction')
    st.write("""### Give us your preferance""")


    rnd = st.slider("R&D Spendings",0,1000000,1000)
    admin = st.slider("Administration spendings",0,1000000,1000)
    market = st.slider("Marketing spendings",0,1000000,1000)

    predx = [rnd,admin,market]
    predxnp = np.array(predx)
    predxnp = predxnp.reshape(1,-1)
    print(predxnp)

    ok = st.button("calculate price")

    if ok:
        profit = data.predict(predxnp)
        profit = np.round_(profit)
        st.subheader(f"Your predicted profit would be {profit[0]}")
        prof_margin = round(((rnd+admin+market+profit[0]-(rnd+admin+market))/(rnd+admin+market+profit[0])*100))
        st.subheader(f"and profit margin is {prof_margin}%")


