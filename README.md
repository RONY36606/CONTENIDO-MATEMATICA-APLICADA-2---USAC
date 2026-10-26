# Calculadoras de Series y Transformadas de Fourier 

Este repositorio contiene un conjunto de herramientas y calculadoras interactivas desarrolladas en Python para el análisis, cálculo y visualización de Series de Fourier y Transformadas de Fourier.

El proyecto combina cálculo simbólico, análisis numérico y visualización gráfica interactiva para facilitar el estudio de señales y procesamiento de frecuencias.

# Tecnologías Principales

SymPy: Para el cálculo simbólico exacto de las series, transformadas e integrales.

NumPy & SciPy: Para la manipulación numérica de arreglos y algoritmos eficientes de FFT (Fast Fourier Transform).

Matplotlib: Para la graficación y representación visual de señales en el dominio del tiempo y la frecuencia.

Jupyter Notebook: Para la ejecución interactiva del código.

## Guía de Instalación

Sigue estos pasos para clonar el repositorio, crear un entorno virtual e instalar todas las dependencias necesarias según tu sistema operativo.

# Requisitos Previos

Asegúrate de tener instalado Python 3.9 o superior en tu sistema.

Puedes comprobar tu versión de Python corriendo en la terminal:

python --version   # En Windows

python3 --version  # En Linux


## Paso 1: Clonar el Repositorio

Abre la terminal o símbolo del sistema y ejecuta:

git clone https://github.com/RONY36606/CONTENIDO-MATEMATICA-APLICADA-2---USAC.git
cd tu-repositorio


## Paso 2: Crear e Instalar el Entorno Virtual

Es recomendable utilizar un entorno virtual para aislar las dependencias de este proyecto.

## En Windows

Crear el entorno virtual:

python -m venv venv


Activar el entorno virtual:

Desde PowerShell:

.\venv\Scripts\Activate.ps1


(Si obtienes un error de políticas de ejecución, ejecuta antes: Set-ExecutionPolicy Unrestricted -Scope Process)

Desde Símbolo del Sistema (CMD):

.\venv\Scripts\activate.bat


(Sabrás que está activo porque aparecerá (venv) al inicio de la línea de comandos).

## En Linux y/o macOS

Crear el entorno virtual:
(Si no tienes el paquete venv instalado en Linux Ubuntu/Debian, ejecuta primero: sudo apt install python3-venv)

python3 -m venv venv


Activar el entorno virtual:

source venv/bin/activate


Paso 3: Instalar las Dependencias

Con el entorno virtual activado, actualiza pip e instala las librerías indicadas en el archivo requirements.txt:

# Actualizar pip
python -m pip install --upgrade pip

# Instalar librerías del proyecto
pip install -r requirements.txt


Uso del Proyecto

Una vez completada la instalación, puedes utilizar las calculadoras mediante Jupyter Notebooks o ejecutando scripts directos de Python.

Opción 1: Abrir con Jupyter Notebook / JupyterLab

Si los scripts están estructurados como notebooks (.ipynb):

jupyter notebook


o

jupyter lab


Esto abrirá una pestaña en tu navegador web donde podrás seleccionar y ejecutar interactiva cada calculadora.

Opción 2: Ejecutar Scripts de Python

Si vas a ejecutar archivos con extensión .py:

python nombre_del_script.py


Contribuciones y Notas

Si deseas añadir más algoritmos, filtros o tipos de transformadas, ¡las contribuciones son bienvenidas! Puedes abrir un Pull Request o reportar problemas en la sección de Issues.

# CONTENIDO-MATEMATICA-APLICADA-2---USAC
