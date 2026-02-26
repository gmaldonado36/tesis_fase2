import streamlit as st

def init_state():
    defaults = {
        "fase": "bienvenida",
        "nombre": "",
        
        # Fase 1 - Reconocimiento
        "imagenes_fase1": [],
        "index_fase1": 0,
        "respuestas_fase1": [],
        
        # Fase 2 - Reconocimiento
        "imagenes_fase2": [],
        "index_fase2": 0,
        "respuestas_fase2": [],
    }
    
    for key, value in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = value
