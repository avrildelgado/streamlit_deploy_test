import streamlit as st

# Initial color
button_color = "blue"

# Create the button
button = st.button("Click Me!", key="my_button")

# Change color on click
if button:
    if button_color == "blue":
        button_color = "red"
    else:
        button_color = "blue"

# Update button style with new color
st.markdown(f"""
<style>
.stButton {{
  background-color: {button_color};
}}
</style>
""", unsafe_allow_html=True)