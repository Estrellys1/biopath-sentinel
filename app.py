import streamlit as st

# Configuración de la página
st.set_page_config(page_title="BioPath-Sentinel AI", page_icon="", layout="wide")

# --- BARRA LATERAL (NAVEGACIÓN) ---
st.sidebar.title(" Panel de Investigación")
opcion = st.sidebar.radio(
    "Seleccione una línea de estudio:",
    ["Inicio", "Oncología Genómica", "Dengue & Influenza", "Seguridad Hídrica (Norovirus)", "Simulación Molecular"]
)

# --- PÁGINA: INICIO ---
if opcion == "Inicio":
    st.title(" BioPath-Sentinel AI")
    st.subheader("Inteligencia Artificial para la Seguridad Biológica Global")
    st.markdown("""
    Plataforma diseñada para la protección de **infraestructuras críticas**. 
    Utilizamos **modelado** avanzado y **bioinformática** para reducir ciclos de detección de 48h a 6h.
    """)
    st.info("Seleccione una investigación en el menú de la izquierda para ver los detalles técnicos.")

# --- PÁGINA: ONCOLOGÍA GENÓMICA ---
elif opcion == "Oncología Genómica":
    st.title(" Investigación: Cáncer de Mama")
    st.write("Análisis de biomarcadores y medicina de precisión.")
    # Aquí puedes pegar tu texto de can_ma.txt o escribir directamente
    try:
        with open("can_ma.txt", "r", encoding="utf-8") as f:
            st.markdown(f.read())
    except:
        st.write("Cargando datos de investigación genómica...")

# --- PÁGINA: DENGUE & INFLUENZA ---
elif opcion == "Dengue & Influenza":
    st.title(" Vigilancia Epidemiológica")
    st.write("Modelado estructural de patógenos virales.")
    st.markdown("""
    Análisis realizado mediante **AlphaFold2** para predecir la interacción de proteínas en variantes de Dengue e Influenza.
    """)

# --- PÁGINA: SEGURIDAD HÍDRICA ---
elif opcion == "Seguridad Hídrica (Norovirus)":
    st.title(" Monitoreo de Norovirus")
    st.write("Protección de plantas de desalinización y agua potable mediante vigilancia genómica constante.")

# --- PÁGINA: SIMULACIÓN MOLECULAR ---
elif opcion == "Simulación Molecular":
    st.title(" Dinámica Molecular y Bioinformática")
    st.markdown("""
    Esta sección requiere el uso de **GPU (CUDA)** para ejecutar simulaciones en **GROMACS**. 
    Actualmente solicitando recursos institucionales para escalar el procesamiento de datos complejos.
    """)

# --- PROPUESTA DE VALOR GENERAL (SIN IMÁGENES) ---
st.markdown("""
###  Bioinformática y Vigilancia Genómica de Alto Rendimiento
BioPath-Sentinel AI integra **simulación molecular** y **modelado predictivo** para la protección de infraestructuras críticas y salud pública. 
Mediante el uso de computación acelerada por GPU, transformamos el análisis bioinformático tradicional en una respuesta digital inmediata.

* **Modelado Estructural:** Predicción de estructuras 3D de alta fidelidad mediante **AlphaFold2**, permitiendo visualizar la arquitectura de proteínas virales y biomarcadores oncológicos.
* **Simulación Molecular:** Análisis de dinámica molecular (MD) con **GROMACS** para estudiar la interacción física entre patógenos y receptores celulares, optimizado para **GPU (CUDA)**.
* **IA y Aprendizaje Automático:** Implementación de redes neuronales convolucionales (CNN) y recurrentes (RNN) para el reconocimiento de patrones genómicos, clasificación de variantes y predicción de resistencia a fármacos.
* **Bioinformática Escalable:** Optimización de pipelines de datos masivos para reducir el ciclo de procesamiento genómico de 48h a solo **6h**.
""")

st.info("Ecosistema diseñado para la soberanía tecnológica en investigación genómica.")

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

















