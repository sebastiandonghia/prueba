import google.generativeai as genai
import os
import streamlit as st

# Usamos st.secrets para obtener la clave de forma segura, igual que en tu app principal
try:
    api_key = st.secrets["GOOGLE_API_KEY"]
    genai.configure(api_key=api_key)

    st.title("Modelos de IA Disponibles")
    st.write("Estos son los modelos a los que tienes acceso y que soportan el método 'generateContent':")

    found_models = False
    for m in genai.list_models():
        if 'generateContent' in m.supported_generation_methods:
            st.success(f"**{m.name}**")
            st.json({
                "Descripción": m.description,
                "Métodos Soportados": m.supported_generation_methods
            })
            found_models = True
    
    if not found_models:
        st.warning("No se encontró ningún modelo que soporte 'generateContent'.")

except KeyError:
    st.error("¡Error Crítico! No se encontró la 'GOOGLE_API_KEY' en los secrets de Streamlit (secrets.toml).")
    st.info("Asegúrate de que tu archivo .streamlit/secrets.toml contiene la línea: GOOGLE_API_KEY = 'tu-api-key'")
except Exception as e:
    st.error(f"Ocurrió un error inesperado al intentar contactar la API de Google:")
    st.exception(e)
