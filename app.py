import streamlit as st
from src.ui.layout import render_header, render_body

st.set_page_config(page_title="Vivienda", layout="wide")
render_header()
render_body()