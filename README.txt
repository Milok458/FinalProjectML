Proyecto Final Aprendizaje Automático

Este proyecto consta de tres secciones de código, las cuales están separadas según su funcionalidad:
    - Limpieza de datos
    - Creación y entrenamiento del modelo
    - Despliegue

A continuación, se describe como hacer uso de cada una de las secciones de este proyecto,
así como documentar sus funcionalidades.
------------------------------------------------------------------------------------------------------------------------
Limpieza de Datos

La sección de limpieza de datos cuenta con el dataset de Star,
así como un notebook con el algoritmo que se encarga de formatear el dataset para la siguiente fase.

Este programa requiere que el dataset "Star99999_raw.csv" Se encuentre dentro de la misma carpeta
y genera un archivo se salida llamado "CleanStar.csv".
------------------------------------------------------------------------------------------------------------------------
Creación y Entrenamiento del Modelo

Esta sección cuenta con el dataset limpio "CleanStar",
un documento de python utilizado para hacer pruebas con los modelos
y un notebook el cual se encarga de generar el modelo final
y el Standard Scaler de datos utilizados en la última fase del proyecto.

Este programa requiere que "CleanStar" se encuentre en su misma carpeta
y genera dos archivos de salida, "NeuralNet.joblib" y "Scaler.joblib"
------------------------------------------------------------------------------------------------------------------------
Despliegue

Esta sección cuenta con tres documentos, los modelos de el Scaler y la red neuronal, así como un programa que funge como
prototipo de producto para el clasificador de estrellas que funciona con nuestro modelo previamente entrenado.

Este programa requiere estar en la misma carpeta que  "NeuralNet.joblib" y "Scaler.joblib".
Este programa cuenta con una interfaz gráfica que permite al usuario clasificar una estrella según sus datos.
El programa requiere de un input de las variables Vmag, Plx y B-V, ya que este calcula de manera independiente
la variable MagA y la clasifica según estos cuatro números.
------------------------------------------------------------------------------------------------------------------------