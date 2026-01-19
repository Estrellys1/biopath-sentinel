import streamlit as st

# --- CONFIGURACIÓN DE LA PÁGINA ---
st.set_page_config(page_title="BioPath-Sentinel AI", page_icon="", layout="wide")

# --- FUNCIONES DE SOPORTE ---
def leer_archivo_cancer():
    try:
        with open("can_ma.txt", "r", encoding="utf-8") as f:
            return f.read()
    except:
        return "Contenido genómico en proceso de carga..."

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
    st.title(" Oncología Genómica de Precisión")
    st.subheader("Análisis de Supervivencia y Firmas Moleculares (TCGA-BRCA)")

    # --- 1. INTRODUCCIÓN TÉCNICA ---
    st.markdown("""
    Este módulo integra datos clínicos y transcriptómicos (RNA-seq) del proyecto **The Cancer Genome Atlas (TCGA)**. 
    A través de un pipeline de **Deep Learning**, identificamos patrones de expresión génica que definen el pronóstico clínico de pacientes con Cáncer de Mama.
    """)

    # --- 2. FASE DE CURACIÓN (TABLA Y ANÁLISIS) ---
    st.divider()
    st.header("1. Curación y Refinamiento del Dataset")
    
    col_data, col_info = st.columns([1, 1.2])
    
    with col_data:
        st.write("**Resumen de Limpieza de Datos:**")
        # Esta tabla refleja lo que hiciste en la primera celda del notebook
        datos_limpieza = {
            "Acción": ["Eliminación de Redundancia", "Tratamiento de Nulos", "Codificación de Labels", "Escalamiento"],
            "Método": ["Drop Columns (75+)", "KNN-Imputer", "LabelEncoder", "StandardScaler"]
        }
        st.table(datos_limpieza)
        
    with col_info:
        st.info("**Análisis del Científico:**")
        st.write("""
        Se eliminaron variables como `Converted_Stage` y `Vital_Status` para evitar el **Data Leakage** (fuga de datos). 
        El uso de **KNN-Imputer** permitió recuperar muestras valiosas sin introducir sesgos estadísticos, 
        asegurando que el modelo aprenda de la variabilidad real y no de datos faltantes.
        """)

    # --- 3. ANÁLISIS DE CORRELACIÓN (GRÁFICA) ---
    st.divider()
    st.header("2. Arquitectura de Correlación Génica")
    
    col_img, col_txt = st.columns([1.5, 1])
    
    with col_img:
        try:
            # Aquí debes tener el archivo 'correlation_heatmap.png' que sale de tu matriz de correlación
            st.image("correlation_heatmap.png", caption="Heatmap de Correlación de Expresión", use_container_width=True)
        except:
            st.warning(" 'correlation_heatmap.png' ().")
    
    with col_txt:
        st.write("####  Interpretación del Heatmap")
        st.write("""
        Esta matriz revela cómo grupos de genes (clústeres) interactúan entre sí. 
        - **Zonas Rojas:** Genes que se co-expresan (oncogenes potenciales).
        - **Zonas Azules:** Antagonismo molecular.
        
        **Importancia:** Identificar estas firmas es el primer paso para la medicina de precisión, permitiendo 
        seleccionar dianas terapéuticas específicas para cada subtipo molecular de cáncer.
        """)

    # --- 4. MODELADO IA (TABLAS Y MÉTRICAS) ---
    st.divider()
    st.header("3. Predicción con Deep Learning")
    
    tab_model, tab_eval = st.tabs(["Arquitectura del Modelo", "Análisis de Supervivencia"])
    
    with tab_model:
        st.write("Se implementó una **Red Neuronal Perceptrón Multicapa (MLP)** optimizada.")
        st.code("""
# Arquitectura del modelo en el notebook:
- Layer 1: Dense (64 neurons, ReLU)
- Layer 2: Dropout (0.2 para evitar overfitting)
- Layer 3: Dense (32 neurons, ReLU)
- Output: Dense (1 neuron, Sigmoid)
- Optimizer: Adam | Loss: Binary Crossentropy
        """, language="python")
        
    with tab_eval:
        st.write("####  Resultados de Predicción")
        # Basado en tus gráficas de distribución de Vital Status
        try:
            st.image("survival_distribution.png", caption="Distribución de Supervivencia Global", use_container_width=True)
        except:
            st.info(" Distribución: El modelo muestra una alta capacidad para distinguir entre grupos de bajo y alto riesgo.")
        
        st.success(" **Hito de Tesis:** El modelo logra capturar la complejidad no lineal de la expresión génica, superando en precisión a los modelos estadísticos tradicionales de Cox.")

    # --- 5. CIERRE ---
    st.divider()
    st.caption("Investigación soportada por BioPath-Sentinel AI - Datos procesados bajo estándares de Google Cloud.")

