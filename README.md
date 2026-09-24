# 🖼️ Conversión a Escala de Grises por Media Aritmética en Python

Este proyecto implementa la conversión de imágenes a escala de grises aplicando la **media aritmética** sobre los canales de color (BGR) utilizando **Python** y **OpenCV**[cite: 16, 17]. 

A diferencia del método ponderado estándar (`cv2.cvtColor`), este algoritmo extrae individualmente los canales Azul (B), Verde (G) y Rojo (R), calcula su promedio directo `(R + G + B) / 3` y genera una nueva imagen procesada en formato de enteros de 8 bits (`uint8`).

---

## 🚀 Características

- 🔍 **Verificación de Archivos:** Confirma la existencia y lectura correcta de cada imagen antes de procesarla para evitar errores en tiempo de ejecución (`if img is not None`)[cite: 16, 17].
- 📐 **Procesamiento Manual:** Descomposición de canales e implementación manual del promedio de color:
  $$\text{Gris} = \frac{R + G + B}{3}$$
- 💾 **Guardado Automático:** Guarda cada imagen procesada con el sufijo `_promedio.jpg`.
- 🖥️ **Visualización Interactiva:** Muestra el resultado en una ventana y espera la interacción del usuario para continuar con la siguiente imagen (`cv2.imshow` y `cv2.waitKey`)[cite: 17].

---

## 🛠️ Tecnologías Requeridas

- **Python 3.x**
- **OpenCV (`opencv-python`)**
- **NumPy**

---

## 📁 Estructura del Repositorio

```text
Grayscale-Conversion-via-Arithmetic-Mean-in-Python/
├── Grayscale.py    # Script principal con el algoritmo de conversión
├── img1.jpg        # Imagen de prueba 1
├── img2.jpg        # Imagen de prueba 2
└── img3.jpg        # Imagen de prueba 3
