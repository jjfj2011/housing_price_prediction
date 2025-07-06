# 🏠 Predicción del Precio de Viviendas en California

Este repositorio alberga un proyecto enfocado en la predicción de precios de viviendas en California, utilizando variables socioeconómicas y geográficas. El modelo optimizado más eficaz ha sido implementado en Streamlit, permitiendo la estimación del precio de una vivienda mediante el ingreso de valores en cada característica.

## 🔗 Enlaces del Proyecto

- 📓 **Notebook en Google Colab (EDA + Modelado):** [Ver notebook aquí](https://colab.research.google.com/drive/1aNXNHcN_aHUakwLCZPjs01qM2UhueYVl?usp=sharing)
- 🌐 **Aplicación desplegada (Streamlit App):** [Probar app aquí](https://prediccion-precios-viviendas.streamlit.app/)

---

## 🚀 Tabla de Contenido

- [🔍 Descripción del Proyecto](#-descripción-del-proyecto)
- [📂 Estructura del Repositorio](#-estructura-del-repositorio)
- [🧠 Algoritmos y Metodología](#-algoritmos-y-metodología)
- [📊 Resultados Obtenidos](#-resultados-obtenidos)
- [💻 Ejecución de la App](#-ejecución-de-la-app)
- [📸 Capturas de Pantalla](#-capturas-de-pantalla)
- [👨‍💼 Autor](#-autor)

---

## 🔍 Descripción del Proyecto

El objetivo es **predecir el precio de una vivienda en California** a partir de variables como:

- Ingreso medio de la zona (`Median Income`)
- Edad media de las casas (`Median Age`)
- Total de habitaciones y dormitorios
- Población y número de hogares
- Latitud y longitud
- Distancias a puntos de referencia: Costa, Los Ángeles, San Diego, San José y San Francisco

---

## 📂 Estructura del Repositorio

```
├── California_Houses.csv            # Dataset
├── app.py                           # Aplicación Streamlit para la predicción
├── modelo_lightgbm_optimizado.pkl   # Modelo entrenado y optimizado con LightGBM
├── requirements.txt                 # Dependencias del proyecto
└── README.md                        # Este archivo
```

---

## 🧠 Algoritmos y Metodología

✅ **Preprocesamiento de datos**

- Análisis exploratorio de datos (EDA) con gráficos para entender la distribución de precios y correlaciones.

✅ **Modelado**

- Modelos desarrollados: XGBoost y LightGBM.
- Selección de hiperparámetros usando **GridSearchCV**.

✅ **Mejor modelo encontrado**

- **Algoritmo:** LightGBM Regressor
- **Mejores hiperparámetros:**
  - `colsample_bytree`: 0.6
  - `max_depth`: 3
  - `subsample`: 1

✅ **Métricas de rendimiento**

- **RMSE del modelo optimizado:** \$44,747.70

✅ **Despliegue**

- Creación de una aplicación con **Streamlit** para que el usuario ingrese los valores de cada feature y obtenga:
  - Precio estimado con visualización gauge.
  - Mapa interactivo con Folium indicando la ubicación y precio.
  - Tabla resumen de las características ingresadas.

---

## 📊 Resultados Obtenidos

- El modelo puede predecir precios de viviendas con un RMSE promedio cercano a **\$44,748**, demostrando un buen desempeño para una primera implementación.
- Gráficos de distribución de precios, correlación y scatterplots permiten entender los factores clave que influyen en el precio.

---

## 💻 Ejecución de la App

### ▶️ Requisitos

- Python 3.8+
- Instalar dependencias:

```bash
pip install -r requirements.txt
```


### ▶️ Correr la aplicación

```bash
streamlit run app.py
```

La aplicación se abrirá en tu navegador predeterminado donde podrás ingresar los valores de las variables y visualizar la predicción.

---

## 📸 Capturas de Pantalla

### 🎯 Pantalla principal de la aplicación



### 📈 Ejemplo de predicción y gráfico gauge



### 🌍 Mapa de la ubicación de la vivienda




---

## 👨‍💼 Autor

**Frans Benavides**

📧 [jjfj2011@gmail.com]

💼 [www.linkedin.com/in/frans-benavides]
