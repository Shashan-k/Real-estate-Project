import streamlit as st

st.set_page_config(
    page_title="Gurgaon Real Estate Analytics App",
    page_icon="👋",
)

# st.write("# Welcome to Real Estate Solution! ")
# st.image("real-state.png", use_column_width=True)

# st.write("## A one stop solution for all your real estate needs")
# Set page width
# Set page width
st.markdown(
    """
    <style>
        .reportview-container {
            max-width: 1000px;
            padding-top: 2rem;
            padding-right: 2rem;
            padding-left: 2rem;
            padding-bottom: 2rem;
        }
        .sidebar .sidebar-content {
            padding-top: 2rem;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# Title
st.write(
    """
    <div style='text-align: center;'>
        <h1>Welcome to Real Estate Solution!</h1>
    </div>
    """,
    unsafe_allow_html=True,
)

# Display local image
image = "real-state.png"
st.image(image, caption='', use_column_width=True)

# Introduction
st.write(
    """
    <div style='text-align: center;'>
        <h2>A one-stop solution for all your real estate needs</h2>
    </div>
    """,
    unsafe_allow_html=True,
)

#st.sidebar.success("Select a demo above.")