import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np


@st.cache
def load_data():
    df = pd.read_csv('50_Startups.csv')
    return df

df = load_data()

def show_explore_page():
    st.title('About the Dataset')
    
    f1 = plt.figure()
    f2 = plt.figure()
    tot_rd = df['R&D Spend'].max()
    tot_admin = df['Administration'].max()
    tot_market = df['Marketing Spend'].max()
    values = [tot_rd,tot_admin,tot_market]
    lable = ['rnd','administration','marketing spend']
    fig1 = plt.figure(figsize = (10, 5))
    plt.bar(lable,values, color ='maroon',
        width = 0.4)
    st.write("""### Total spends dedicated for each categories""")
    st.pyplot(fig1,clear_fig=True)


    fig2 = plt.figure(figsize=(10, 5))
    sns.heatmap(df.corr(), cmap="YlGnBu", annot=True)
    st.write("""### Heatmap of coorelation""")
    st.pyplot(fig2,clear_fig=True)


    ind = st.number_input("enter company number",0,50)
    total_spent = (df['R&D Spend'][ind]+df['Administration'][ind]+df['Marketing Spend'][ind])
    st.metric('rnd spend',df['R&D Spend'][ind])
    st.metric('admin spend',df['Administration'][ind])
    st.metric('market spend',df['Marketing Spend'][ind])
    st.metric('profit margin',np.round_(((df['R&D Spend'][ind]+df['Administration'][ind]+df['Marketing Spend'][ind]+df['Profit'][ind])-(df['R&D Spend'][ind]+df['Administration'][ind]+df['Marketing Spend'][ind]))/(df['R&D Spend'][ind]+df['Administration'][ind]+df['Marketing Spend'][ind]+df['Profit'][ind])*100))
    st.metric('total spending',round(total_spent))


    st.write("""### Profits of each company""")
    fig3 = plt.figure(figsize=(10, 5))
    ax = sns.barplot(x=df.index,y="Profit", data=df)
    st.pyplot(fig3)

    st.write("""### Profit margins of each company""")
    profit_margins = {}
    def profmar():
        for ind in df.index:
            prof_margin = ((df['R&D Spend'][ind]+df['Administration'][ind]+df['Marketing Spend'][ind]+df['Profit'][ind])-(df['R&D Spend'][ind]+df['Administration'][ind]+df['Marketing Spend'][ind]))/(df['R&D Spend'][ind]+df['Administration'][ind]+df['Marketing Spend'][ind]+df['Profit'][ind])*100
            profit_margins["company {0}".format(ind)] = prof_margin
        return profit_margins
    company_names = list(range(0,50))
    p_margins = list(profmar().values())
    fig4 = plt.figure(figsize = (25, 12.5))
    ax = sns.barplot(x = company_names,y= p_margins)
    st.pyplot(fig4)

