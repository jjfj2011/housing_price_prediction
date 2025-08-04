# 🏠 Predicción del Precio de Viviendas en California

Este repositorio alberga un proyecto enfocado en la predicción de precios de viviendas en California, utilizando variables socioeconómicas y geográficas. El modelo optimizado más eficaz ha sido implementado en Streamlit, permitiendo la estimación del precio de una vivienda mediante el ingreso de valores en cada característica.

## 🔗 Enlaces del Proyecto

- 📓 **Notebook en Google Colab (EDA + Modelado):** [Ver notebook aquí](https://colab.research.google.com/drive/1aNXNHcN_aHUakwLCZPjs01qM2UhueYVl?usp=sharing)
- 🌐 **Aplicación desplegada (Streamlit App):** [Ver app aquí](https://prediccion-precios-viviendas.streamlit.app/)

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

- Modelos desarrollados: **XGBoost** y **LightGBM**.
- Selección de hiperparámetros usando **GridSearchCV**.

✅ **Mejor modelo encontrado**

- **Algoritmo:** LightGBM Regressor (seleccionado mediante GridSearchCV con validación cruzada 5-fold)
- **Mejores hiperparámetros encontrados:**
  - `learning_rate`: 0.1
  - `max_depth`: 7
  - `n_estimators`: 300
- **Tiempo de entrenamiento:** ~0.82 minutos

✅ **Métricas de rendimiento**

- **RMSE del modelo optimizado:** \$44,447.89

✅ **Despliegue**

- Creación de una aplicación con **Streamlit** para que el usuario ingrese los valores de cada feature y obtenga:
  - Precio estimado con visualización gauge.
  - Mapa interactivo con Folium indicando la ubicación y precio.
  - Tabla resumen de las características ingresadas.

---

## 📊 Resultados Obtenidos

- El modelo puede predecir precios de viviendas con un RMSE promedio cercano a **\$44,448**, demostrando un buen desempeño para una primera implementación.
- Gráficos de distribución de precios, correlación y scatterplots permiten entender los factores clave que influyen en el precio.

---

## 💻 Ejecución de la App

### ▶️ Requisitos

- Python 3.12.2
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

![image](https://github.com/user-attachments/assets/25061830-598c-4c39-baee-8c63a5d1f697)


### 📈 Ejemplo de predicción y gráfico gauge

![image](https://github.com/user-attachments/assets/9339891b-0a8a-4cae-aac2-129ccd7235ca)


### 🌍 Mapa de la ubicación de la vivienda

![image](https://github.com/user-attachments/assets/65a90ae0-69af-4e16-b5a6-095ed6826526)



---

## 👨‍💼 Autor

**Frans Benavides**

📧 [jjfj2011@gmail.com]

💼 [www.linkedin.com/in/frans-benavides]
