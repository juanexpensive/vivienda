import pandas as pd


def get_province_data(housing_data: pd.DataFrame, selected_province: str) -> pd.DataFrame:
    province_data = housing_data[housing_data["province"] == selected_province]
    return province_data.sort_values("period")


def prepare_periods(sorted_province_data: pd.DataFrame):
    return sorted_province_data["period"].unique()


def normalize_period_range(first_period, last_period):
    if first_period <= last_period:
        return first_period, last_period, False

    return last_period, first_period, True


def filter_period_range(
    sorted_province_data: pd.DataFrame,
    first_period,
    last_period,
) -> pd.DataFrame:
    return sorted_province_data[
        (sorted_province_data["period"] >= first_period)
        & (sorted_province_data["period"] <= last_period)
    ]


def calculate_kpis(selected_range_data: pd.DataFrame):
    latest_row = selected_range_data.iloc[-1]
    first_row = selected_range_data.iloc[0]

    latest_value = latest_row["value"]
    first_value = first_row["value"]
    variation = latest_value - first_value

    if first_value != 0:
        percentage_variation = (variation / first_value) * 100
    else:
        percentage_variation = 0

    return latest_value, variation, percentage_variation
