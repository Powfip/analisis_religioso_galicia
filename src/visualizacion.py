import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import os
from matplotlib.ticker import PercentFormatter

# Configurar estilo y colores
sns.set_style("whitegrid")
sns.set_palette("husl")
plt.rcParams['figure.figsize'] = (14, 7)
plt.rcParams['font.size'] = 11

# Crear carpeta para gráficos si no existe
os.makedirs('output/graficos', exist_ok=True)

# Cargar datos
df_religion_genero = pd.read_csv('output/religion_por_genero.csv')
df_religion_edad = pd.read_csv('output/religion_por_edad.csv')
df_frecuencia_genero = pd.read_csv('output/frecuencia_por_genero.csv')
df_frecuencia_edad = pd.read_csv('output/frecuencia_por_edad.csv')

# Convertir a porcentajes (multiplicar por 100)
for col in df_religion_genero.columns:
    if col != 'Perfil':
        df_religion_genero[col] = df_religion_genero[col] * 100

for col in df_religion_edad.columns:
    if col != 'Perfil':
        df_religion_edad[col] = df_religion_edad[col] * 100

for col in df_frecuencia_genero.columns:
    if col != 'Perfil':
        df_frecuencia_genero[col] = df_frecuencia_genero[col] * 100

for col in df_frecuencia_edad.columns:
    if col != 'Perfil':
        df_frecuencia_edad[col] = df_frecuencia_edad[col] * 100

# ============================================================================
# GRÁFICO 1: Religión por Género (Gráfico de barras)
# ============================================================================
fig, ax = plt.subplots(figsize=(12, 6))

# Preparar datos (excluir Total, N, N.C.)
data = df_religion_genero[['Perfil', 'Hombre', 'Mujer']].copy()
data = data[~data['Perfil'].isin(['(N)', 'N.C.'])].reset_index(drop=True)

x = range(len(data))
width = 0.35

bars1 = ax.bar([i - width/2 for i in x], data['Hombre'], width, label='Hombre', alpha=0.8)
bars2 = ax.bar([i + width/2 for i in x], data['Mujer'], width, label='Mujer', alpha=0.8)

ax.set_xlabel('Religión', fontsize=12, fontweight='bold')
ax.set_ylabel('Porcentaje (%)', fontsize=12, fontweight='bold')
ax.set_title('Religiosidad en Galicia por Género', fontsize=14, fontweight='bold')
ax.set_xticks(x)
ax.set_xticklabels(data['Perfil'], rotation=45, ha='right')
ax.yaxis.set_major_formatter(PercentFormatter(decimals=0))
ax.legend(loc='upper right', fontsize=11)
ax.grid(axis='y', alpha=0.3)

plt.tight_layout()
plt.savefig('output/graficos/01_religion_por_genero.png', dpi=300, bbox_inches='tight')
print('✓ Guardado: output/graficos/01_religion_por_genero.png')
plt.close()

# ============================================================================
# GRÁFICO 2: Religión por Edad (Gráfico de barras)
# ============================================================================
fig, ax = plt.subplots(figsize=(14, 6))

# Columnas de edad (excluir Perfil, Total, N, N.C.)
edad_cols = [col for col in df_religion_edad.columns if col not in ['Perfil', 'Total']]
data_filtered = df_religion_edad[~df_religion_edad['Perfil'].isin(['(N)', 'N.C.'])].reset_index(drop=True)

x = range(len(edad_cols))
width = 0.12
multiplier = 0

for idx, row in data_filtered.iterrows():
    offset = width * multiplier
    valores = [row[col] for col in edad_cols]
    ax.bar([i + offset for i in x], valores, width, label=row['Perfil'])
    multiplier += 1

ax.set_xlabel('Grupo de Edad', fontsize=12, fontweight='bold')
ax.set_ylabel('Porcentaje (%)', fontsize=12, fontweight='bold')
ax.set_title('Religiosidad en Galicia por Grupo de Edad', fontsize=14, fontweight='bold')
ax.set_xticks([i + width * (len(data_filtered) - 1) / 2 for i in x])
ax.set_xticklabels(edad_cols, rotation=45, ha='right')
ax.yaxis.set_major_formatter(PercentFormatter(decimals=0))
ax.legend(bbox_to_anchor=(1.05, 1), loc='upper left', fontsize=10)
ax.grid(axis='y', alpha=0.3)

