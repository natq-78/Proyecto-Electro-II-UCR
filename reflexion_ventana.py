# Reflexion y transmision de una onda plana a incidencia normal
# Proyecto programado - FS0820 Electromagnetismo II
# Natalia Quesada Fallas
#
# Formulas de Griffiths (2017), seccion 9.3.2
# Se supone que los medios son transparentes y no magneticos

import numpy as np
import matplotlib.pyplot as plt
import os

# Carpeta donde se guardan las figuras
if not os.path.exists("figuras"):
    os.mkdir("figuras")


# ----- Datos -----

# Longitud de onda en el vacio (en micrometros)
lam0 = 20

# Materiales de la ventana y sus indices de refraccion (Crystran)
nombres = ["KRS-5", "ZnSe", "CsI", "KBr", "CaF2"]
indices = [2.3409, 2.3278, 1.7276, 1.4929, 1.3161]

# Posiciones a la izquierda (medio 1) y a la derecha (medio 2) de la interfaz
z1 = np.linspace(-60, 0, 600)
z2 = np.linspace(0, 60, 600)


# ----- Tabla de resultados -----

print("Material   cara      r        t        R        T      R+T")

perdidas = []

for i in range(len(nombres)):
    n = indices[i]

    # Cara de entrada: del vacio (n1 = 1) al material (n2 = n)
    n1 = 1
    n2 = n
    r = (n1 - n2) / (n1 + n2)
    t = 2 * n1 / (n1 + n2)
    R = r**2
    T = (n2 / n1) * t**2
    print(nombres[i], "  entrada", round(r, 3), " ", round(t, 3), " ", round(R, 3), " ", round(T, 3), " ", round(R + T, 3))

    # Cara de salida: del material (n1 = n) al vacio (n2 = 1)
    n1 = n
    n2 = 1
    r = (n1 - n2) / (n1 + n2)
    t = 2 * n1 / (n1 + n2)
    R = r**2
    T = (n2 / n1) * t**2
    print(nombres[i], "  salida ", round(r, 3), " ", round(t, 3), " ", round(R, 3), " ", round(T, 3), " ", round(R + T, 3))

    # Perdida de la ventana completa (dos caras, sumando los rebotes internos)
    T_ventana = (1 - R) / (1 + R)
    perdida = 1 - T_ventana
    perdidas.append(perdida)

print()
print("Perdida de la ventana completa:")
for i in range(len(nombres)):
    print(nombres[i], ":", round(100 * perdidas[i], 1), "%")

# Comprobacion con el ejemplo de Griffiths (aire a vidrio): R = 0.04 y T = 0.96
n1 = 1
n2 = 1.5
r = (n1 - n2) / (n1 + n2)
t = 2 * n1 / (n1 + n2)
print()
print("Aire a vidrio: R =", round(r**2, 3), " T =", round((n2 / n1) * t**2, 3))


# ----- Figuras 1 y 2: campos en las caras de entrada y salida -----

for cara in ["entrada", "salida"]:

    plt.figure(figsize=(12, 10))

    for i in range(len(nombres)):
        n = indices[i]

        if cara == "entrada":
            n1 = 1
            n2 = n
        else:
            n1 = n
            n2 = 1

        r = (n1 - n2) / (n1 + n2)
        t = 2 * n1 / (n1 + n2)
        R = r**2
        T = (n2 / n1) * t**2

        # numeros de onda en cada medio
        k1 = 2 * np.pi * n1 / lam0
        k2 = 2 * np.pi * n2 / lam0

        # campos electricos en t = 0
        E_inc = np.cos(k1 * z1)
        E_ref = r * np.cos(-k1 * z1)
        E_tra = t * np.cos(k2 * z2)

        plt.subplot(3, 2, i + 1)
        plt.plot(z1, E_inc, "--", color="tab:blue", label="incidente")
        plt.plot(z1, E_ref, "--", color="tab:red", label="reflejada")
        plt.plot(z1, E_inc + E_ref, color="black", linewidth=2, label="total en el medio 1")
        plt.plot(z2, E_tra, color="tab:green", linewidth=2, label="transmitida")
        plt.axvline(0, color="black")
        plt.axvspan(0, 60, color="lightsteelblue", alpha=0.4)
        plt.xlim(-60, 60)
        plt.ylim(-2.2, 2.2)
        plt.xlabel("z (µm)")
        plt.ylabel("E / E0")
        plt.title(nombres[i] + ":  r = " + str(round(r, 3)) + ",  t = " + str(round(t, 3))
                  + ",  R = " + str(round(R, 3)) + ",  T = " + str(round(T, 3)), fontsize=10)
        plt.grid(alpha=0.3)

    # la leyenda va en el espacio vacio que queda en la esquina
    plt.subplot(3, 2, 6)
    plt.plot([], [], "--", color="tab:blue", label="incidente")
    plt.plot([], [], "--", color="tab:red", label="reflejada")
    plt.plot([], [], color="black", linewidth=2, label="total en el medio 1")
    plt.plot([], [], color="tab:green", linewidth=2, label="transmitida")
    plt.axis("off")
    plt.legend(loc="center", fontsize=13)

    plt.tight_layout()
    plt.savefig("figuras/campos_" + cara + ".png", dpi=200)
    plt.close()


