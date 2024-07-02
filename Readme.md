# Compilador Antachawy

Este proyecto tiene como objetivo desarrollar un compilador para un nuevo lenguaje de programación denominado Antachawy, el cual utiliza el quechua como base para sus sintaxis y términos. Este esfuerzo busca reducir la brecha digital que existe actualmente en Perú, promoviendo el uso de tecnologías y lenguajes de programación accesibles para las comunidades quechuahablantes.

## Requisitos Previos

- Python 3.8 o superior
- pip (gestor de paquetes de Python)

## Creación y Activación de un Entorno Virtual

### En Windows

1. Abre una terminal (cmd, PowerShell, o Git Bash).
2. Navega al directorio del proyecto.
3. Crea un entorno virtual con el siguiente comando:

    ```bash
    python -m venv env
    ```

4. Activa el entorno virtual:

    ```bash
    .\env\Scripts\activate
    ```

### En Linux/MacOS

1. Abre una terminal.
2. Navega al directorio del proyecto.
3. Crea un entorno virtual con el siguiente comando:

    ```bash
    python3 -m venv env
    ```

4. Activa el entorno virtual:

    ```bash
    source env/bin/activate
    ```

## Instalación de Requerimientos

Una vez que el entorno virtual esté activado, instala los paquetes necesarios usando el archivo `requirements.txt`.

1. Asegúrate de estar en el directorio del proyecto y que el entorno virtual esté activado.
2. Ejecuta el siguiente comando:

    ```bash
    pip install -r requirements.txt
    ```

Esto instalará todas las dependencias necesarias para el proyecto.

## Ejecución del Compilador

Con el entorno virtual activado y las dependencias instaladas, puedes ejecutar el compilador con el siguiente comando:

### En Linux/MaxOS

    ```bash
    python3 src/main.py <inpust/archivo.awy>
    ```
### En Windows
    ```bash
    python src\\main.py <inputs\\archivo.awy>
    ```

Reemplaza el <archivo.awy> con el nombre del archivo fuente que deseas compilar.

## Contribuciones

¡Las contribuciones son bienvenidas! Siéntete libre de abrir issues o pull requests para mejorar el proyecto.