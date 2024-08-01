import streamlit as st
from streamlit_timeline import st_timeline

st.set_page_config(layout="wide")
st.title("Línea temporal de Libros y Películas de Ciencia Ficción.")
st.subheader("Aguante la Ciencia Ficción.")
st.write("Bienvenidos al desierto de lo real.")

# Películas y libros de Ciencia Ficción
items = [
    {"id": 1, "content": "Metropolis", "start": "1927-01-10", "title": "A dystopian future where society is divided into two classes."},
    {"id": 2, "content": "2001: A Space Odyssey", "start": "1968-04-02", "title": "A journey through space and time exploring human evolution."},
    {"id": 3, "content": "The Matrix", "start": "1999-03-31", "title": "A hacker discovers the world is a simulated reality and joins a rebellion."},
    {"id": 4, "content": "Frankenstein", "start": "1818-01-01", "title": "A classic novel about a scientist and his monstrous creation."},
    {"id": 5, "content": "Solaris", "start": "1961-06-01", "title": "A philosophical science fiction novel by Stanisław Lem."},
    {"id": 6, "content": "Do Androids Dream of Electric Sheep?", "start": "1968-01-01", "title": "The basis for the film 'Blade Runner.'"}
]

# Create the timeline
timeline = st_timeline(items, groups=[], options={"editable": False}, height="400px")

# Display details of the selected movie
st.subheader("Selected Movie")
if timeline:
    selected_movie = next((item for item in items if item["id"] == timeline), None)
    if selected_movie:
        st.write(f"**Title:** {selected_movie['content']}")
        st.write(f"**Release Date:** {selected_movie['start']}")
        st.write(f"**Description:** {selected_movie['title']}")
