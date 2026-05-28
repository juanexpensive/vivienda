import streamlit as st
def render_header():
    st.title("Vivienda")
    st.subheader("Evolución del precio de la vivienda por provincia en España")
    st.write("Primera versión en construcción")

def render_body(housing_data):
    provinces = housing_data["province"].unique()
    selected_province = st.selectbox("selecciona una provincia",options=provinces)
    filtered_data = housing_data[housing_data["province"] == selected_province]
    st.dataframe(filtered_data)
    
