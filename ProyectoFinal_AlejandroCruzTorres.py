
# =============================================================================
# PROYECTO DE EJEMPLO: ANÁLISIS DE PROMEDIOS CICLO ESCOLAR 2024-2025 Y 2025-2026
# =============================================================================
# Pregunta: ¿Cuál es la tendencia en promedios en matematicas y español de alumnos de 3o de Secundaria?
# =============================================================================

# -----------------------------------------------------------------------------
# IMPORTACIONES
# -----------------------------------------------------------------------------
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np


# -----------------------------------------------------------------------------
# 1. CARGAR DATOS A ANALIZAR
# -----------------------------------------------------------------------------
#Se carga el archivo en formato encoding='ISO-8859-1', ya que contiene en el contenido la letra Ñ
def f_Carga_archivo_promedios():
    print("=" * 100)
    print("PASO 1: CARGA DE ARCHIVO DE CALIFICACIONES")    
    print("=" * 100)
    df_promedios = pd.read_csv('promedios.csv',sep=",",encoding='ISO-8859-1' )

    return df_promedios 

# -----------------------------------------------------------------------------
# 2. EXPLORACIÓN INICIAL
# -----------------------------------------------------------------------------
def f_exploracion_inicial(df_promedios):
    #Validar información
    #Ver primeras filas
    print("=" * 100)
    print("PASO 2: EXPLORACIÓN DE LA INFORMACIÓN CARGADA AL DATASET")    
    print("=" * 100)
    print("\n=====> Primeras filas")
    print(df_promedios.head)
    #Ver primeras y filas finales
    print("\n=====> Primeras y ultimas filas")
    print(df_promedios)
    # Información del dataset
    print("\n=====> Informacíon del Dataset")
    print(df_promedios.info())
    # Estadísticas descriptivas
    print("\n=====> Estadísticas Descriptivas")
    print(df_promedios.describe())
    # Verificar valores nulos
    print("\n=====> Valores nulos")
    print(df_promedios.isnull().sum())
    print()

# -----------------------------------------------------------------------------
# 3. INTERPRETACIÓN DE INFORMACIÓN CARGADA
# -----------------------------------------------------------------------------
# - Se tienen 400 registros de alumnos con 3 evaluaciones
# - 200 registros corresponden al ciclo escolar 2024-2025 y 200 a 2025-2026
#   200 registros corresponde a matemáticas y 200 a español
# - Las evaluaciones van de 6 a 10
# - No hay valores nulos
def f_interpretar_información(df_promedios):
    print("=" * 100)
    print("PASO 3: TOTALES DE LA INFORMACIÓN CARGADA")    
    print("=" * 100)
    #Obtener total de registros
    registros = len(df_promedios)
    print("Total de registros", registros )
    #Obtener total de columnas
    columnas = len(df_promedios.columns)
    print("Total de columnas", columnas )
    #Obtener total de registros por ciclo
    df_promedio_ciclo =  df_promedios.groupby('cicloescolar').size()
    print("Total de cicloescolar", df_promedio_ciclo )
    #Obtener total de registros por asignatura
    df_promedio_asignatura =  df_promedios.groupby('asignatura').size()
    print("Total de cicloescolar", df_promedio_asignatura )
    #Obtener calificacion minima
    minimos = df_promedios[['calif1', 'calif2', 'calif3']].min()
    print("Mínimos\n", minimos )
    # Obtener calificación máxima
    maximos = df_promedios[['calif1', 'calif2', 'calif3']].max()    
    print("Máximos\n", maximos )
    #Obtener promedio de evaluaciones
    promedios = df_promedios[['calif1', 'calif2', 'calif3']].mean()    
    print("Promedios\n", promedios )

# -----------------------------------------------------------------------------
# 4. LIMPIEZA Y PREPARACIÓN DE DATOS
# -----------------------------------------------------------------------------
def f_limpieza_preparacion_datos(df_promedios):
    print("=" * 70)
    print("PASO 4: LIMPIEZA DE DATOS")
    print("=" * 70)
    # Verificar duplicados
    duplicados = df_promedios.duplicated().sum()
    print(f"\nDuplicados encontrados: {duplicados}")
    if duplicados > 0:
        df = df_promedios.drop_duplicates()
        print("Duplicados eliminados")

    # Verificar tipos de datos
    print("\n=== TIPOS DE DATOS ===")
    print(df_promedios.dtypes)

    #Crear columna de promedio truncado a 2 digitos
    df_promedios['promedio'] = np.trunc((df_promedios[['calif1', 'calif2', 'calif3']].mean(axis=1))*100)/100
    print(df_promedios)


