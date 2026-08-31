# -*- coding: utf-8 -*-
"""
Created on Wed Jan 10 12:33:26 2024

@author: jose ochoa
"""

import cv2

imagenes = ["img1", "img2", "img3"]

for ruta in imagenes:
    img = cv2.imread(f"{ruta}.jpg")

    # Asegurarse de que la imagen existe antes de procesar
    if img is not None:
        r = img[:, :, 2]
        g = img[:, :, 1]
        b = img[:, :, 0]

        n_img = (r + g + b) / 3
        n_img = n_img.astype('uint8')  # uint8 es el formato estándar para imágenes

        cv2.imwrite(f"{ruta}_promedio.jpg", n_img)

        # Mostrar la imagen en ventana
        cv2.imshow(f"Resultado {ruta}", n_img)
        cv2.waitKey(0)  # Espera a que presiones una tecla para continuar

cv2.destroyAllWindows()