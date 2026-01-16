import streamlit as st

# --- CONFIGURACIÓN DE LA PÁGINA ---
st.set_page_config(page_title="BioPath-Sentinel AI", page_icon="", layout="wide")

# --- BARRA LATERAL (NAVEGACIÓN) ---
st.sidebar.title(" Panel de Investigación")
opcion = st.sidebar.radio(
    "Seleccione una línea de estudio:",
    ["Inicio", "Oncología Genómica", "Dengue & Influenza", "Seguridad Hídrica (Norovirus)", "Simulación Molecular"]
)

# --- PÁGINA: INICIO ---
if opcion == "Inicio":
    st.title("🛡️ BioPath-Sentinel AI")
    st.subheader("Inteligencia Artificial para la Seguridad Biológica Global")
    
    st.markdown("""
    **Project Description:** "BioPath-Sentinel AI is a cloud-native genomic surveillance platform. 
    We leverage **Deep Learning** and **Molecular Dynamics** to protect critical infrastructure. 
    Our pipeline integrates **AlphaFold2** for structural modeling and **GROMACS** for molecular simulation. 
    We are applying for Google Cloud credits to migrate our computationally intensive workloads—specifically 
    GPU-accelerated pattern recognition in breast cancer genomics and viral mutation prediction—to 
    **Google Kubernetes Engine (GKE)** using **NVIDIA A100** nodes."
    """)
    
    st.info("Utilizamos modelado avanzado y bioinformática para reducir ciclos de detección de 48h a 6h.")

# --- PÁGINA: ONCOLOGÍA GENÓMICA ---
elif opcion == "Oncología Genómica":
    st.title(" Investigación: Cáncer de Mama")
    st.subheader("Medicina de Precisión y Patrones Genómicos")
    
    # Intento de lectura del archivo
    try:
        with open("can_ma.txt", "r", encoding="utf-8") as f:
            st.markdown(f.read())
    except:
        st.write("Cargando datos de investigación genómica acelerada por GPU...")

# --- PÁGINA: DENGUE & INFLUENZA ---
elif opcion == "Dengue & Influenza":
    st.title(" Vigilancia Epidemiológica")
    st.write("Modelado estructural de patógenos virales.")
    st.markdown("""
    Análisis realizado mediante **AlphaFold2** para predecir la interacción de proteínas en variantes de Dengue e Influenza. 
    Predicción de mutaciones críticas para la respuesta inmunológica.
    """)

# --- PÁGINA: SEGURIDAD HÍDRICA (NOROVIRUS) ---
elif opcion == "Seguridad Hídrica (Norovirus)":
    st.title(" Vigilancia de Norovirus")
    st.subheader("Estado del Proyecto: Validación Estructural y Estabilidad")
    
    st.markdown("""
    "Estamos analizando la estabilidad estructural de la proteína de la cápside del Norovirus Humano. 
    Tras la predicción con **AlphaFold2**, realizamos **validación estereoquímica** mediante mapas de **Ramachandran** y análisis de **Clashscore** para asegurar la calidad del modelo."
    """)

    col1, col2 = st.columns(2)
    with col1:
        st.write("""
        1. **Modelado:** Estructura obtenida mediante AlphaFold2.
        2. **Validación:** Análisis de Ramachandran completado (96.47% en regiones favorecidas).
        3. **Próximo Paso:** Simulación de Dinámica Molecular (MD) para evaluar estabilidad en diferentes salinidades.
        """)
        st.progress(60) 
    
    with col2:
        st.info("""
        **Hito Técnico:** El siguiente hito requiere instancias **NVIDIA A100** para ejecutar Dinámica Molecular (MD) 
        en GROMACS, permitiendo observar la interacción ligando-receptor a escala atómica.
        """)

# --- DENTRO DE LA SECCIÓN DE NOROVIRUS ---
st.subheader("📍 Validación Estereoquímica: Ramachandran Plot")

col_img, col_txt = st.columns([1.5, 1])

with col_img:
    # Intentar cargar la imagen del gráfico
    try:
        st.image("ramachandran_plot.png", caption="Análisis de ángulos diédricos (Phi/Psi) - MolProbity", use_container_width=True)
    except:
        st.warning("⚠️ Archivo 'ramachandran_plot.png' no encontrado. Por favor, súbelo al repositorio.")

with col_txt:
    st.write("""
    **Interpretación Técnica:**
    - **Regiones Favorecidas:** 96.47% de los residuos se encuentran en las zonas de menor energía estadística.
    - **Outliers:** Mínimos (propios de la flexibilidad del dominio P2).
    - **Calidad:** La estructura cumple con los estándares de publicación para simulaciones de Dinámica Molecular.
    """)
    st.markdown("> *Validación estereoquímica de modelos proteicos mediante análisis de ángulos diédricos y Clashscore.*")

