# Reflexión y transmisión en la ventana de un láser infrarrojo

Proyecto programado de Electromagnetismo II (FS0820), UCR.
Natalia Quesada Fallas.

## Qué hace el código

El archivo `reflexion_ventana.py` estudia una onda de luz de 20 µm que llega de frente a una ventana de cinco materiales distintos (KRS-5, ZnSe, CsI, KBr y CaF2).

Para cada material:

- Calcula cuánta luz se refleja y cuánta se transmite en la cara de entrada y en la de salida de la ventana.
- Calcula cuánta luz se pierde en total al atravesar la ventana.
- Imprime estos resultados en pantalla.

Además guarda en la carpeta `figuras/`:

- `campos_entrada.png`: las ondas en la cara de entrada para los cinco materiales.
- `campos_salida.png`: las ondas en la cara de salida para los cinco materiales.
- `R_T_vs_n2.png`: la luz reflejada y transmitida según el índice de refracción.
- `animacion.gif`: las ondas moviéndose en el tiempo para los cinco materiales.

## Cómo correrlo

Se necesita Python con `numpy` y `matplotlib`. Si no los tiene instalados:

```
pip install numpy matplotlib
```

Luego, en la carpeta del proyecto:

```
python reflexion_ventana.py
```
