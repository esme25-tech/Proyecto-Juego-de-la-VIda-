# Proyecto: Juego de la Vida 

## Resumen

Esta es la explicación de cómo se organizó, cómo se desarrolló y cómo funciona una aplicación web interactiva basada en el Juego de la Vida.
El proyecto se realizó en equipo utilizando Python y se organizó en tres partes principales: una encargada de las reglas matemáticas y los cambios de las células, otra dedicada al diseño de la interfaz visual y una última, llamada `main.py`, que conecta todas las partes para que la aplicación funcione correctamente.
El objetivo principal del proyecto es convertir un modelo matemático en una aplicación web fácil de usar y entender. De esta manera, los usuarios pueden observar cómo cambian y evolucionan diferentes patrones en tiempo real, además de controlar la simulación mediante las herramientas interactivas que ofrece Streamlit.

## Introducción problema

La mayoría de las versiones del Juego de la Vida funcionan únicamente en la consola de comandos y muestran los resultados mediante caracteres de texto. Esto presenta algunas dificultades:

* **Poca claridad visual:** Al utilizar solo texto, es más difícil observar y comprender los patrones que se forman en el tablero.

* **Poca interacción:** Los usuarios no pueden controlar fácilmente la simulación con opciones como iniciar, pausar o reiniciar.

* **Dificultad para ejecutarlo:** En muchos casos, es necesario instalar y configurar programas o herramientas de desarrollo para poder utilizarlo.

Este proyecto busca solucionar estos problemas mediante la creación de una aplicación web fácil de usar, que muestre los resultados de forma clara y permita a los usuarios interactuar con la simulación de manera sencilla.

## Introducción objetivo

### Objetivo general

Crear una aplicación web interactiva que permita simular el funcionamiento del Juego de la Vida de Conway utilizando Python, NumPy y Streamlit. Para ello, se busca organizar el código en diferentes partes y trabajar de manera colaborativa utilizando herramientas de control de versiones.

### Objetivos particulares

* Crear un sistema que aplique las reglas matemáticas del Juego de la Vida de manera eficiente, utilizando matrices de NumPy y permitiendo que los bordes del tablero se conecten entre sí.

* Diseñar una interfaz visual sencilla, ordenada y adaptable, utilizando HTML y CSS dentro de Streamlit.

* Agregar controles que permitan al usuario iniciar, pausar y reiniciar la simulación sin que la aplicación deje de responder.

* Documentar el proceso de creación del proyecto y organizar el código en un repositorio de GitHub para que otras personas puedan revisarlo y ejecutarlo fácilmente.

## Solucion y evidencia

La solución consiste en organizar el programa en tres partes principales para que el código sea más fácil de entender, modificar y mantener:

1. **`logica.py` (Funcionamiento del juego):** Se encarga de crear el tablero y aplicar las reglas del Juego de la Vida. También cuenta las células vecinas de cada casilla y utiliza una técnica que conecta los bordes del tablero, haciendo que funcione como si fuera infinito. Además, determina cuándo una célula vive, muere o nace.

2. **`interfaz.py` (Diseño visual):** Se encarga de cómo se ve la aplicación web. Aquí se diseña la página, se muestran las reglas del juego en un panel desplegable, se crea el tablero con casillas de diferentes colores y se agregan los botones para controlar la simulación.

3. **`main.py` (Archivo principal):** Es el encargado de conectar los otros dos archivos. También utiliza una función de Streamlit llamada `st.session_state` para recordar el estado de la simulación y actualizar el tablero conforme avanzan las generaciones.

**Puedes checar los siguientes links:**

* [Repositorio en GitHub](https://github.com/esme25-tech/Proyecto-Juego-de-la-VIda-)

* [Aplicación en Streamlit](https://uappbh3wmicbdelf7wekxu.streamlit.app/)

## Conclusiones

### Conclusiones generales

Con el desarrollo de este proyecto se comprobó que es posible convertir conceptos matemáticos complejos en una aplicación web interactiva y fácil de utilizar mediante herramientas como Python y Streamlit.
Además, dividir el programa en diferentes archivos facilitó el trabajo en equipo, ya que cada integrante pudo encargarse de una parte del proyecto, separando el funcionamiento del juego de su diseño visual.

### Conclusiones particulares

* **Funcionamiento del juego:** El uso de NumPy permitió realizar los cálculos de las células de manera rápida y eficiente, sin afectar el funcionamiento de la aplicación.

* **Interactividad y control:** Gracias al uso de `st.session_state`, se logró mantener el estado de la simulación y agregar opciones para iniciar, pausar y reiniciar el juego sin que la página se quedara congelada.

* **Trabajo en equipo:** El uso de herramientas de GitHub, como las ramas (branches), los problemas (issues) y las solicitudes de cambios (pull requests), permitió organizar mejor el trabajo, compartir los avances y unir el código de cada integrante de manera ordenada.

## Reproductibilidad

### Dependencias

Para poder ejecutar este proyecto en tu computadora, necesitas tener instalados los siguientes programas y bibliotecas:

* **Python (versión 3.8 o superior):** Es el lenguaje de programación utilizado para desarrollar el proyecto.

* **NumPy:** Es una biblioteca que permite trabajar con matrices y realizar cálculos de manera rápida.

* **Streamlit:** Es una herramienta que permite crear la página web interactiva donde se muestra el Juego de la Vida.

### Instalación y ejecución

Sigue estos pasos para descargar y ejecutar el proyecto en tu computadora:

1. **Descargar el proyecto**

   Abre la terminal o consola de tu computadora y escribe el siguiente comando para descargar los archivos desde GitHub:

   ```
   git clone https://github.com/esme25-tech/Proyecto-Juego-de-la-Vida-.git
   
   ```

2. **Entrar a la carpeta del proyecto**

   Una vez descargado, accede a la carpeta con el siguiente comando:

   ```
   cd Proyecto-Juego-de-la-Vida-
   
   ```

3. **Instalar las bibliotecas necesarias**

   Escribe el siguiente comando para instalar NumPy y Streamlit, que son necesarias para que el programa funcione:

   ```
   pip install streamlit numpy
   
   ```

4. **Ejecutar la aplicación**

   Para iniciar el programa, escribe el siguiente comando:

   ```
   streamlit run main.py
   
   ```

5. **Abrir el programa**

   Después de ejecutar el comando, se abrirá una pestaña en tu navegador web con la aplicación del Juego de la Vida. Desde ahí podrás visualizar el tablero y comenzar a utilizar sus funciones interactivas.
