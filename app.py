import streamlit as st

# Configuración de la página
st.set_page_config(page_title="BioPath-Sentinel AI | Global Genomic Surveillance", page_icon="nn", layout="wide")

# --- CABECERA ---
st.title(" BioPath-Sentinel AI")
st.subheader("Inteligencia Artificial para la Seguridad Biológica Global")

# --- PROPUESTA DE VALOR GENERAL ---
col1, col2 = st.columns([2, 1])
with col1:
    st.markdown("""
    ### Vigilancia Genómica en Tiempo Real
    BioPath-Sentinel AI es una plataforma diseñada para la protección de **infraestructuras críticas y salud pública**. 
    Mediante el uso de computación de alto rendimiento (GPU) y modelos de **Deep Learning**, transformamos el monitoreo biológico lento en una defensa digital instantánea.
    
    * **Universalidad:** Capacidad de procesar patógenos hídricos, transmitidos por vectores y respiratorios.
    * **Velocidad:** Reducción del ciclo de detección de 48h a solo **6h**.
    * **Escalabilidad:** Implementable en cualquier entorno que requiera seguridad sanitaria de alto nivel.
    """)
with col2:
    with col2:
    # Usar la URL RAW de GitHub asegura que la imagen siempre cargue
    st.image("https://raw.githubusercontent.com/Estrellys1/biopath-sentinel/main/virus1.png", 
             caption="Modelado Bioinformático Multi-Patógeno")

st.divider()

# --- SEGMENTOS DE IMPACTO (Aquí generalizamos) ---
st.header(" Áreas de Aplicación")
c1, c2, c3 = st.columns(3)

with c1:
    st.markdown("####  Seguridad Hídrica")
    st.write("Sistemas de monitoreo para plantas de desalinización y tratamiento de agua potable, garantizando la detección inmediata de **Norovirus** y otros contaminantes biológicos.")

with c2:
    st.markdown("####  Vigilancia Epidemiológica")
    st.write("Detección y seguimiento de variantes de **Dengue** y virus hemorrágicos para la prevención de brotes en regiones tropicales y subtropicales.")

with c3:
    st.markdown("####  Salud Pública Global")
    # AGREGAMOS TU IMAGEN AQUÍ
    st.image("influenz_2.png", caption="Modelado de Virus Influenza") 
    st.write("Análisis de patógenos respiratorios como **Influenza**, permitiendo tomar decisiones basadas en datos genómicos precisos.")

st.divider()

# --- TECNOLOGÍA (Lo que le interesa a Google) ---
st.header(" Nuestro Stack Tecnológico")
st.write("Apalancamos la potencia de la nube para democratizar la bioinformática avanzada:")
st.code("""
- Protein Folding: AlphaFold2
- Deep Learning: TensorFlow / Keras (CNN & RNN)
- Molecular Dynamics: GROMACS
- Infrastructure: GPU Accelerated Computing
""", language="text")

st.success("BioPath-Sentinel AI: Protegiendo el futuro a través del código genético.")

# --- CONTACTO ---
st.sidebar.title("Contacto Corporativo")
st.sidebar.write("**📧 Email:** ")
st.sidebar.info("Solicitando vinculación al programa Google Cloud for Startups")

st.sidebar.divider()

# --- NUEVA SECCIÓN: CÁNCER DE MAMA ---
st.sidebar.title("Investigación Genómica")

# Esta función lee el archivo que subiste a GitHub
def leer_archivo_cancer():
    try:
        with open("can_ma.txt", "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        return "El archivo de investigación can_ma.txt no se encontró en el repositorio."

# Crear el botón desplegable en la barra lateral
with st.sidebar.expander("Ver Proyecto: Cáncer de Mama"):
    contenido = leer_archivo_cancer()
    st.write(contenido)








