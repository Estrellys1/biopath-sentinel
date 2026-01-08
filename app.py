import streamlit as st

# Configuración de la página
st.set_page_config(page_title="BioPath-Sentinel AI", page_icon="🧬", layout="wide")

# --- ESTILO PERSONALIZADO ---
st.markdown("""
    <style>
    .main { background-color: #f0f2f6; }
    .title { color: #0E1117; font-family: 'Helvetica'; }
    </style>
    """, unsafe_allow_html=True)

# --- CABECERA ---
st.title("🧬 BioPath-Sentinel AI")
st.subheader("Vigilancia Genómica con IA para la Seguridad Sanitaria y del Agua")

# --- INTRODUCCIÓN ---
col1, col2 = st.columns(2)
with col1:
    st.markdown("""
    ### Nuestra Misión
    Protegemos infraestructuras críticas mediante la detección temprana de patógenos. 
    Utilizamos **AlphaFold2** y **Deep Learning** para reducir los tiempos de respuesta de 48 horas a solo **6 horas**.
    """)
with col2:
    # Aquí puedes poner una imagen de una proteína
    st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/a/a9/AlphaFold_structure_of_a_protein.png/600px-AlphaFold_structure_of_a_protein.png", caption="Modelado Estructural de Proteínas Virales")

st.divider()

# --- PROYECTO SANTA MARTA Y AGUA ---
st.header("🌊 Seguridad Hídrica: El Caso Santa Marta")
col3, col4 = st.columns([2, 1])
with col3:
    st.write("""
    Estamos enfocados en brindar soluciones de monitoreo biológico para plantas de tratamiento de agua potable. 
    Nuestro proyecto piloto se centra en la **planta desalinizadora de Santa Marta**, asegurando que el agua esté libre de **Norovirus Humano** mediante análisis genómico acelerado por GPU.
    """)
with col4:
    # Imagen de agua/mar
    st.image("https://images.unsplash.com/photo-1518020382113-a7e8fc38eac9?ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=60", caption="Tecnología para Desalinización Segura")

st.divider()

# --- MULTI-PATÓGENOS ---
st.header("🦠 Plataforma Multi-Patógeno")
st.write("Nuestra IA no se detiene en el agua. El motor BioPath-Sentinel es capaz de analizar:")
kpi1, kpi2, kpi3 = st.columns(3)
kpi1.metric("Norovirus", "Agua Potable")
kpi2.metric("Dengue", "Salud Regional")
kpi3.metric("Influenza", "Prevención Global")

st.info("Aspiramos a ser el estándar de seguridad biológica para empresas de servicios públicos y entidades gubernamentales.")

# --- CONTACTO ---
st.sidebar.title("Contacto")
st.sidebar.write("**📍 Sede:** Santa Marta, Colombia")
st.sidebar.write("**📧 Email:** teducip@gmail.com")
st.sidebar.write("[Visita mi LinkedIn](https://www.linkedin.com/feed/?trk=guest_homepage-basic_nav-header-signin)")