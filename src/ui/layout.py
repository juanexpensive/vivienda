import streamlit as st
import pandas as pd
import altair as alt

def render_header():
    st.title("Spain Insights")
    st.subheader("Evolution of housing prices by province in Spain")
    st.write("First version under construction")

def prepare_periods(sorted_province_data : pd.DataFrame):
    periods = sorted_province_data["period"].unique()
    return periods

def render_select_periods(periods):
    col1, col2 = st.columns(2)

    first_period = col1.selectbox("select first period", options=periods, index = 0)
    last_period = col2.selectbox("select last period", options = periods, index = len(periods)-1)

    if first_period > last_period:
        st.write("Wrong formatting, swapped periods")
        box = first_period
        first_period = last_period
        last_period = box
    return first_period, last_period

def calculate_kpis(sorted_province_data: pd.DataFrame):
    # Take the last and first rows of the selected province period.
    latest_row = sorted_province_data.iloc[-1]
    first_row = sorted_province_data.iloc[0]

    # Extract the numeric values we want to compare.
    latest_value = latest_row["value"]
    first_value = first_row["value"]

    # Absolute change across the selected time period.
    variation = latest_value - first_value

    # Percentage change needs a zero check to avoid division errors.
    if first_value != 0:
        percentage_variation = (variation / first_value) * 100
    else:
        percentage_variation = 0

    # Return all KPI values so render_body() can use them.
    return latest_value, variation, percentage_variation

def render_kpis(latest_value, variation, percentage_variation):
    # Show the three headline metrics for the selected province.
    col1, col2, col3 =  st.columns(3)
    col1.metric("Latest value", latest_value)
    col2.metric("Variation", variation)
    col3.metric("% of variation", f"{percentage_variation:.2f}%")

def render_chart(
    chart_data: pd.DataFrame,
    selected_province: str,
    first_period,
    last_period
) -> None:
    # Draw the chart title, the line chart, and the supporting data table.
    st.write(f"Historical evolution in {selected_province} between {first_period} - {last_period}")

    # Build an explicit chart so Streamlit does not guess extra series or axes.
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

def render_body(housing_data: pd.DataFrame) -> None:
    # Build the province dropdown from the provinces available in the dataset.
    provinces = housing_data["province"].unique()
    selected_province = st.selectbox("select a province", options=provinces)

    # Keep only the rows that belong to the selected province.
    province_data: pd.DataFrame = housing_data[housing_data["province"] == selected_province]
    
    # Sort by period so first/last row calculations are correct.
    sorted_province_data = province_data.sort_values("period")

    # Render selectboxes for periods 
    available_periods = prepare_periods(sorted_province_data=sorted_province_data)

    first_period, last_period = render_select_periods(periods=available_periods)

    selected_range_data = sorted_province_data [
        (sorted_province_data["period"] >= first_period) & (sorted_province_data["period"] <= last_period) 
    ]

    chart_data = selected_range_data[["period", "value"]]

    # Calculate the KPI values from the ordered rows.
    latest_value, variation, percentage_variation = calculate_kpis(selected_range_data)

    # Show the headline metric cards near the top.
    render_kpis(latest_value, variation, percentage_variation)

    # Render the chart and the raw support table.
    render_chart(chart_data, selected_province, first_period, last_period)