plt.tight_layout()
plt.savefig('output/graficos/02_religion_por_edad.png', dpi=300, bbox_inches='tight')
print('✓ Guardado: output/graficos/02_religion_por_edad.png')
plt.close()

# ============================================================================
# GRÁFICO 3: Frecuencia por Género (Gráfico de barras)
# ============================================================================
fig, ax = plt.subplots(figsize=(12, 6))

# Preparar datos (excluir N, N.C., Total)
data = df_frecuencia_genero[['Perfil', 'Hombre', 'Mujer']].copy()
data = data[~data['Perfil'].isin(['(N)', 'N.C.'])].reset_index(drop=True)

x = range(len(data))
width = 0.35

bars1 = ax.bar([i - width/2 for i in x], data['Hombre'], width, label='Hombre', alpha=0.8)
bars2 = ax.bar([i + width/2 for i in x], data['Mujer'], width, label='Mujer', alpha=0.8)

ax.set_xlabel('Frecuencia de Asistencia', fontsize=12, fontweight='bold')
ax.set_ylabel('Porcentaje (%)', fontsize=12, fontweight='bold')
ax.set_title('Frecuencia de Asistencia a Actos Religiosos por Género', fontsize=14, fontweight='bold')
ax.set_xticks(x)
ax.set_xticklabels(data['Perfil'], rotation=45, ha='right')
ax.yaxis.set_major_formatter(PercentFormatter(decimals=0))
ax.legend(loc='upper right', fontsize=11)
ax.grid(axis='y', alpha=0.3)

plt.tight_layout()
plt.savefig('output/graficos/03_frecuencia_por_genero.png', dpi=300, bbox_inches='tight')
print('✓ Guardado: output/graficos/03_frecuencia_por_genero.png')
plt.close()

# ============================================================================
# GRÁFICO 4: Frecuencia por Edad (Gráfico de barras)
# ============================================================================
fig, ax = plt.subplots(figsize=(14, 6))

# Preparar datos para barras (excluir (N), N.C.)
edad_cols = [col for col in df_frecuencia_edad.columns if col not in ['Perfil', 'Total']]
data_filtered = df_frecuencia_edad[~df_frecuencia_edad['Perfil'].isin(['(N)', 'N.C.'])].reset_index(drop=True)

x = range(len(edad_cols))
width = 0.12
multiplier = 0

for idx, row in data_filtered.iterrows():
    offset = width * multiplier
    valores = [row[col] for col in edad_cols]
    ax.bar([i + offset for i in x], valores, width, label=row['Perfil'])
    multiplier += 1

ax.set_xlabel('Grupo de Edad', fontsize=12, fontweight='bold')
ax.set_ylabel('Porcentaje (%)', fontsize=12, fontweight='bold')
ax.set_title('Frecuencia de Asistencia a Actos Religiosos por Edad', fontsize=14, fontweight='bold')
ax.set_xticks([i + width * (len(data_filtered) - 1) / 2 for i in x])
ax.set_xticklabels(edad_cols, rotation=45, ha='right')
ax.yaxis.set_major_formatter(PercentFormatter(decimals=0))
ax.legend(bbox_to_anchor=(1.05, 1), loc='upper left', fontsize=10)
ax.grid(axis='y', alpha=0.3)

plt.tight_layout()
plt.savefig('output/graficos/04_frecuencia_por_edad.png', dpi=300, bbox_inches='tight')
print('✓ Guardado: output/graficos/04_frecuencia_por_edad.png')
plt.close()

print('\n' + '='*60)
print('✓ TODAS LAS VISUALIZACIONES CREADAS Y GUARDADAS')
print('='*60)
print('\nGráficos disponibles en: output/graficos/')
print('  1. 01_religion_por_genero.png')
print('  2. 02_religion_por_edad.png')
print('  3. 03_frecuencia_por_genero.png')
print('  4. 04_frecuencia_por_edad.png')

