import streamlit as st
from pages import bienvenida, instrucciones, fase1, descanso, fase2, gracias
from services.state_manager import init_state

st.set_page_config(
    page_title="Estudio de Reconocimiento",
    layout="centered"
)

init_state()

fase = st.session_state.fase

if fase == "bienvenida":
    bienvenida.run()
elif fase == "instrucciones":
    instrucciones.run()
elif fase == "prueba":  # Cambié "prueba" por consistencia con instrucciones.py
    fase1.run()
elif fase == "descanso":
    descanso.run()
elif fase == "fase2":
    fase2.run()
elif fase == "gracias":
    gracias.run()

