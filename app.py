import streamlit as st
import matplotlib.pyplot as plt
from Bio import Phylo
import io

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
    [
        "Inicio", 
        "Oncología Genómica", 
        "Dengue & Influenza", 
        "Sentinel Genome (DENV-2 Deep Dive)",
        "Seguridad Hídrica (Norovirus)", 
        "Dinámica Molecular de Péptidos (Amiloides)", # <-- Tu sección favorita
        "Simulación Molecular" # <-- Mantenemos la original
    ]
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
    A través de un pipeline de **Deep Learning**, identificamos patrones de expresión génica que definen el pronóstico clínico.
    """)

    # --- 2. FASE DE CURACIÓN ---
    st.divider()
    st.header("1. Curación y Refinamiento del Dataset")
    
    col_data, col_info = st.columns([1, 1.2])
    
    with col_data:
        st.write("**Resumen de Limpieza de Datos:**")
        datos_limpieza = {
            "Acción": ["Eliminación de Redundancia", "Tratamiento de Nulos", "Codificación de Labels", "Escalamiento"],
            "Método": ["Drop Columns (75+)", "KNN-Imputer", "LabelEncoder", "StandardScaler"]
        }
        st.table(datos_limpieza)
        
    with col_info:
        st.info("**Análisis del Científico:**")
        st.write("""
        Se eliminaron variables redundantes para evitar el **Data Leakage**. 
        El uso de **KNN-Imputer** permitió recuperar muestras valiosas sin introducir sesgos, 
        asegurando que el modelo aprenda de la variabilidad genética real.
        """)

        # --- 3. ANÁLISIS DE CORRELACIÓN ---
    st.divider()
    st.header("2. Arquitectura de Correlación Génica")
    
    col_img, col_txt = st.columns([1.5, 1])
    
    with col_img:
        try:
            # Ahora que ya descargaste el archivo, Streamlit lo mostrará aquí
            st.image("correlation_heatmap.png", caption="Heatmap de Correlación de Expresión", use_container_width=True)
        except:
            st.warning(" El archivo 'correlation_heatmap.png' no se encuentra en la carpeta.")
    
    with col_txt:
        st.write("#### 🌡️ Interpretación del Heatmap")
        st.write("""
        Esta matriz revela cómo grupos de genes interactúan entre sí. 
        - **Zonas Rojas:** Genes que se co-expresan (oncogenes potenciales).
        - **Zonas Azules:** Antagonismo molecular.
        """)

    # --- 4. MODELADO IA ---
    st.divider()
    st.header("3. Predicción con Deep Learning (MLP)")
    
    tab_model, tab_eval = st.tabs([" Arquitectura del Modelo", " Análisis de Resultados"])
    
    with tab_model:
        st.write("Se implementó una **Red Neuronal Perceptrón Multicapa (MLP)**.")
        st.code("""
# Parámetros del modelo (Keras/TensorFlow):
model.add(Dense(64, activation='relu', input_dim=X.shape[1]))
model.add(Dropout(0.2))
model.add(Dense(32, activation='relu'))
model.add(Dense(1, activation='sigmoid'))
        """, language="python")
        
    with tab_eval:
        st.write("####  Resultados de Predicción Vital")
        # Aquí cargará la otra imagen que tienes del notebook
        try:
            st.image("survival_distribution.png", caption="Distribución de Supervivencia Predicha", use_container_width=True)
        except:
            st.info("Sube el archivo 'survival_distribution.png' para visualizar los resultados finales.")
    
        st.success(" **Hito:** El modelo captura la complejidad no lineal de la transcriptómica.")
            
# --- PÁGINA: DENGUE & INFLUENZA ---
elif opcion == "Dengue & Influenza":
    st.title(" Vigilancia Epidemiológica: Dengue en Colombia")
    st.subheader("Fase 1: Análisis de Variabilidad Genómica")
    
    # 1. SECCIÓN MAFFT (Alineamiento)
    with st.expander(" Ver Alineamiento Representativo (MAFFT)", expanded=False):
        st.code("""
