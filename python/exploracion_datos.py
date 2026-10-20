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

# 5. EXPLORACIÓN DE PRODUCTOS

productos = pd.read_csv("data/productos.csv")

print("\n=== EXPLORACIÓN DE PRODUCTOS ===")

print("\nPrimeras 5 filas:")
print(productos.head())

print("\nDimensiones del dataset:")
print(productos.shape)

print("\nInformación de las columnas:")
productos.info()

# 6. ESTADÍSTICAS DESCRIPTIVAS DE PRODUCTOS

print("\n=== ESTADÍSTICAS DE PRODUCTOS ===")

print(productos["costo_unitario"].describe())

# 7. EXPLORACIÓN DE PEDIDOS

pedidos = pd.read_csv("data/pedidos.csv")

print("\n=== EXPLORACIÓN DE PEDIDOS ===")

print("\nPrimeras filas:")
print(pedidos.head())

print("\nDimensiones del dataset:")
print(pedidos.shape)

print("\nInformación de las columnas:")
pedidos.info()

# 8. RELACIÓN ENTRE CLIENTES Y PEDIDOS

pedidos_clientes = pd.merge(
    pedidos,
    clientes,
    on="id_cliente",
    how="inner"
)

print("\n=== PEDIDOS CON INFORMACIÓN DE CLIENTES ===")
print(pedidos_clientes.head())

# 9. VALIDACIÓN DE RELACIONES ENTRE PEDIDOS Y CLIENTES

pedidos_clientes_left = pd.merge(
    pedidos,
    clientes,
    on="id_cliente",
    how="left",
    indicator=True
)

print("\n=== VALIDACIÓN DE PEDIDOS Y CLIENTES ===")

print(pedidos_clientes_left["_merge"].value_counts())


# 10. EXPLORACIÓN DEL DETALLE DE PEDIDOS

detalle = pd.read_csv("data/detalle_pedidos.csv")

print("\n=== DETALLE DE PEDIDOS ===")

print("\nPrimeras filas:")
print(detalle.head())

print("\nDimensiones:")
print(detalle.shape)

print("\nInformación de columnas:")
detalle.info()

# 11. RELACIÓN ENTRE PEDIDOS, DETALLE Y PRODUCTOS

ventas = pd.merge(
    detalle,
    pedidos,
    on="id_pedido",
    how="inner"
)

ventas = pd.merge(
    ventas,
    productos,
    on="id_producto",
    how="inner"
)

print("\n=== DATASET DE VENTAS ===")

print(ventas.head())

print("\nDimensiones:")
print(ventas.shape)

print("\nColumnas:")
print(ventas.columns.tolist())

# 12. CÁLCULO DEL IMPORTE POR LÍNEA

ventas["importe"] = (
    ventas["cantidad"] * ventas["precio_unitario"]
)

print("\n=== IMPORTES POR LÍNEA DE VENTA ===")

print(
    ventas[
        ["id_pedido", "nombre_producto",
         "cantidad", "precio_unitario", "importe"]
    ]
)

# 13. ANÁLISIS DE ESTADOS DE PEDIDOS

print("\n=== ESTADOS DE LOS PEDIDOS ===")

print(pedidos["estado"].value_counts())

# 14. FILTRAR VENTAS ENTREGADAS

ventas_entregadas = ventas[
    ventas["estado"] == "Entregado"
]

print("\n=== VENTAS ENTREGADAS ===")

print(
    ventas_entregadas[
        ["id_pedido", "nombre_producto", "importe", "estado"]
    ]
)

print("\nCantidad de líneas entregadas:")
print(len(ventas_entregadas))

# 15. FACTURACIÓN TOTAL

facturacion_total = ventas_entregadas["importe"].sum()

print("\n=== FACTURACIÓN TOTAL ===")
print(f"Facturación: ${facturacion_total:,.2f}")


# 16. CÁLCULO DEL TICKET PROMEDIO

cantidad_pedidos = ventas_entregadas["id_pedido"].nunique()

ticket_promedio = facturacion_total / cantidad_pedidos

print("\n=== TICKET PROMEDIO ===")
print(f"Pedidos entregados: {cantidad_pedidos}")
print(f"Ticket promedio: ${ticket_promedio:,.2f}")

# 17. CÁLCULO DE GANANCIA BRUTA

ventas_entregadas = ventas_entregadas.copy()

ventas_entregadas["costo_total"] = (
    ventas_entregadas["cantidad"]
    * ventas_entregadas["costo_unitario"]
)

ventas_entregadas["ganancia_bruta"] = (
    ventas_entregadas["importe"]
    - ventas_entregadas["costo_total"]
)

print("\n=== GANANCIA BRUTA POR PRODUCTO ===")

print(
    ventas_entregadas[
        ["nombre_producto", "cantidad",
         "importe", "costo_total", "ganancia_bruta"]
    ]
)

# 18. GANANCIA BRUTA TOTAL

ganancia_bruta_total = ventas_entregadas["ganancia_bruta"].sum()

print("\n=== GANANCIA BRUTA TOTAL ===")
print(f"Ganancia bruta: ${ganancia_bruta_total:,.2f}")

# 19. CÁLCULO DEL MARGEN BRUTO

margen_bruto = (
    ganancia_bruta_total / facturacion_total
) * 100

print("\n=== MARGEN BRUTO ===")
print(f"Margen bruto: {margen_bruto:.2f}%")