# -----------------------------------------------------------------------------
# 5. ANÁLISIS DE LA INFORMACIÓN CARGADA
# -----------------------------------------------------------------------------
def f_analisis_información(df_promedios):
    print("=" * 70)
    print("PASO 5: ANÁLISIS DESCRIPTIVO")
    print("=" * 70)

    # ANÁLISIS 1: Promedio por asignatura y ciclo escolars
    promedio_asignatura_ciclo = df_promedios.groupby(['asignatura', 'cicloescolar'])['promedio'].mean().reset_index()
    promedio_asignatura_ciclo['promedio'] = np.trunc(promedio_asignatura_ciclo['promedio'] * 100) / 100

#    df.groupby(['asignatura', 'ciclo'])['promedio'].mean().reset_index()

    print(f"\n=== VENTAS TOTALES ===")
    print(promedio_asignatura_ciclo)
    #print(f"Promedio por transacción: ${df['total'].mean():,.2f}")
    #print(f"Mediana: ${df['total'].median():,.2f}")

    # ANÁLISIS 2: Ventas por producto
    """print("\n=== VENTAS POR PRODUCTO ===")
    ventas_producto = df.groupby('producto')['total'].agg([
        ('total', 'sum'),
        ('promedio', 'mean'),
        ('transacciones', 'count')
    ]).sort_values('total', ascending=False)
    print(ventas_producto)
    """
    return promedio_asignatura_ciclo

# -----------------------------------------------------------------------------
# 6. VISUALIZACIONES
# -----------------------------------------------------------------------------

def f_visualizar_analisis(df_promedios_ciclo, tipo):
    print("=" * 70)
    print("PASO 4: CREANDO VISUALIZACIONES")
    print("=" * 70)

    # Configurar estilo
    plt.style.use('default')
    sns.set_palette("husl")

    # VISUALIZACIÓN 1: Ventas por producto (Gráfico de barras)
    print("\nCreando Gráfico 1:Promedios por Asignatura y Ciclo Escolar...")

    match tipo:
        case "barras":
            # Configurar el estilo
            sns.set_theme(style="darkgrid") # Fondo gris con cuadrícula blanca
            sns.set_palette("magma")   
            # Crear el gráfico de barras
            plt.figure(figsize=(10, 6))
            plt.xlabel('Asignatura', fontsize=12)
            plt.ylabel('Promedios', fontsize=12) 
            plt.grid(axis='y', linestyle='--', alpha=0.5)
            plt.tight_layout()
            grafico = sns.barplot(
                data=df_promedios_ciclo, 
                x='asignatura', 
                y='promedio', 
                hue='cicloescolar'
            )
            
            # 2. Iteración sobre los contenedores para poner las etiquetas
            for container in grafico.containers:
                grafico.bar_label(container, fmt='%.2f', padding=3)

            # Personalización
            plt.title('Promedio por Asignatura y Ciclo Escolar')
            plt.ylim(0, 10)  # Ajustar escala de calificaciones
            plt.legend(title='Ciclo Escolar', )

            plt.savefig('grafico1_promedios_asignatura_ciclo.png', dpi=300, bbox_inches='tight')
            print("✓ Gráfico 1 guardado")

            plt.show()

        case 'linea':
            print("\nCreando Gráfico 2: Tendencia de promedios por ciclo escolar...")
            plt.figure(figsize=(10, 6))
            promedios_cicloescolar = df_promedios.groupby(['cicloescolar'])['promedio'].mean()
            print(promedios_cicloescolar)
            plt.plot(promedios_cicloescolar.index, promedios_cicloescolar.values, linewidth=2, color='green')
            plt.title('Tendencia de Promedios de Español y Matemáticas por Ciclo Escolar', fontsize=16, fontweight='bold')
            plt.xlabel('Ciclo Escolar', fontsize=12)
            plt.ylabel('Promedios', fontsize=12)
            plt.grid(True, alpha=0.3)
            plt.xticks(rotation=45)
            plt.tight_layout()
            plt.savefig('grafico2_tendencia_promedios_cicloescolar.png', dpi=300, bbox_inches='tight')
            plt.show()
            print("✓ Gráfico 2 guardado")

        case 'caja':
            # Configurar el estilo
            sns.set_theme(style="darkgrid") # Fondo gris con cuadrícula blanca
            plt.figure(figsize=(10, 6))                        
            # Crear el Boxplot
            # x: Categorías (Español, Matemáticas)
            # y: Los valores numéricos (Promedios)
            ax = sns.boxplot(data=df_promedios, x='asignatura', y='promedio', palette="magma")

            # Opcional: Agregar los puntos individuales encima para ver cada ciclo exacto
            sns.stripplot(data=df_promedios, x='asignatura', y='promedio', color="black", alpha=0.3)

            plt.title('Distribución de Promedios por Asignatura', fontsize=14)
            plt.ylabel('Promedio')
            plt.xlabel('Asignatura')
            plt.savefig('grafico3_rango_promedios_asignatura.png', dpi=300, bbox_inches='tight')
            plt.show()
            print("✓ Gráfico 3 guardado")


        case 'pastel':
            # VISUALIZACIÓN 4: Promedios por Ciclo escolar por región (Gráfico de pastel)
            print("\nCreando Gráfico 4: Distribución de Promedios")
            plt.figure(figsize=(8, 8))
            ventas_region_pie = df_promedios.groupby('promedio')['promedio'].sum()
            #df_promedios.boxplot(column='promedio', by='cicloescolar', grid=False)            
            plt.pie(ventas_region_pie.values, labels=ventas_region_pie.index, 
                    autopct='%1.1f%%', startangle=90, colors=['#ff9999','#66b3ff','#99ff99'])
            plt.title('Distribución de Promedios', fontsize=16, fontweight='bold')
            plt.tight_layout()
            plt.savefig('grafico4_promedios.png', dpi=300, bbox_inches='tight')
            plt.show()
            print("✓ Gráfico 4 guardado")

