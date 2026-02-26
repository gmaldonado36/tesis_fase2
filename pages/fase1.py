import streamlit as st
from services.image_loader import load_random_images
import os
from PIL import Image
from config import FASE1_FOLDER

def run():
    st.title("Fase 1 - Reconocimiento de Imágenes")
    
    # Inicializar imágenes si no existen
    if not st.session_state.imagenes_fase1:
        st.session_state.imagenes_fase1 = load_random_images(FASE1_FOLDER)
        st.session_state.index_fase1 = 0
        st.session_state.respuestas_fase1 = []
    
    # Verificar si terminamos
    if st.session_state.index_fase1 >= len(st.session_state.imagenes_fase1):
        st.session_state.fase = "descanso"
        st.rerun()
        return
    
    idx = st.session_state.index_fase1
    img_name = st.session_state.imagenes_fase1[idx]
    img_path = os.path.join(FASE1_FOLDER, img_name)
    
    total = len(st.session_state.imagenes_fase1)
    st.progress((idx) / total, text=f"Imagen {idx + 1} de {total}")
    
    # Mostrar imagen
    img = Image.open(img_path)
    img.thumbnail((900, 900))
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.image(img, use_container_width=True)
    
    st.markdown("### ¿Usted ya ha visto esta imagen?")
    
    col_yes, col_no = st.columns(2)
    
    with col_yes:
        if st.button("Sí", key="btn_si_fase1", use_container_width=True):
            guardar_respuesta(img_name, "Si")
    
    with col_no:
        if st.button("No", key="btn_no_fase1", use_container_width=True):
            guardar_respuesta(img_name, "No")

def guardar_respuesta(img_name, respuesta):
    st.session_state.respuestas_fase1.append({
        "imagen": img_name,
        "respuesta": respuesta
    })
    st.session_state.index_fase1 += 1
    st.rerun()
