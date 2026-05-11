# procesar_datos.py
# Requiere:  pip install pandas openpyxl
# Uso:       python procesar_datos.py
#
# Lee Encuesta.xlsx y muestra un resumen de frecuencias
# de cada pregunta en la consola.

import pandas as pd

df = pd.read_excel("Encuesta.xlsx")

df.columns = [
    "nombre", "correo", "timestamp",
    "conocimiento_ml",    # Conocimiento sobre ML (escala cualitativa)
    "nivel_seg_ml",       # Nivel infraestructura para ML en seguridad
    "metodos_trad",       # Usa métodos de seguridad tradicionales
    "tipo_ataque",        # Tipo de ciberataque más frecuente
    "beneficio_ml",       # Beneficio principal del ML en detección
    "arquitectura_ml",    # Arquitectura ML más efectiva
    "desafio_ml",         # Desafío principal para adoptar ML
    "ef_trad",            # Efectividad métodos tradicionales (1-5)
    "det_real",           # Importancia detección en tiempo real (1-5)
    "mejora_pred",        # ML mejora predicción ante SQL/XSS (Likert)
    "frec_actualizacion", # Frecuencia actualización de protocolos
    "factor_migracion",   # Factor para migrar a seguridad proactiva IA
]

preguntas = {
    "conocimiento_ml":    "Conocimiento sobre Machine Learning",
    "nivel_seg_ml":       "Nivel de infraestructura para seguridad + ML",
    "metodos_trad":       "¿Usa métodos de seguridad tradicionales?",
    "beneficio_ml":       "Beneficio principal del ML en detección",
    "ef_trad":            "Efectividad métodos tradicionales vs ataques sofisticados",
    "det_real":           "Importancia detección en tiempo real",
    "mejora_pred":        "ML mejora predicción ante SQL/XSS (Likert)",
    "desafio_ml":         "Desafío principal para adoptar ML",
    "arquitectura_ml":    "Arquitectura ML más efectiva",
    "factor_migracion":   "Factor para migrar a seguridad proactiva con IA",
    "frec_actualizacion": "Frecuencia de actualización de protocolos",
}

print("=" * 60)
print(f"  RESUMEN DE ENCUESTA  —  {len(df)} respuestas")
print("=" * 60)

for col, titulo in preguntas.items():
    print(f"\n▸ {titulo}")
    conteo = df[col].value_counts()
    for valor, n in conteo.items():
        pct = round(n / len(df) * 100, 1)
        barra = "█" * n
        print(f"   {valor:<18} {n:>2} ({pct:>4}%)  {barra}")

print("\n" + "=" * 60)
alto_ml  = df["conocimiento_ml"].isin(["Excelente","Importante","Muy importante"]).sum()
usa_trad = df["metodos_trad"].eq("Sí").sum()
infra_al = df["nivel_seg_ml"].eq("Alto").sum()
print("KPIs PRINCIPALES")
print(f"  Conocimiento ML alto (Excelente/Importante):  {alto_ml} ({round(alto_ml/len(df)*100)}%)")
print(f"  Usan métodos tradicionales (Sí):              {usa_trad} ({round(usa_trad/len(df)*100)}%)")
print(f"  Infraestructura nivel Alto:                   {infra_al} ({round(infra_al/len(df)*100)}%)")
print("=" * 60)

from flask import Flask, send_file

app = Flask(__name__)

@app.route("/")
def index():
    return send_file("dashboard.html")

if __name__ == "__main__":
    app.run(debug=False)