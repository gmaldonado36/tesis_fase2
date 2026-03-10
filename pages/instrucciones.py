import streamlit as st

def run():
    st.title("Información General")

    st.write("Bienvenido(a) a la prueba.")
    st.write("Esta prueba consta de **2 fases**.")
    st.write("Al **finalizar** cada fase, podrás tomar un breve **descanso** si lo deseas.")
    st.write("En cada fase verás una serie de **imágenes** que puede que hayas visto en la prueba anterior o que no.")
    st.write("Tu misión es identificar correctamente **cuáles imágenes ya viste y cuáles no**.")
    st.write("Cuando estés listo(a) para continuar, podrás iniciar la siguiente fase haciendo clic en el botón correspondiente.")

    if st.button("Avanzar", type="primary"):
        st.session_state.fase = "prueba"
        st.rerun()