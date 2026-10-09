import pandas as pd
print(pd.__version__)

# 1. Crear el dataset de ejemplo simular a un CSV
datos_hospital = {
    'id_paciente': [101, 102, 103, 104, 105],
    'edad': [45, 23, 60, 35, 50],
    'nivel_glucosa': [140, 85, 180, 95, 160],
    'presion_arterial': [80, 70, 90, 72, 85],
    'indice_masa_corporal': [28.5, 21.0, 33.2, 24.1, 30.8],
    'diagnostico_diabetes': [1, 0, 1, 0, 1] # 1: Riesgo / 0: Sin riesgo
}

df = pd.DataFrame(datos_hospital)

# 2. Eliminar la columna que no aporta información útil (id_paciente)
df_limpio = df.drop(columns=['id_paciente'])

# 3. Separar Variables de Entrada (X) y Variable Objetivo (y)
X = df_limpio[['edad', 'nivel_glucosa', 'presion_arterial', 'indice_masa_corporal']] # Features / Entradas
y = df_limpio['diagnostico_diabetes']                                                # Target / Salida

# 4. Mostrar estructura
print("--- DATOS DE ENTRADA (FEATURES - X) ---")
print(X.head(2))

print("\n--- VARIABLE OBJETIVO (TARGET - y) ---")
print(y.head(2))