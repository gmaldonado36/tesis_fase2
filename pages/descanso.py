import streamlit as st

def run():
    st.title("🎉 ¡Fase 1 Completada!")
    
    st.write("---")
    
    st.markdown("""
    ### Has completado la primera fase del estudio.
    
    Tómate unos minutos para descansar si lo necesitas.
    
    Cuando estés **listo(a)**, haz clic en el botón para continuar con la **Fase 2**.
    """)
    
    st.write("---")
    
    # Mostrar resumen de fase 1 (opcional)
    total_fase1 = len(st.session_state.respuestas_fase1)
    st.info(f"📊 Respondiste {total_fase1} imágenes en la Fase 1")
    
    st.write("")
    st.write("")
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("Continuar a Fase 2", type="primary", use_container_width=True):
            st.session_state.fase = "fase2"
            st.rerun()
