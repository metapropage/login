import streamlit as st
import streamlit.components.v1 as components

components.html(
    """
    <h1>Streamlit Example</h1>
    <p>This is an example of embedding HTML in Streamlit.</p>
    <a href="https://streamlit.io" target="_blank">Visit Streamlit</a>
    """,
    height=300,
)
