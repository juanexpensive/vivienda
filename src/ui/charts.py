import altair as alt
import pandas as pd
import streamlit as st


def render_chart(
    chart_data: pd.DataFrame,
    selected_province: str,
    first_period,
    last_period,
) -> None:
    st.write(
        f"Historical evolution in {selected_province} between {first_period} - {last_period}"
    )

    line_chart = (
        alt.Chart(chart_data)
        .mark_line(point=True)
        .encode(
            x=alt.X("period:O", title="Period"),
            y=alt.Y("value:Q", title="Value"),
            tooltip=["period", "value"],
        )
        .properties(width="container")
    )

    st.altair_chart(line_chart, width="stretch")
    st.dataframe(chart_data)
