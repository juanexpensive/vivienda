import streamlit as st
from src.data.loader import load_housing_data
from src.ui.components import render_header
from src.ui.page import render_body

housing_data = load_housing_data()

st.set_page_config(page_title="S-Pain", layout="wide")
render_header()
render_body(housing_data)
