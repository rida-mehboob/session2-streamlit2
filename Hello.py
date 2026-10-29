import streamlit as st

st.set_page_config(page_title="Hello | Multipage Streamlit", page_icon="👋", layout="wide")
st.title("Welcome to Streamlit! 👋")
st.sidebar.success("Select a demo page above.")
st.write("This is a multipage Streamlit app built for Session 2 · Part E.")
st.markdown("""
Use the sidebar to explore three interactive pages:

- **Plotting Demo:** generate and explore an animated random walk.
- **Mapping Demo:** view and filter sample locations around San Francisco.
- **DataFrame Demo:** filter and chart a sample agricultural-production dataset.

Each page is a separate Python script in the `pages/` folder, and Streamlit builds the sidebar navigation automatically.
""")
st.info("All demo data is bundled/generated in Python, so no internet download or SSL certificate is required.")
