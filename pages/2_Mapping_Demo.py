import numpy as np
import pandas as pd
import streamlit as st

st.set_page_config(page_title="Mapping Demo", page_icon="🌍", layout="wide")
st.title("🌍 Mapping Demo")
st.write("Explore simulated sample points around San Francisco using an interactive map.")
count = st.sidebar.slider("Number of map points", 20, 500, 150, 10)
spread = st.sidebar.slider("Point spread (degrees)", 0.005, 0.08, 0.025, 0.005)
seed = st.sidebar.number_input("Random seed", min_value=0, max_value=9999, value=25)
rng = np.random.default_rng(seed)
points = pd.DataFrame({"lat": 37.7749 + rng.normal(0, spread, count),
                       "lon": -122.4194 + rng.normal(0, spread, count)})
st.map(points, zoom=10)
st.caption("Locations are simulated for demonstration; they are not real observations.")
if st.checkbox("Show sample coordinates"):
    st.dataframe(points.head(30), use_container_width=True)
