import pandas as pd

def limpiar_dataframe(ruta, header, fila_eliminar, renombrar_primera_col=True):
    """
    Limpia un archivo Excel eliminando filas sobrantes y reestablecer cabeceras.
    Args:
        ruta (str): ruta al archivo Excel
        header (int): número de fila a usar como cabecera
        fila_eliminar (int o list): número(s) de fila(s) a eliminar después
        renombrar_primer_col (bool): si True, renombra la primera columna a 'Perfil
    Returns:
        pd.DataFrame: DataFrame limpio
    """
    df = pd.read_excel(ruta, engine='openpyxl', header=header)

    # Renombrar NaN por 'Perfil' si la columna comienza con NaN
    if pd.isna(df.columns[0] and renombrar_primera_col):
        df.columns = ['Perfil'] + list(df.columns[1:])
    elif renombrar_primera_col  and df.iloc[0,0] != 'Perfil':
        # Si la primera fila tiene datos y queremos usarla como cabecera
        df.iloc[0,0] = 'Perfil'
        df.columns = df.iloc[0]
        # Eliminar la fila que fue usada como cabecera
        if isinstance(fila_eliminar, list):
            fila_eliminar = sorted(set(fila_eliminar + [0]), reverse=True)
        else:
            fila_eliminar = sorted([fila_eliminar, 0], reverse=True)
    # Eliminar fila(s) sobrante(s)
    if isinstance(fila_eliminar, list):
        fila_eliminar = [i for i in fila_eliminar if i < len(df)]
        if fila_eliminar:
            df = df.drop([df.index[i] for i in sorted(fila_eliminar, reverse=True)])
    else:
        if fila_eliminar < len(df):
            df = df.drop(df.index[fila_eliminar])
    # Resetear índices
    df = df.reset_index(drop=True)

    # Limpiar columnas: reemplazar Unnamed por Perfil y eliminar espacios
    df.columns = [col.replace('Unnamed: 0', 'Perfil').strip() if isinstance(col, str) else 'sin_nombre' for col in df.columns]
    return df

# Abrir y limpiar los archivos
archivos = {
    'religion_por_genero': ('data/religiosidad_por_sexo.xlsx', 10, 0, True),
    'religion_por_edad': ('data/religiosidad_por_edad.xlsx', 10, 0, True),
    'frecuencia_por_genero': ('data/frecuencia_atos_religiosos_por_sexo.xlsx', 12, 0, False),
    'frecuencia_por_edad': ('data/frecuencia_atos_religiosos_por_edad.xlsx', 12, 0, False),
}

dataframes = {}
for nombre, (ruta, header, fila_eliminar, renombrar) in archivos.items():
    dataframes[nombre] = limpiar_dataframe(ruta, header, fila_eliminar, renombrar)

# Mostrar resultados
for nombre, df in dataframes.items():
    print(f'{nombre}:')
    print(df)

# Guardar archivos en CSV
for nombre, df in dataframes.items():
    df.to_csv(f'output/{nombre}.csv', index=False)
    print(f'Archivo guardado en output/{nombre}.csv')