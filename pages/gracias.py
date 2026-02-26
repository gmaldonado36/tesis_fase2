import streamlit as st

def run():
    st.title("🙏 ¡Gracias por participar!")
    
    st.balloons()
    
    st.write("---")
    
    nombre = st.session_state.get("nombre", "Participante")
    
    st.markdown(f"""
    ### ¡Felicidades, **{nombre}**!
    
    Has completado exitosamente todas las fases del estudio.
    
    Tu participación es muy valiosa para nuestra investigación.
    """)
    
    st.write("---")
    
    # Resumen final
    col1, col2 = st.columns(2)
    
    with col1:
        total_fase1 = len(st.session_state.respuestas_fase1)
        st.metric("Imágenes Fase 1", total_fase1)
    
    with col2:
        total_fase2 = len(st.session_state.respuestas_fase2)
        st.metric("Imágenes Fase 2", total_fase2)
    
    st.write("---")
    st.success("Puedes cerrar esta ventana.")
    
    # Opcional: botón para reiniciar (útil para pruebas)
    if st.button("Reiniciar prueba (solo para testing)"):
        for key in list(st.session_state.keys()):
            del st.session_state[key]
        st.rerun()

