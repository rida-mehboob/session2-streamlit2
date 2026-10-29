import numpy as np
import pandas as pd
import streamlit as st

st.set_page_config(page_title="DataFrame Demo", page_icon="📊", layout="wide")
st.title("📊 DataFrame Demo")
st.write("Filter a small illustrative dataset and display a dataframe and comparison chart.")
regions = ["Australia", "Brazil", "China", "India", "United States"]
years = list(range(2015, 2025))
rng = np.random.default_rng(101)
rows = []
for i, region in enumerate(regions):
    baseline = 8 + 5 * i
    for year in years:
        rows.append({"Region": region, "Year": year,
                     "Production index": max(0, baseline + (year - 2015) * (i + 1) * 0.7
                                             + rng.normal(0, 1.2))})
data = pd.DataFrame(rows)
selected = st.multiselect("Choose regions", regions, default=["Australia", "China"])
if not selected:
    st.warning("Select at least one region.")
    st.stop()
filtered = data[data["Region"].isin(selected)]
pivot = filtered.pivot(index="Year", columns="Region", values="Production index")
st.line_chart(pivot)
st.subheader("Filtered data")
st.dataframe(filtered, use_container_width=True)
st.caption("Illustrative synthetic data, not an official UN statistical series.")