def f_interpretacion_resultados():
    # -----------------------------------------------------------------------------
    # 7. INTERPRETACIÓN Y CONCLUSIONES
    # -----------------------------------------------------------------------------
    print("=" * 70)
    print("PASO 5: INTERPRETACIÓN DE RESULTADOS")
    print("=" * 70)

    print("""
    HALLAZGOS PRINCIPALES:
    ----------------------

    1. TENDENCIA DE PROMEDIOS:
    - Los promedios tienden a mejorar del ciclo escolar 2024-2025 respecto al ciclo escolar 2025-2026

    RESPUESTA A LA PREGUNTA INICIAL:
    ---------------------------------
    "¿Cuál es la tendencia en promedios en matematicas y español de alumnos de 3o de Secundaria?"

    TENDENCIA: Los promedios de ambas asignaturas por ciclo escolar se aprecia la tendencia a una leve mejoría,
            ya que en el ciclo escolar 2024-2025 se tuvo un promedio de 8.04 y se concluye el ciclo 2025-2026 en 8.06.
            Sin embargo se observa que en la asignatura de español es la que aporta la tendencia a mejoría ya que 
            del ciclo 1 fue de 8.01 y en en el c1clo 2 concluye en 8.06, pero en la asgnatura de matematicas se tiene un
            decremento ya que en el ciclo 1 el promedio fue de 8.10 y en el ciclo 2 se concluye con 8.01
            
    RANGO DE PROMEDIOS:
    1. Los promedios de Español se encuentran en el rango de 6.4 A 10
    2. Los promedios de Matemáticas se encuentran en el rango de 6.0 A 9.7

    PROMEDIOS DONDE SE CONCENTRA LA INFORMACIÓN
    1. Los promedios de Español se concentran mayormente en el rango de 7.3 a 8.7
    2. Los promedios de Matemáticas se concentran mayormente en el rango de 7.7 a 8.7

    LIMITACIONES DEL ANÁLISIS:
    ---------------------------
    - El conjunto de alumnos considerados en este análisis solo es una muestra, se requeríria hacer 
      el analisis procesamiento de la información con la totalidad de los alumnos, esto permitiría poder
      obtener la información  por alcaldías y poder ver en que zonas se tiene mayor rezago en apropvechamiento.

    
    CONCLUSIÓN GENERAL:
    -------------------
    El aprovechamiento obtenido en el muestreo se aprecia una leve mejoría, pero para poder obtener los datos
    mas precisos se se requiere realizar el analisis sobre el total de la población estudiantil agrupandolos por 
    alcaldias.
    Y deberá de realizarse el analisis por asignatura, para poder enfocar las herramientas pedagógicas en 
    aquellas zonas de mayor rezago.

    """)

    print("=" * 70)
    print("FIN DEL ANÁLISIS DE PROMEDIOS")
    print("=" * 70)


df_promedios = f_Carga_archivo_promedios()
f_exploracion_inicial(df_promedios)
f_interpretar_información(df_promedios)
f_limpieza_preparacion_datos(df_promedios)
df_promedios_ciclo = f_analisis_información(df_promedios)
f_visualizar_analisis(df_promedios_ciclo, 'linea')
f_visualizar_analisis(df_promedios_ciclo, 'barras')
f_visualizar_analisis(df_promedios_ciclo, 'caja')
f_visualizar_analisis(df_promedios_ciclo, 'pastel')
f_interpretacion_resultados()
