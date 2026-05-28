import streamlit as st
from src.data.loader import  load_housing_data

def render_header():
    st.title("Vivienda")
    st.subheader("Evolución del precio de la vivienda por provincia en España")
    st.write("Primera versión en construcción")

def render_body(): 
    housing_data = load_housing_data()
    st.dataframe(housing_data)