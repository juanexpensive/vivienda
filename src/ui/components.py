import streamlit as st


def render_header() -> None:
    st.title("SPain")
    st.subheader("Evolution of housing prices by province in Spain")
    st.write("First version under construction")


def render_select_periods(periods):
    col1, col2 = st.columns(2)

    first_period = col1.selectbox("select first period", options=periods, index=0)
    last_period = col2.selectbox(
        "select last period",
        options=periods,
        index=len(periods) - 1,
    )

    return first_period, last_period


def render_kpis(latest_value, variation, percentage_variation, highest_variation) -> None:
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Latest value", latest_value)
    col2.metric("Variation", variation)
    col3.metric("% of variation", f"{percentage_variation:.2f}%")
    col4.metric("province with highest variation",f"{highest_variation.name}")