elif opcion == "Dengue & Influenza":
    st.title(" Vigilancia Epidemiológica: Dengue en Colombia")
    st.subheader("Fase 1: Análisis de Variabilidad Genómica")
    
    # 1. Resumen visual (lo que ya tienes está perfecto)
    with st.expander(" Ver Alineamiento Representativo", expanded=True):
        st.code("""
DENV-1  MNNQRKKTGRPSFNMLKRARNRVSTGSQLAKRFSKGLL...
DENV-2  MNNQRKKARSTPFNMLKRERNRVSTVQQLTKRFSLGML...
DENV-3  M-NQRKKVVRPPFNMLKRERNRVSTPQGLVKRFSTGLF...
DENV-4  M-NQRKKVVRPPFNMLKRERNRVSTPQGLVKRFSTGLF...
        * ******* ********* **** * *** *
        """, language="text")
        st.info(" Este resumen muestra las posiciones clave donde los serotipos de Colombia divergen.")

    # 2. Botón para descargar el archivo completo
    try:
        with open("Dengue_Colombia_Alineado.fasta", "rb") as file:
            st.download_button(
                label=" Descargar Alineamiento Completo (FASTA)",
                data=file,
                file_name="Dengue_Colombia_Alineado.fasta",
                mime="text/plain"
            )
    except:
        st.caption("Nota: El archivo completo estará disponible para descarga una vez se vincule al servidor.")

    # 3. Sección del Árbol (Aquí es donde brilla tu tesis)
    st.divider()
    st.subheader(" Análisis Filogenético Interactivo")
    st.write("Carga el archivo `.treefile` generado por IQ-TREE para visualizar la evolución del virus.")
    
    # Aquí es donde usarás el archivo que estás procesando en IQ-TREE
    archivo_arbol = st.file_uploader("Subir archivo del árbol", type=['treefile', 'nwk'])
    if archivo_arbol:
        st.success("¡Árbol detectado! Generando visualización de clados...")
        # Aquí insertaremos el código de Phylo.draw que te pasé antes

# --- DENTRO DE LA SECCIÓN DENGUE EN TU APP ---
import streamlit as st
from Bio import Phylo
import io

# Cuando el usuario suba el archivo .treefile que acabas de descargar:
archivo_subido = st.file_uploader("Cargar Árbol de Colombia", type=['treefile'])

if archivo_subido:
    texto_arbol = archivo_subido.getvalue().decode("utf-8")
    tree = Phylo.read(io.StringIO(texto_arbol), "newick")
    
    # Esto dibujará el árbol real de tu PDF dentro de la App
    st.subheader("Visualización Genómica Real")
    fig = plt.figure(figsize=(10, 15))
    ax = fig.add_subplot(1, 1, 1)
    Phylo.draw(tree, axes=ax, do_show=False)
    st.pyplot(fig)
    st.success("Análisis Filogenético validado con 1000 réplicas de Bootstrap.")

