import streamlit as st
import plotly.express as px
import pandas as pd
from utils import load_data, get_summary_table, top_regions

# --- Load Data ---
data_dict = load_data()

# --- Sidebar ---
st.set_page_config(page_title="Solar Data Dashboard", layout="wide")
st.sidebar.title("☀️ Solar Dashboard")
country = st.sidebar.selectbox("Select Country", options=list(data_dict.keys()), format_func=str.capitalize)

df = data_dict[country]

# --- Main Title ---
st.title(f"🌍 Solar Energy Analysis — {country.capitalize()}")

# --- Summary Metrics ---
with st.expander("📊 Summary Statistics", expanded=True):
    summary_df = get_summary_table(df)
    st.dataframe(summary_df.style.format("{:.2f}"), use_container_width=True)

# --- Layout: Two columns ---
col1, col2 = st.columns(2)

with col1:
    st.subheader("☀️ GHI Distribution")
    fig = px.histogram(df, x="GHI", nbins=30, color_discrete_sequence=["#FECB52"])
    st.plotly_chart(fig, use_container_width=True)

with col2:
    st.subheader("💨 DNI Distribution")
    fig = px.histogram(df, x="DNI", nbins=30, color_discrete_sequence=["#A1C6EA"])
    st.plotly_chart(fig, use_container_width=True)

# --- Scatter Plot ---
st.subheader("📈 Scatter Plot: RH vs GHI")
fig = px.scatter(df, x="RH", y="GHI", size="BP", color="Tamb",
                 labels={"RH": "Relative Humidity", "GHI": "Global Horizontal Irradiance"},
                 hover_data=["Tamb", "BP"],
                 color_continuous_scale="Viridis")
st.plotly_chart(fig, use_container_width=True)

# --- Correlation Heatmap (Optional: Pandas only for now) ---
with st.expander("📉 Correlation Matrix"):
    corr = df[["GHI", "DNI", "DHI", "RH", "Tamb", "BP"]].corr()
    st.dataframe(corr.style.background_gradient(cmap="coolwarm").format("{:.2f}"))

# --- Top Regions Table ---
st.subheader("🏆 Top Regions by GHI")
top = top_regions(df, metric="GHI", n=5)
if not top.empty:
    st.table(top)
else:
    st.info("No region data available.")

# --- Footer ---
st.markdown("---")
st.markdown("Made by Hailemariyam using [Streamlit](https://streamlit.io)")
