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
