# Conta Ayuda API

API REST desarrollada con **FastAPI** para analizar datos financieros a partir de archivos CSV o JSON. El proyecto utiliza **Pandas** para el procesamiento de datos y **Scikit-learn** para la detección de anomalías. Fue desarrollado como parte del curso de Ingeniería de Software.

## Tecnologías

- Python 3.10+
- FastAPI
- Pandas
- NumPy
- Scikit-learn
- Pytest
- GitHub Actions

## Instalación

```bash
# Clonar el repositorio
git clone https://github.com/Laura-Montana/prueba.git
cd prueba

# Crear entorno virtual
python -m venv venv

# Activar entorno
# Linux/macOS
source venv/bin/activate

# Windows
venv\Scripts\activate

# Instalar dependencias
pip install -r requirements.txt

# Ejecutar la aplicación
uvicorn main:app --reload
```

La API estará disponible en:

- API: http://localhost:8000
- Documentación Swagger: http://localhost:8000/docs

---

## Funcionalidades

- Carga de archivos CSV y JSON.
- Validación de formato y datos.
- Cálculo de métricas financieras.
- Análisis de tendencias.
- Comparación entre períodos.
- Detección de valores atípicos.
- Generación de reportes en formato JSON.

---

## Formato de entrada

### CSV

```csv
fecha,monto,categoria
2024-01-15,1500000,ventas
2024-01-20,500000,gastos
```

### JSON

```json
[
  {
    "fecha": "2024-01-15",
    "monto": 1500000,
    "categoria": "ventas"
  },
  {
    "fecha": "2024-01-20",
    "monto": 500000,
    "categoria": "gastos"
  }
]
```

Se aceptan fechas en los formatos:

- `YYYY-MM-DD`
- `DD/MM/YYYY`
- `DD-MM-YYYY`

---

## Endpoints principales

| Método | Endpoint | Descripción |
|---------|----------|-------------|
| POST | `/api/upload/` | Carga un archivo para analizar. |
| GET | `/api/analysis/metricas` | Métricas generales. |
| GET | `/api/analysis/tendencias` | Tendencias por período. |
| GET | `/api/analysis/comparacion` | Comparación entre meses. |
| GET | `/api/analysis/outliers` | Detección de anomalías. |
| GET | `/api/analysis/completo` | Resumen completo del análisis. |
| GET | `/api/report/json` | Reporte en formato JSON. |

---

## Calidad del proyecto

- Pruebas automatizadas con **Pytest**.
- Integración continua mediante **GitHub Actions**.
- Validación de archivos y datos de entrada.
- Documentación automática con **Swagger**.
- Módulo de detección de anomalías con **Isolation Forest**.

Para ejecutar las pruebas:

```bash
pytest -v
```

---

## Mejoras futuras

- Persistencia de datos con PostgreSQL o SQLite.
- Autenticación de usuarios.
- Dashboard para visualizar resultados.
- Modelos predictivos basados en aprendizaje automático.

---

## Licencia

Este proyecto se distribuye bajo la licencia **MIT**.