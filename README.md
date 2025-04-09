# 💵 Dólar Blue Always On Top (GTK App)

Una pequeña aplicación de escritorio hecha en Python que muestra el valor actual del **Dólar Blue** en Argentina. La ventana se mantiene siempre visible y actualiza los datos automáticamente cada 30 segundos.

## 🖥️ Características

- Muestra la cotización de compra y venta del dólar blue  
- Se actualiza automáticamente cada 30 segundos  
- Ventana flotante que se mantiene por encima de otras  
- Etiqueta con la hora de la última actualización  
- Ligera, rápida y hecha con ❤️ por Santiago Sito

## 📦 Requisitos

- Python 3  
- GTK+ 3 (vía PyGObject)  
- `requests` (para obtener los datos desde la API)

### En Ubuntu o derivados

```bash
sudo apt update
sudo apt install python3-gi gir1.2-gtk-3.0
pip install requests
```

### 🚀 Ejecución

Cloná este repositorio y ejecutá la app con:

```bash
python3 dolar_blue_widget.py
```

Asegurate de que el archivo se llame dolar_blue_widget.py o adaptá el nombre del script si usás otro.

### 📡 Fuente de datos

La aplicación utiliza la API pública de [Bluelytics](https://www.bluelytics.com.ar/) para obtener los valores actuales del dólar blue en Argentina.

### 🛠️ Tecnologías usadas

Python 3

GTK+ 3 (vía PyGObject)

API REST (requests)

## 🧠 Autor

Desarrollado por Santiago Sito – ideas, mejoras o forks son bienvenidos ✨
