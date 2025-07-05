import streamlit as st
import langchain_helper

st.title("🍷 RESTAURANT NAME & MENU GENERATOR ✨")
cuisine=st.sidebar.selectbox("select a cuisine",("Indian","American","Arabic","Europian","Chinese","Japanese","African","Oceanian","Middle eastern"))

if cuisine:
    response=langchain_helper.generate_restaurant_name_items(cuisine)
    st.header(response['restaurant_name'].strip())
    menu_items=response['menu_items'].strip().split(",")
    st.subheader("🍽 MENU-ITEMS 🍽")
    for item in menu_items:
        st.write("-",item) 