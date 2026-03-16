# 📊 Análisis de Religiosidad en Galicia

Proyecto de análisis y visualización de datos sobre religiosidad, frecuencia de asistencia a actos religiosos y distribución por género y edad en Galicia.

## 📋 Descripción del Proyecto

Este proyecto procesa datos de un barómetro de marzo 2024 sobre religiosidad en Galicia, realizando:

- **Limpieza y transformación** de archivos Excel
- **Exportación a CSV** para análisis posterior
- **Visualización** mediante gráficos profesionales
- **Análisis** de tendencias por género y grupo de edad

## 📁 Estructura del Proyecto

```
datos_religiosidad_galicia/
├── README.md                          # Este archivo
├── requeriments.txt                   # Dependencias del proyecto
├── data/                              # Datos originales (Excel)
│   ├── religiosidad_por_sexo.xlsx
│   ├── religiosidad_por_edad.xlsx
│   ├── frecuencia_atos_religiosos_por_sexo.xlsx
│   └── frecuencia_atos_religiosos_por_edad.xlsx
├── output/                            # Archivos generados
│   ├── *.csv                          # Datos procesados en CSV
│   └── graficos/                      # Gráficos generados
│       ├── 01_religion_por_genero.png
│       ├── 02_religion_por_edad.png
│       ├── 03_frecuencia_por_genero.png
│       └── 04_frecuencia_por_edad.png
└── scr/                               # Scripts Python
    ├── limpieza.py                    # Procesamiento de datos
    ├── scraping.py                    # (Reservado para web scraping)
    └── visualizacion.py               # Generación de gráficos
```

## 🛠️ Soluciones Implementadas

### 1. **Limpieza de Datos (limpieza.py)**

#### Problemas Identificados:
- ❌ Archivos Excel con múltiples encabezados y filas sobrantes
- ❌ Nombres de columnas inconsistentes (NaN, Unnamed)
- ❌ Filas de metadatos mezcladas con datos reales

#### Soluciones Aplicadas:
✅ **Función reutilizable** `limpiar_dataframe()` para procesar todos los archivos
✅ **Automatización** del renombrado de columnas a "Perfil"
✅ **Eliminación inteligente** de filas sobrantes basada en índices
✅ **Estandarización** de nombres de columnas

```python
def limpiar_dataframe(ruta, header, fila_eliminar, renombrar_primera_col=True):
    """Limpia un archivo Excel eliminando filas sobrantes y renombrando cabeceras."""
    # Procesa el archivo según parámetros específicos
    # Retorna un DataFrame limpio y listo para análisis
```

#### Resultado:
- 4 archivos Excel procesados correctamente
- Exportados a CSV en `output/`
- Datos listos para visualización

---

### 2. **Visualización de Datos (visualizacion.py)**

#### Problemas Identificados:
- ❌ Datos en formato decimal (0.116) poco comprensible para usuarios finales
- ❌ Falta de gráficos profesionales
- ❌ Filas de muestra (N) y No Contesta (N.C.) afectando visualización

#### Soluciones Aplicadas:
✅ **Conversión a porcentajes** (0.116 → 11.6%) para mejor legibilidad
✅ **4 gráficos de barras profesionales** con alta resolución (300 DPI)
✅ **Filtrado automático** de filas innecesarias (N, N.C.)
✅ **Estandarización de estilos** con paleta de colores coherente
✅ **Formato de ejes** en porcentaje (%) para claridad inmediata

#### Gráficos Generados:

1. **Religión por Género** (`01_religion_por_genero.png`)
   - Barras agrupadas: Hombre vs Mujer
   - Muestra distribución de creencias por género
   - Categorías: Católico practicante, Católico no practicante, Creyente otra religión, Agnóstico, Indiferente, Ateo

2. **Religión por Edad** (`02_religion_por_edad.png`)
   - Barras agrupadas por grupo de edad
   - Análisis de evolución religiosa según tramos de edad
   - Grupos: 18-24, 25-34, 35-44, 45-54, 55-64, 65-74, 75+

3. **Frecuencia por Género** (`03_frecuencia_por_genero.png`)
   - Comparativa de asistencia a actos religiosos por género
   - Categorías: Nunca, Casi nunca, Varias veces al año, 2-3 veces mes, Todos domingos, Varias veces semana

4. **Frecuencia por Edad** (`04_frecuencia_por_edad.png`)
   - Patrón de asistencia según grupo de edad
   - Identifica grupos más/menos practicantes por edad

---

## 🚀 Cómo Usar

### Requisitos Previos
```bash
Python 3.8+
pip o conda
```

### Instalación

1. **Clonar/Descargar el proyecto**
```bash
cd datos_religiosidad_galicia
```

2. **Crear entorno virtual** (recomendado)
```bash
python -m venv .venv
source .venv/bin/activate  # En macOS/Linux
# o
.venv\Scripts\activate     # En Windows
```

