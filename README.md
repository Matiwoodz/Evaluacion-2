# 📚 Scripts de Automatización y Geolocalización

Este repositorio contiene dos scripts en Python que automatizan tareas relacionadas con APIs:  
uno para **gestionar libros en una biblioteca** y otro para **obtener rutas y coordenadas geográficas**.

---

## 🧩 1. listado.py — Generador y Listado de Libros

Este script genera de forma automática 50 libros con datos aleatorios (título, autor e ISBN)  
y los envía a una API REST de biblioteca para almacenarlos.

### 🚀 Funcionalidades
- Crea múltiples libros con datos generados aleatoriamente.
- Envía cada registro a un endpoint remoto usando `requests`.
- Obtiene y muestra la lista completa de libros registrados en formato JSON.
- Muestra el total de libros en la biblioteca.

### 🛠️ Requisitos
- Python 3.x  
- Librerías:  
  ```bash
  pip install requests
# 🌍 geo.py — Buscador de Rutas con GraphHopper API

`geo.py` es un script interactivo en **Python** que utiliza la API de **GraphHopper** para realizar búsquedas geográficas y calcular rutas entre dos ubicaciones.  
Permite elegir distintos tipos de transporte y entrega información detallada del recorrido, incluyendo **distancia, duración y pasos de navegación**.

---

## 🚗 Funcionalidades
- 🔍 **Geocodificación:** convierte nombres de lugares en coordenadas (latitud y longitud).  
- 🗺️ **Cálculo de rutas:** genera direcciones paso a paso entre origen y destino.  
- 🚙 **Perfiles disponibles:**  
  - `auto`  
  - `bicicleta`  
  - `a pie`  
- ⏱️ Muestra:
  - Distancia total del viaje.  
  - Duración estimada (horas, minutos, segundos).  
  - Instrucciones de ruta traducidas al español.  

---

## 🛠️ Requisitos
- **Python 3.x**  
- Librerías necesarias:
  ```bash
  pip install requests
