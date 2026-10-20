import pandas as pd

# 1. CARGA DE DATOS
clientes = pd.read_csv("data/clientes.csv")

# 2. EXPLORACIÓN GENERAL
print("=== EXPLORACIÓN DE CLIENTES ===")

print("\nPrimeras 5 filas:")
print(clientes.head())

print("\nDimensiones del dataset:")
print(clientes.shape)

print("\nInformación de las columnas:")
clientes.info()

# 3. VALIDACIONES DE CALIDAD
print("\n=== CALIDAD DE DATOS ===")

print("\nValores nulos por columna:")
print(clientes.isnull().sum())

print("\nFilas duplicadas:")
print(clientes.duplicated().sum())

print("\nID de clientes duplicados:")
print(clientes["id_cliente"].duplicated().sum())

# 4. CONVERSIÓN DE FECHAS
clientes["fecha_registro"] = pd.to_datetime(
    clientes["fecha_registro"]
)

print("\nTipo de dato de fecha_registro:")
print(clientes["fecha_registro"].dtype)