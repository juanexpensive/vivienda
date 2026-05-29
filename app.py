import streamlit as st
from src.ui.layout import render_header, render_body
from src.data.loader import load_housing_data

housing_data = load_housing_data()
column = housing_data.columns.tolist()

st.set_page_config(page_title="Spain Insigths", layout="wide")
render_header()
render_body(housing_data)