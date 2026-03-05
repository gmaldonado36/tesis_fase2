import streamlit as st

def run():
    st.title("Información General")

    st.write("Bienvenidos a la prueba.")
    st.write("Esta prueba consta de **2 fases.**")
    st.write("Al **finalizar** cada fase, podrás tomar un breve **descanso** si lo deseas.")
    st.write("Cuando estés listo(a) para continuar, podrás iniciar la siguiente fase haciendo clic en el botón correspondiente.")

    if st.button("Avanzar", type="primary"):
        st.session_state.fase = "prueba"
        st.rerun()