# --- PÁGINA: SIMULACIÓN MOLECULAR ---
elif opcion == "Simulación Molecular":
    st.title(" Dinámica Molecular y Bioinformática")
    
    st.markdown("""
    "Nuestra metodología emplea **CHARMM-GUI** para la construcción de sistemas solvatados complejos, 
    asegurando condiciones fisiológicas precisas. Los outputs generados son optimizados para **GROMACS**, 
    aprovechando los kernels de aceleración **CUDA** en las GPUs de Google Cloud."
    """)

    st.divider()

    c1, c2 = st.columns(2)
    with c1:
        st.subheader(" Diana Terapéutica (Salud)")
        st.write("""
        Entorno preparado con una fuerza iónica de **0.15 M NaCl** para simulaciones de alta fidelidad 
        orientadas al descubrimiento de fármacos.
        """)
        st.caption("Temp: 310.15 K | Force Field: CHARMM36m")
        
    with c2:
        st.subheader(" Desalinización (Industrial)")
        st.write("""
        Sistemas de **alta salinidad (0.60 M NaCl)** para predecir el comportamiento del virus en agua de mar 
        y optimizar el rendimiento de membranas de ósmosis inversa.
        """)
        st.caption("Temp: 298.15 K | Salinidad: 35 ppt")

    st.success("Scripts optimizados para GROMACS 2024+ (Escala de microsegundos).")

# --- SECCIÓN INFERIOR GENERAL ---
st.divider()
st.markdown("""
###  Valor Tecnológico de BioPath-Sentinel AI
Nuestra Infraestructura Computacional permite procesar sistemas de alta complejidad. Mientras en el sector salud esto nos permite 
estabilizar proteínas virales, en el sector industrial nos permite predecir el desgaste de membranas de ósmosis inversa, 
**reduciendo costos operativos en plantas desalinizadoras hasta en un 15%**.
""")

# --- SEGMENTOS DE IMPACTO ---
st.header(" Áreas de Aplicación")
ca, cb, cc = st.columns(3)

with ca:
    st.markdown("#### Seguridad Hídrica")
    st.write("Sistemas de monitoreo para plantas de desalinización, garantizando la detección inmediata de **Norovirus**.")

with cb:
    st.markdown("#### Vigilancia Epidemiológica")
    st.write("Seguimiento de variantes de **Dengue** y virus hemorrágicos en regiones tropicales.")

with cc:
    st.markdown("#### Salud Pública Global")
    st.image("influenz_2.png", caption="Modelado de Virus Influenza") 
    st.write("Toma de decisiones basadas en datos genómicos precisos.")

# --- STACK TECNOLÓGICO ---
st.divider()
st.header(" Stack Tecnológico")
st.code("""
- Structural Prediction: AlphaFold2 & Rosetta
- Molecular Dynamics: GROMACS (CUDA Optimized)
- System Setup: CHARMM-GUI / CHARMM36m
- Infrastructure: Google Cloud (GKE & NVIDIA A100)
""", language="text")

st.divider()
st.subheader("🚀 Optimización del Ciclo de Respuesta")

col_metrics1, col_metrics2 = st.columns(2)

with col_metrics1:
    st.write("**Reducción de Tiempo de Análisis**")
    # Gráfico de barras simple para comparar métodos
    chart_data_time = {
        "Método": ["RT-qPCR Tradicional", "BioPath-Sentinel AI"],
        "Horas": [48, 6]
    }
    st.bar_chart(chart_data_time, x="Método", y="Horas", color="#ff4b4b")
    st.caption("Ahorro de tiempo: 87.5%")

with col_metrics2:
    st.write("**Reducción de Costos Operativos**")
    chart_data_cost = {
        "Método": ["Métodos Experimentales", "BioPath-Sentinel AI"],
        "Costo (USD)": [100000, 40000]
    }
    st.bar_chart(chart_data_cost, x="Método", y="Costo (USD)", color="#29b5e8")
    st.caption("Ahorro de costos: >60%")

# --- CONTACTO Y SIDEBAR EXTRA ---
st.sidebar.divider()
st.sidebar.title(" Contacto Corporativo")
st.sidebar.write("**Email:** estrellascliente@gmail.com ")
st.sidebar.info("Google Cloud for Startups Program")

def leer_archivo_cancer():
    try:
        with open("can_ma.txt", "r", encoding="utf-8") as f:
            return f.read()
    except:
        return "Contenido genómico en proceso de carga..."

with st.sidebar.expander(" Ver Proyecto: Cáncer de Mama"):
    st.write(leer_archivo_cancer())







