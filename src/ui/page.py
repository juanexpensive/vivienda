import pandas as pd
import streamlit as st

from src.domain.analytics import (
    calculate_kpis,
    filter_period_range,
    get_province_data,
    calculate_highest_and_lowest_variation,
    normalize_period_range,
    prepare_periods,
    calculate_ranking
)
from src.ui.charts import render_chart
from src.ui.components import render_kpis, render_select_periods


def render_body(housing_data: pd.DataFrame) -> None:
    provinces = housing_data["province"].unique()
    selected_province = st.selectbox("select a province", options=provinces)

    sorted_province_data = get_province_data(housing_data, selected_province)
    available_periods = prepare_periods(sorted_province_data)

    first_period, last_period = render_select_periods(available_periods)
    first_period, last_period, was_swapped = normalize_period_range(
        first_period,
        last_period,
    )

    if was_swapped:
        st.info("Selected period range was reversed, so it has been swapped automatically.")

    selected_range_data = filter_period_range(
        sorted_province_data,
        first_period,
        last_period,
    )
    
    chart_data = selected_range_data[["period", "value"]]
    highest_variation, lowest_variation = calculate_highest_and_lowest_variation(calculate_ranking(housing_data, first_period, last_period))
    latest_value, variation, percentage_variation = calculate_kpis(selected_range_data)
    render_kpis(latest_value, variation, percentage_variation, highest_variation, lowest_variation)
    render_chart(chart_data, selected_province, first_period, last_period)