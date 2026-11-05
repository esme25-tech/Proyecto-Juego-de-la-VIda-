import streamlit as st
import time
from logica import crear_tablero_aleatorio, siguiente_generacion
from interfaz import mostrar_encabezado, renderizar_tablero, mostrar_controles

# 1. Mostrar la cabecera (Desde interfaz.py)
mostrar_encabezado()

VELOCIDAD = 0.60

# 2. Memoria del juego (Session State)
if "grid" not in st.session_state:
    st.session_state.grid = crear_tablero_aleatorio()
if "corriendo" not in st.session_state:
    st.session_state.corriendo = False

# 3. Mostrar controles y capturar la acción (Desde interfaz.py)
accion = mostrar_controles()

# 4. Lógica de los botones
if accion == "iniciar":
    st.session_state.corriendo = True
    st.rerun()
elif accion == "pausar":
    st.session_state.corriendo = False
    st.rerun()
elif accion == "reiniciar":
    st.session_state.grid = crear_tablero_aleatorio()
    st.session_state.corriendo = False
    st.rerun()

# 5. Dibujo y animación
tablero_placeholder = st.empty()

if not st.session_state.corriendo:
    tablero_placeholder.markdown(renderizar_tablero(st.session_state.grid), unsafe_allow_html=True)
else:
    for _ in range(100):
        tablero_placeholder.markdown(renderizar_tablero(st.session_state.grid), unsafe_allow_html=True)
        st.session_state.grid = siguiente_generacion(st.session_state.grid)
        time.sleep(VELOCIDAD)
    st.rerun()  
