import pandas as pd
from sklearn.ensemble import IsolationForest
import matplotlib.pyplot as plt

# DATOS FINANCIEROS

datos = {
    "monto": [
        120,
        150,
        130,
        170,
        160,
        180,
        200,
        210,
        190,
        175,
        5000,   # anomalía
        6200    # anomalía
    ]
}

df = pd.DataFrame(datos)

# MODELO IA

modelo = IsolationForest(
    contamination=0.15,
    random_state=42
)

# Entrenar modelo
modelo.fit(df[["monto"]])

# Detectar anomalías
df["anomalia"] = modelo.predict(df[["monto"]])

# Convertir valores
df["anomalia"] = df["anomalia"].map({
    1: "Normal",
    -1: "Anómalo"
})

# =========================
# MOSTRAR RESULTADOS
# =========================

print("\n===== DETECCIÓN DE ANOMALÍAS =====\n")

print(df)

# =========================
# GRÁFICA
# =========================

plt.figure(figsize=(8,5))

for i in range(len(df)):
    if df["anomalia"][i] == "Anómalo":
        plt.scatter(i, df["monto"][i], marker="x", s=100)
    else:
        plt.scatter(i, df["monto"][i])

plt.title("Detección de anomalías financieras")
plt.xlabel("Transacción")
plt.ylabel("Monto")

plt.show()