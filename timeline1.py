import streamlit as st
import streamlit.components.v1 as components

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

# Convert items to JSON format
import json
items_json = json.dumps(items)

# HTML and JavaScript to render the timeline
html_code = f"""
<!DOCTYPE html>
<html>
<head>
    <script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/vis/4.21.0/vis.min.js"></script>
    <link href="https://cdnjs.cloudflare.com/ajax/libs/vis/4.21.0/vis.min.css" rel="stylesheet" type="text/css" />
</head>
<body>
    <div id="visualization"></div>
    <script type="text/javascript">
        var container = document.getElementById('visualization');
        var items = new vis.DataSet({items_json});
        var options = {{
            editable: false
        }};
        var timeline = new vis.Timeline(container, items, options);
    </script>
</body>
</html>
"""

# Render the HTML and JavaScript
components.html(html_code, height=400)
