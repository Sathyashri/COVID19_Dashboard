import streamlit as st
import pandas as pd
import plotly.express as px

# --- Page Config ---
st.set_page_config(page_title="COVID-19 Dashboard", layout="wide")

# --- Load Data ---
@st.cache_data
def load_data():
    return pd.read_csv("covid_cleaned.csv")

covid_data = load_data()

# --- Title ---
st.title("🌍 COVID-19 Data Dashboard")
st.markdown("This dashboard provides a visual overview of COVID-19 trends across the world.")

# --- Country Selector ---
countries = covid_data['country'].unique()
selected_country = st.selectbox("Select Country", sorted(countries))

filtered_data = covid_data[covid_data['country'] == selected_country]

# --- Summary Cards ---
st.markdown("### 🧾 Summary Statistics")

total_cases = filtered_data['cumulative_total_cases'].max()
total_deaths = filtered_data['cumulative_total_deaths'].max()
active_cases = filtered_data['active_cases'].max()

col1, col2, col3 = st.columns(3)
col1.metric("🦠 Total Cases", f"{total_cases:,.0f}")
col2.metric("💀 Total Deaths", f"{total_deaths:,.0f}")
col3.metric("🩺 Active Cases", f"{active_cases:,.0f}")

st.markdown("---")

# --- Line Chart: Cases Over Time ---
st.markdown("### 📈 COVID-19 Cases Over Time")
fig_cases = px.line(
    filtered_data,
    x="date",
    y="cumulative_total_cases",
    title=f"Total Cases in {selected_country}",
    labels={"date": "Date", "cumulative_total_cases": "Total Cases"}
)
st.plotly_chart(fig_cases, use_container_width=True)

# --- Line Chart: Deaths Over Time ---
st.markdown("### ⚰️ COVID-19 Deaths Over Time")
fig_deaths = px.line(
    filtered_data,
    x="date",
    y="cumulative_total_deaths",
    title=f"Total Deaths in {selected_country}",
    labels={"date": "Date", "cumulative_total_deaths": "Total Deaths"},
    color_discrete_sequence=["red"]
)
st.plotly_chart(fig_deaths, use_container_width=True)

# --- Bar Chart: Active Cases by Country (Latest Date) ---
st.markdown("### 📊 Active Cases by Country (Latest Date)")
latest_date = covid_data['date'].max()
latest_data = covid_data[covid_data['date'] == latest_date]

fig_active = px.bar(
    latest_data.sort_values('active_cases', ascending=False).head(10),
    x='country',
    y='active_cases',
    title=f"Top 10 Countries by Active Cases ({latest_date})",
    labels={'active_cases': 'Active Cases', 'country': 'Country'},
    color='active_cases',
    color_continuous_scale='Blues'
)
st.plotly_chart(fig_active, use_container_width=True)

# --- Footer ---
st.markdown("---")
st.markdown("📊 **Dashboard** | Built with Streamlit & Plotly")
