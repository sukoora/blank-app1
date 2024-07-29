import streamlit as st
from dataclasses import dataclass

@dataclass
class Option:
    name: str
    is_selected: bool = False

# Sample data
options = [Option(name=f"Option {i}") for i in range(1, 6)]

def main():
    st.title("Dynamic List with Checkboxes")

    # Dynamic checkboxes without keys
    for option in options:
        option.is_selected = st.checkbox(option.name, value=option.is_selected)

    # Button to display selected options
    if st.button("Show Selected Options"):
        selected_options = [option.name for option in options if option.is_selected]
        st.write("Selected Options:", selected_options)

if __name__ == "__main__":
    main()