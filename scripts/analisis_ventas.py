
#Proy2 - Script de analisis de ventas 
import pandas as pd
import matplotlib.pyplot as plt 
import os 

#Leer datos 
df = pd.read_csv("datos/ventas_simuladas.csv")
#Convertir fecha
df['sales_date'] = pd.to_datetime(df['sales_date'])

#ANALISIS 1: Ventas totales
ventas_totales = df['amount'].sum()
print(f"Ventas totales: ${ventas_totales:.2f}")
#ANALISIS 2: Numero de transacciones
num_transacciones = len(df)
print(f"Numero de transacciones: {num_transacciones}")
#ANALISIS 3: Venta promedio
venta_promedio = df['amount'].mean()
print(f"Venta promedio: ${venta_promedio:.2f}")
#ANALISIS 4: Ventas por mes
df['year_month'] = df['sales_date'].dt.to_period('M')
ventas_por_mes = df.groupby('year_month')['amount'].agg(['sum','count','mean'])
print("Ventas por mes: ")
print(ventas_por_mes)
# ===== GRAFICO: Evolucion de ventas =====
plt.figure(figsize=(12, 6))
ventas_por_mes['sum'].plot(marker='o', linewidth=2, markersize=8, color='steelblue')
plt.title('Evolucion de Ventas Mensuales', fontsize=14, fontweight='bold')
plt.xlabel('Mes', fontsize=12)
plt.ylabel('Monto ($)', fontsize=12)
plt.grid(True, alpha=0.3)
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("resultados/grafico_ventas.png", dpi=300, bbox_inches='tight')
print("Grafico guardado en: resultados/grafico_ventas.png")
plt.close()

# ===== GRAFICO: Distribucion de ventas por dia =====
plt.figure(figsize=(12, 6))
plt.hist(df['amount'], bins=30, color='coral', edgecolor='black', alpha=0.7)
plt.title('Distribucion de Montos de Venta', fontsize=14, fontweight='bold')
plt.xlabel('Monto ($)', fontsize=12)
plt.ylabel('Frecuencia', fontsize=12)
plt.grid(True, alpha=0.3, axis='y')
plt.tight_layout()
plt.savefig("resultados/distribucion_ventas.png", dpi=300, bbox_inches='tight')
print("Grafico de distribucion guardado")
plt.close()

print("="*60)
print("ANALISIS COMPLETADO EXITOSAMENTE")
print("="*60)