DENV-1  MNNQRKKTGRPSFNMLKRARNRVSTGSQLAKRFSKGLL...
DENV-2  MNNQRKKARSTPFNMLKRERNRVSTVQQLTKRFSLGML...
DENV-3  M-NQRKKVVRPPFNMLKRERNRVSTPQGLVKRFSTGLF...
DENV-4  M-NQRKKVVRPPFNMLKRERNRVSTPQGLVKRFSTGLF...
        * ******* ********* **** * *** *
        """, language="text")
        st.info("Este resumen muestra las posiciones clave donde los serotipos de Colombia divergen.")

    # 2. PARTE INFORMATIVA: Vigilancia Genómica Real
    st.divider()
    st.header("1. Resultados de Vigilancia Genómica (IQ-TREE)")
    st.markdown("""
    Análisis filogenético realizado sobre el set de secuencias colombianas. 
    Los resultados identifican a la cepa **ADA60761** como una variante de interés prioritario 
    debido a su posición en el árbol y su divergencia genética.
    """)
    
    col_inf, col_txt = st.columns([1.5, 1])
    
    with col_inf:
        # Aquí se muestra el árbol real que obtuviste
        try:
            st.image("arbol_agresiva.png", caption="Detalle del Árbol Filogenético: ADA60761 y clados relacionados")
        except:
            st.error(" Sube el archivo 'arbol_agresiva.png' para visualizar el árbol real.")

    with col_txt:
        st.success("**Variante Agresiva Identificada:** ADA60761")
        st.write("""
        **Análisis de Datos:** En el árbol adjunto, se observa que la cepa ADA60761 presenta una de las ramas más extensas, 
        lo que indica una acumulación significativa de mutaciones frente a los ancestros.
        
        **Soporte Estadístico:** El valor de **84.9/99** (SH-aLRT/Bootstrap) confirma la robustez de este clado, 
        validando científicamente su clasificación como variante de monitoreo.
        """)

    # 3. FASE 2: ESTRUCTURA PROTEICA (ALPHAFOLD)
    st.divider()
    st.header("2. Fase 2: Estructura 3D de la Variante ADA60761")
    
    col_img, col_desc = st.columns([1.5, 1])
    
    with col_img:
        # Aquí se muestra la proteína que generaste
        try:
            st.image("dengue_agresiva.png", caption="Predicción Estructural mediante IA (AlphaFold2)")
        except:
            st.error(" Sube el archivo 'dengue_agresiva.png' para visualizar la proteína.")

    with col_desc:
        st.markdown("""
        **Interpretación del Modelo 3D:**
        
        A partir de la secuencia genómica de la cepa agresiva, AlphaFold2 ha predicho su conformación:
        
        * 🔵 **Azul (pLDDT > 90):** Máxima confianza en la predicción.
        * 🟡 **Amarillo/Naranja:** Regiones con alta flexibilidad estructural.
        
        Esta estructura permite identificar cómo las mutaciones detectadas en la Fase 1 
        alteran la superficie del virus, facilitando potencialmente su propagación.
        """)

    # 4. TABLA DE COMPARACIÓN FINAL
    st.subheader(" Resumen de Hallazgos: ADA60761")
    data_resumen = {
        "Parámetro": ["Origen", "Tipo de Virus", "Evidencia Genómica", "Análisis Estructural"],
        "Detalle": ["Colombia", "DENV-2 Agresivo", "Rama extendida en IQ-TREE", "Modelo AlphaFold Completo"]
    }
    st.table(data_resumen)
 
    # --- TABLA DE MUTACIONES (NUEVA SECCIÓN REFORMADA) ---
    st.subheader(" Análisis de Deriva Antigénica")
    
    # Datos extraídos de tu comparación en MAFFT entre la ancestral y la agresiva
    data_mutaciones = {
        "Posición (Proteína E)": [126, 160, 390],
        "Cepa Ancestral (1986)": ["Lisina (K)", "Treonina (T)", "Asparagina (N)"],
        "Cepa Agresiva (ADA60761)": ["Arginina (R)", "Serina (S)", "Ácido Aspártico (D)"],
        "Impacto en el Virus": ["Mayor Estabilidad", "Escape Inmune", "Afinidad al Receptor"]
    }
    st.table(data_mutaciones)  
   
    
    # 4. PARTE INTERACTIVA (Carga de archivos para el usuario)
    st.divider()
    st.header("3. Herramienta de Diagnóstico Interactiva")
    st.write("Cargue sus propios datos genómicos (.treefile o .nwk) para compararlos.")
    
    archivo_usuario = st.file_uploader("Subir archivo de árbol filogenético", type=['treefile', 'nwk'])
    
    if archivo_usuario:
        try:
            contenido = archivo_usuario.getvalue().decode("utf-8")
            tree_user = Phylo.read(io.StringIO(contenido), "newick")
            st.subheader("Visualización Personalizada")
            fig_user = plt.figure(figsize=(10, 8))
            ax_user = fig_user.add_subplot(1, 1, 1)
            Phylo.draw(tree_user, axes=ax_user, do_show=False)
            st.pyplot(fig_user)
            st.balloons() 
        except Exception as e:
            st.error(f"Error al procesar el archivo: {e}") 
            
    # --- PÁGINA: SENTINEL GENOME (ANÁLISIS AVANZADO DEL PDF) ---
elif opcion == "Sentinel Genome (DENV-2 Deep Dive)":
    st.title(" Sentinel Genome: Evolutionary Intelligence")
    st.subheader("Módulo de Inteligencia Genómica Avanzada - Brote Colombia 2024-2025")

    st.markdown("""
    Este módulo especializado representa el **Deep Dive** científico de BioPath-Sentinel. 
    A diferencia del monitoreo general, aquí procesamos **215 genomas completos** del brote actual en Colombia 
    para identificar la deriva evolutiva del virus en tiempo real.
    """)

    # --- 1. FILOGENIA DE ALTA RESOLUCIÓN ---
    st.divider()
    st.header("1. Reconstrucción Filogenética (IQ-TREE 2)")
    
    col_tree, col_txt_tree = st.columns([1.6, 1])
    
    with col_tree:
        try:
            st.image("arbol_filogenetico_brote.png", 
                     caption="Divergencia del Brote 2024 (Marcado en Rojo) vs. Cepas Históricas", 
                     use_container_width=True)
        except:
            st.warning("'arbol_filogenetico_brote.png' análisis evolutivo.")

    with col_txt_tree:
        st.write("####  Análisis de Clados Emergentes")
        st.info("**Especificaciones Técnicas:**")
        st.write("""
        - **Herramientas:** MAFFT (Alineamiento) + IQ-TREE 2.
        - **Modelo Evolutivo:** GTR+F+I+G4 (ModelFinder).
        - **Hallazgo:** Se identificó una divergencia significativa en las secuencias con prefijos **PQ, PP y OR**.
        """)

    # --- 2. RASTREO DE MUTACIONES ---
    st.divider()
    st.header("2. Identificación de Mutaciones Críticas")
    
    data_mut_pdf = {
        "Posición Genómica": [208, 228, 291, 312],
        "Referencia (Ancestral)": ["C", "A", "C", "C"],
        "Brote Actual (2024)": ["T", "G", "T", "T"],
        "Prioridad Estructural": ["Media", "ALTA", "Media", "Alta"]
    }
    st.table(data_mut_pdf)
    st.success(" **Valor Estratégico:** Blancos principales para el modelado de péptidos bloqueadores.")

# --- PÁGINA: SEGURIDAD HÍDRICA (NOROVIRUS) ---
elif opcion == "Seguridad Hídrica (Norovirus)":
    st.title(" Seguridad Hídrica: Monitoreo de Norovirus")
    st.subheader("Validación Estructural y Vigilancia en Infraestructura Crítica")

    st.markdown("""
    El monitoreo de Norovirus es vital para la seguridad del agua. En esta sección validamos las estructuras 
    proteicas virales para asegurar que los modelos de simulación sean precisos.
    """)

    # --- SECCIÓN DE VALIDACIÓN (RAMACHANDRAN) ---
    st.divider()
    st.subheader("Validación Estereoquímica: Ramachandran Plot")

    col_img_n, col_txt_n = st.columns([1.5, 1])

    with col_img_n:
        try:
            st.image("ramachandran_plot.png", 
                     caption="Mapa de Ramachandran - Validación Estructural Norovirus", 
                     use_container_width=True)
        except:
            st.warning(" Archivo 'ramachandran_plot.png' no encontrado.")
    
    with col_txt_n:
        st.info("**Hito Técnico:** Validación para Dinámica Molecular (MD).")
        st.write("""
        **Resultados de Calidad:**
        - **Regiones Favorecidas:** 96.47% de los residuos.
        - **Interpretación:** La alta densidad en zonas verdes confirma estabilidad termodinámica.
        """)
        st.write("**Aplicación:** Estos modelos se utilizan para predecir la persistencia del virus en plantas de tratamiento.")

# --- PÁGINA: DINÁMICA MOLECULAR DE PÉPTIDOS (AMILOIDES) ---
elif opcion == "Dinámica Molecular de Péptidos (Amiloides)":
    st.title(" Dinámica Molecular de Estructuras Amiloides")
    st.subheader("Simulación de L-Difenilalanina (L-FF) en Mezclas de Agua y 2-Propanol")

    st.markdown("""
    **Investigación de Máster:** Estudio del proceso de autoensamblaje a nivel atómico. Los péptidos de difenilalanina son el modelo por excelencia para entender la formación de fibras amiloides, críticas tanto en enfermedades neurodegenerativas como en el diseño de nuevos bionanomateriales.
    """)

    # --- 1. METODOLOGÍA TÉCNICA (GROMACS) ---
    st.divider()
    col_tech, col_vis = st.columns([1, 1])

    with col_tech:
        st.header("1. Configuración del Sistema")
        st.write("""
        - **Molécula:** L-Difenilalanina (L-FF) en estado zwitteriónico.
        - **Software:** GROMACS 2020.4.
        - **Campo de Fuerza:** OPLS-AA (Optimized Potentials for Liquid Simulations).
        - **Solventes:** Mezclas binarias de Agua (TIP3P) y 2-Propanol en diversas fracciones molares.
        """)
        st.info("Se analizaron las interacciones no covalentes y la solvatación preferencial que dicta la agregación peptídica.")

    with col_vis:
        try:
            # Recuerda subir una imagen de tu tesis con este nombre
            st.image("simulacion_lff_box.png", caption="Sistema Solvatado de L-FF en GROMACS", use_container_width=True)
        except:
            st.warning(" s 'simulacion_lff_box.png'")

    # --- 2. ANÁLISIS DE RESULTADOS (RDF & ESTABILIDAD) ---
    st.divider()
    st.header("2. Termodinámica y Estructura")
    
    st.write("Resultados obtenidos tras 50ns de simulación por sistema:")

    tab_rdf, tab_hbond, tab_rg = st.tabs([" Solvatación (RDF)", " Puentes de Hidrógeno", " Estabilidad (Rg)"])

    with tab_rdf:
        st.write("#### Funciones de Distribución Radial g(r)")
        st.write("""
        El análisis de las RDF reveló una **solvatación preferencial** del 2-propanol hacia los anillos aromáticos. 
        Este desplazamiento del agua es el motor termodinámico que facilita la nucleación amiloide.
        """)
        # Aquí puedes mostrar una gráfica de RDF de tu tesis
        try:
            st.image("grafica_rdf_tesis.png", caption="Análisis g(r) - Solvatación Preferencial")
        except:
            st.write("(Gráfica de RDF pendiente de carga)")

    with tab_hbond:
        st.write("#### Dinámica de Enlaces de Hidrógeno")
        st.write("""
        Se cuantificó la competencia entre las interacciones péptido-péptido y péptido-solvente. 
        Este equilibrio es lo que define si el péptido permanece soluble o forma una estructura agregada.
        """)

    with tab_rg:
        st.write("#### Radio de Giro (Rg)")
        st.write("""
        La estabilidad del Radio de Giro durante la trayectoria confirma que la molécula mantiene su integridad conformacional, permitiendo interacciones de apilamiento $\pi-\pi$ (pi-stacking).
        """)

    # --- VALOR ESTRATÉGICO ---
    st.divider()
    st.success("""
    **Conexión Estratégica:** Mi experiencia en la física de péptidos me permite hoy en BioPath-Sentinel diseñar péptidos inhibidores de alta afinidad y predecir la estabilidad de proteínas virales bajo diversas condiciones de microambiente químico.
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

















































