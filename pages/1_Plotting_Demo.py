import numpy as np
import pandas as pd
import streamlit as st

st.set_page_config(page_title="Plotting Demo", page_icon="📈", layout="wide")
st.title("📈 Plotting Demo")
st.write("Explore a synthetic random walk and compare several series.")
steps = st.sidebar.slider("Number of steps", 50, 500, 150, 50)
series_count = st.sidebar.slider("Number of series", 1, 5, 3)
seed = st.sidebar.number_input("Random seed", min_value=0, max_value=9999, value=42)
rng = np.random.default_rng(seed)
data = pd.DataFrame(np.cumsum(rng.normal(size=(steps, series_count)), axis=0),
                    columns=[f"Series {i+1}" for i in range(series_count)])
st.line_chart(data)
st.caption("Synthetic data generated in Python; change the sidebar controls to update the chart.")
if st.checkbox("Show underlying data"):
    st.dataframe(data, use_container_width=True)