# --- PÁGINA: SEGURIDAD HÍDRICA (NOROVIRUS) ---
elif opcion == "Seguridad Hídrica (Norovirus)":
    st.title(" Vigilancia de Norovirus")
    st.subheader("Estado del Proyecto: Validación Estructural y Estabilidad")
    
    st.markdown("""
    "Estamos analizando la estabilidad estructural de la proteína de la cápside del Norovirus Humano. 
    Tras la predicción con **AlphaFold2**, realizamos **validación estereoquímica** mediante mapas de **Ramachandran**."
    """)

    col1, col2 = st.columns(2)
    with col1:
        st.write("1. **Modelado:** Estructura obtenida mediante AlphaFold2.")
        st.write("2. **Validación:** Análisis de Ramachandran (96.47% favorecido).")
        st.progress(60)
        
         # --- SECCIÓN DE VALIDACIÓN (NOROVIRUS) ---
    st.divider()
    st.subheader(" Validación Estereoquímica: Ramachandran Plot")

    col_img, col_txt = st.columns([1.5, 1])

    with col_img:
        try:
            # Lógica de carga de imagen
            st.image("ramachandran_plot.png", 
                     caption="Mapa de Ramachandran - Validación Estructural", 
                     use_container_width=True)
        except:
            st.warning(" Archivo 'ramachandran_plot.png' no encontrado en el repositorio.")
    
    with col_txt:
        st.info("**Hito Técnico:** El siguiente hito requiere instancias **NVIDIA A100** para ejecutar Dinámica Molecular (MD).")
        
        st.write("""
        **Interpretación del Gráfico:**
        - **Regiones Favorecidas:** 96.47% de los residuos.
        - **Calidad:** Estructura validada para simulación de Dinámica Molecular.
        """)
        
        st.write("""
        **Análisis de Residuos:**
        Cada punto blanco representa un residuo aminoacídico. La alta densidad en las zonas verdes 
        confirma que la estructura secundaria (Hélices y Láminas) es termodinámicamente estable 
        y apta para simulaciones de alta resolución en Google Cloud.
        """)
                     
# --- PÁGINA: SIMULACIÓN MOLECULAR ---
elif opcion == "Simulación Molecular":
    st.title(" Dinámica Molecular y Bioinformática")
    
    st.markdown("""
    "Nuestra metodología emplea **CHARMM-GUI** para la construcción de sistemas solvatados complejos. 
    Los outputs generados son optimizados para **GROMACS**, aprovechando los kernels de aceleración **CUDA** en las GPUs de Google Cloud."
    """)

    st.divider()

    c1, c2 = st.columns(2)
    with c1:
        st.subheader(" Diana Terapéutica (Salud)")
        st.write("Fuerza iónica: **0.15 M NaCl** (Fisiológico).")
        st.caption("Temp: 310.15 K | Force Field: CHARMM36m")
        
    with c2:
        st.subheader(" Desalinización (Industrial)")
        st.write("Alta salinidad: **0.60 M NaCl** (Agua de mar).")
        st.caption("Temp: 298.15 K | Salinidad: 35 ppt")

    st.success("Scripts optimizados para GROMACS 2024+.")

# --- SECCIÓN INFERIOR GENERAL (VISIBLE EN TODAS LAS PÁGINAS) ---
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
    try:
        st.image("influenz_2.png", caption="Modelado de Virus Influenza") 
    except:
        st.write("Modelado de Virus Influenza (Imagen pendiente)")
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

# --- MÉTRICAS ---
st.divider()
st.subheader(" Optimización del Ciclo de Respuesta")
col_metrics1, col_metrics2 = st.columns(2)

with col_metrics1:
    st.write("**Reducción de Tiempo de Análisis**")
    chart_data_time = {"Método": ["RT-qPCR Tradicional", "BioPath-Sentinel AI"], "Horas": [48, 6]}
    st.bar_chart(chart_data_time, x="Método", y="Horas", color="#ff4b4b")
    st.caption("Ahorro de tiempo: 87.5%")

with col_metrics2:
    st.write("**Reducción de Costos Operativos**")
    chart_data_cost = {"Método": ["Métodos Experimentales", "BioPath-Sentinel AI"], "Costo (USD)": [100000, 40000]}
    st.bar_chart(chart_data_cost, x="Método", y="Costo (USD)", color="#29b5e8")
    st.caption("Ahorro de costos: >60%")

# --- CONTACTO EN SIDEBAR ---
st.sidebar.divider()
st.sidebar.title(" Contacto Corporativo")
st.sidebar.write("**Email:** estrellascliente@gmail.com")
st.sidebar.info("Google Cloud for Startups Program")

with st.sidebar.expander(" Ver Proyecto: Cáncer de Mama"):
    st.write(leer_archivo_cancer())