3. **Instalar dependencias**
```bash
pip install -r requeriments.txt
```

### Ejecución

#### Opción 1: Ejecutar todo el pipeline
```bash
# Primero: Limpiar datos
python scr/limpieza.py

# Luego: Generar gráficos
python scr/visualizacion.py
```

#### Opción 2: Ejecutar scripts individuales
```bash
# Solo limpiar datos
python scr/limpieza.py

# Solo generar gráficos (si ya están los CSV)
python scr/visualizacion.py
```

---

## 📊 Análisis de Resultados

### Insights Principales

#### Por Género:
- Las mujeres tienden a ser más religiosas que los hombres
- Casos destacables:
  - Católicas practicantes: 20.6% (vs 11.6% hombres)
  - Ateos: 18.9% hombres (vs 11.1% mujeres)

#### Por Edad:
- Los jóvenes (18-24) son más agnósticos e indiferentes (38.7% + 19.6%)
- Los mayores (75+) son más católicos practicantes (57.4%)
- Tendencia clara: A mayor edad, mayor religiosidad

#### Frecuencia de Asistencia:
- Mayoría nunca asiste a actos religiosos (33.4%)
- Solo 9.6% asiste todos los domingos
- Variación significativa por edad: mayores asisten más frecuentemente

---

## 🔧 Características Técnicas

### Limpieza de Datos
- **Manejo inteligente de encabezados**: Detecta automáticamente filas de encabezado
- **Normalización de columnas**: Convierte nombres inconsistentes a estándares
- **Filtrado automático**: Elimina filas de metadatos sin intervención manual
- **Modularidad**: Una función para todos los archivos (DRY principle)

### Visualización
- **Alta resolución**: 300 DPI para impresión profesional
- **Porcentajes automáticos**: Convierte decimales a % para mejor comprensión
- **Formato profesional**: Títulos, etiquetas y leyendas claras
- **Grid inteligente**: Mejora legibilidad sin sobrecargar

### Escalabilidad
- Agregar nuevos gráficos es trivial (solo añadir más figuras)
- Agregar nuevos datos es simple (solo extender el diccionario de archivos)
- Los scripts son reutilizables para otros proyectos similares

---

## 📈 Archivos Generados

### CSV (Datos Procesados)
| Archivo | Descripción |
|---------|-------------|
| `religion_por_genero.csv` | Distribución religiosa por género |
| `religion_por_edad.csv` | Distribución religiosa por edad |
| `frecuencia_por_genero.csv` | Frecuencia de asistencia por género |
| `frecuencia_por_edad.csv` | Frecuencia de asistencia por edad |

### PNG (Gráficos)
| Archivo | Tipo | Uso |
|---------|------|-----|
| `01_religion_por_genero.png` | Barras agrupadas | Comparativa género |
| `02_religion_por_edad.png` | Barras agrupadas | Análisis por edad |
| `03_frecuencia_por_genero.png` | Barras agrupadas | Asistencia por género |
| `04_frecuencia_por_edad.png` | Barras agrupadas | Asistencia por edad |

---

## 🐛 Mejoras Futuras

- [ ] Agregar análisis estadístico (Chi-cuadrado, correlaciones)
- [ ] Crear un dashboard interactivo con Plotly/Streamlit
- [ ] Incluir tests automatizados
- [ ] Exportar resultados a Excel con gráficos incrustados
- [ ] Crear reporte PDF automático
- [ ] Análisis geográfico dentro de Galicia (por comarcas)

---

## 📦 Dependencias

```
pandas>=1.3.0
openpyxl>=3.6.0
matplotlib>=3.4.0
seaborn>=0.11.0
```

Ver `requeriments.txt` para versiones exactas.

---

## 👨‍💻 Autor

Proyecto de análisis de datos - Marzo 2026

---

## 📝 Licencia

Este proyecto es de código abierto y libre para usar y modificar.

---

## 📞 Notas Técnicas

### Por qué esta arquitectura:
1. **Separación de responsabilidades**: Cada script hace una cosa bien
2. **Reutilización**: Funciones genéricas para múltiples archivos
3. **Mantenibilidad**: Cambios centralizados en una función
4. **Escalabilidad**: Fácil agregar nuevos datos/gráficos
5. **Profesionalismo**: Código limpio, documentado y modular

### Flujo de datos:
```
Excel → Limpieza → CSV → Visualización → PNG
(Data)   (Script)  (Data)  (Script)      (Output)
```

---

## ✅ Checklist del Proyecto

- [x] Limpiar y procesar archivos Excel
- [x] Exportar datos a CSV
- [x] Crear visualizaciones profesionales
- [x] Convertir datos a porcentajes
- [x] Filtrar datos innecesarios (N, N.C.)
- [x] Documentar todo el proceso
- [x] Preparar para presentación

---

**Última actualización**: 16 de marzo de 2026
