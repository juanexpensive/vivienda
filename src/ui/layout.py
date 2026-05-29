import streamlit as st
import pandas as pd
def render_header():
    st.title("Spain Insights")
    st.subheader("Evolution of housing prices by province in Spain")
    st.write("First version under construction")

def render_body(housing_data):
    provinces = housing_data["province"].unique()
    selected_province = st.selectbox("selecciona una provincia",options=provinces)
    filtered_data = housing_data[housing_data["province"] == selected_province]
    chart_data = filtered_data[["period","value"]]
    indexed_chart_data = chart_data.set_index("period")
    st.line_chart(indexed_chart_data)
    st.dataframe(chart_data)
