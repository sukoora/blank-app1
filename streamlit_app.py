import streamlit as st

st.title("🎈 My new app")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)

placeholder = st.empty()

# Replace the placeholder with some text:
placeholder.text("Hello")

# Replace the text with a chart:
placeholder.line_chart({"data": [1, 5, 2, 6]})

# Replace the chart with several elements:
with placeholder.container():
    st.write("This is one element")
    st.write("This is another")

# Clear all those elements:
placeholder.empty()

import time

ph = st.empty()
for x in range(5):
    ph.button(f"Refresh", key=f'refresh_{x}')
    time.sleep(1)
st.write("✔️ 1 minute over!")