# ----- Figura 3: R y T en funcion del indice -----

n2 = np.linspace(1, 4, 300)
R = ((1 - n2) / (1 + n2))**2
T = 4 * n2 / (1 + n2)**2
perdida = 1 - (1 - R) / (1 + R)

plt.figure(figsize=(8, 4.5))
plt.plot(n2, R, color="tab:red", linewidth=2, label="R (una cara)")
plt.plot(n2, T, color="tab:green", linewidth=2, label="T (una cara)")
plt.plot(n2, R + T, "--", color="black", label="R + T")
plt.plot(n2, perdida, color="tab:orange", linewidth=2, label="pérdida de la ventana")

# puntos de los materiales
for i in range(len(nombres)):
    plt.plot(indices[i], perdidas[i], "o", color="tab:orange")

plt.text(1.95, 0.30, "KRS-5 y ZnSe")
plt.text(1.66, 0.17, "CsI")
plt.text(1.42, 0.11, "KBr")
plt.text(1.18, 0.07, "CaF2")

plt.xlabel("n2  (con n1 = 1)")
plt.ylabel("fracción de la potencia incidente")
plt.ylim(0, 1.05)
plt.grid(alpha=0.3)
plt.legend(loc="center left")
plt.tight_layout()
plt.savefig("figuras/R_T_vs_n2.png", dpi=200)
plt.close()

print()
print("Figuras guardadas en la carpeta figuras")


# ----- Animacion de los 5 materiales (cara de entrada) -----
# Se hace una sola figura con un panel por material y se guarda como gif

from matplotlib.animation import FuncAnimation

fig = plt.figure(figsize=(12, 10))

# listas para guardar las lineas de cada panel y poder moverlas despues
lineas_inc = []
lineas_ref = []
lineas_tot = []
lineas_tra = []
lista_r = []
lista_t = []
lista_k1 = []
lista_k2 = []

for i in range(len(nombres)):
    n1 = 1
    n2 = indices[i]
    r = (n1 - n2) / (n1 + n2)
    t = 2 * n1 / (n1 + n2)

    lista_r.append(r)
    lista_t.append(t)
    lista_k1.append(2 * np.pi * n1 / lam0)
    lista_k2.append(2 * np.pi * n2 / lam0)

    plt.subplot(3, 2, i + 1)
    l1, = plt.plot(z1, np.zeros(len(z1)), "--", color="tab:blue")
    l2, = plt.plot(z1, np.zeros(len(z1)), "--", color="tab:red")
    l3, = plt.plot(z1, np.zeros(len(z1)), color="black", linewidth=2)
    l4, = plt.plot(z2, np.zeros(len(z2)), color="tab:green", linewidth=2)
    lineas_inc.append(l1)
    lineas_ref.append(l2)
    lineas_tot.append(l3)
    lineas_tra.append(l4)

    plt.axvline(0, color="black")
    plt.axvspan(0, 60, color="lightsteelblue", alpha=0.4)
    plt.xlim(-60, 60)
    plt.ylim(-2.2, 2.2)
    plt.xlabel("z (µm)")
    plt.ylabel("E / E0")
    plt.title("Vacío a " + nombres[i])
    plt.grid(alpha=0.3)

# leyenda en el panel que sobra
plt.subplot(3, 2, 6)
plt.plot([], [], "--", color="tab:blue", label="incidente")
plt.plot([], [], "--", color="tab:red", label="reflejada")
plt.plot([], [], color="black", linewidth=2, label="total en el medio 1")
plt.plot([], [], color="tab:green", linewidth=2, label="transmitida")
plt.axis("off")
plt.legend(loc="center", fontsize=13)
plt.tight_layout()


# esta funcion cambia las ondas en cada paso de tiempo
def actualizar(paso):
    wt = 2 * np.pi * paso / 40     # 40 pasos por periodo
    for i in range(len(nombres)):
        E_inc = np.cos(lista_k1[i] * z1 - wt)
        E_ref = lista_r[i] * np.cos(-lista_k1[i] * z1 - wt)
        E_tra = lista_t[i] * np.cos(lista_k2[i] * z2 - wt)
        lineas_inc[i].set_ydata(E_inc)
        lineas_ref[i].set_ydata(E_ref)
        lineas_tot[i].set_ydata(E_inc + E_ref)
        lineas_tra[i].set_ydata(E_tra)


animacion = FuncAnimation(fig, actualizar, frames=40, interval=50)

# se guarda el gif en la carpeta de figuras
animacion.save("figuras/animacion.gif", writer="pillow", fps=20)
print("Animacion guardada en figuras/animacion.gif")

# se cierra la figura para que no se muestre en pantalla
plt.close()
