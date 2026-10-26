# -*- coding: utf-8 -*-
"""
================================================================================
RESOLVER DE SERIES TRIGONOMÉTRICAS DE FOURIER Y ESPECTRO DE ARMÓNICAS (OFFLINE)
================================================================================
No requiere conexión a internet. Utiliza SymPy, NumPy y Matplotlib.

Librerías necesarias (instalar una única vez localmente en tu PC):
    pip install sympy numpy matplotlib
"""

import numpy as np
import sympy as sp
import matplotlib.pyplot as plt

def calcular_fourier(f_expr, t_var, t_a, t_b, num_armonicas=10):
    """
    Calcula coeficientes a0, an, bn, la forma compacta de armónicas (Cn, phi_n)
    y grafica la aproximación y los espectros.
    """
    n = sp.Symbol('n', integer=True, positive=True)
    T = t_b - t_a
    w0 = 2 * sp.pi / T

    print("=" * 70)
    print(" ANÁLISIS DE SERIE TRIGONOMÉTRICA DE FOURIER")
    print("=" * 70)
    print(f"• Función f(t)       : {f_expr}")
    print(f"• Intervalo de f(t)  : [{t_a}, {t_b}]")
    print(f"• Periodo (T)        : {T}")
    print(f"• Frecuencia w0      : {w0}")
    print("-" * 70)

    # -------------------------------------------------------------------------
    # 1. CÁLCULO SIMBÓLICO DE COEFICIENTES (a0, an, bn)
    # -------------------------------------------------------------------------
    print("\n1. COEFICIENTES SIMBÓLICOS DE FOURIER:")
    
    # Coeficiente a0 (Valor Medio / Componente DC)
    a0 = (1 / T) * sp.integrate(f_expr, (t_var, t_a, t_b))
    a0 = sp.simplify(a0)
    print(f"  a0 = {a0}")

    # Coeficiente an
    an = (2 / T) * sp.integrate(f_expr * sp.cos(n * w0 * t_var), (t_var, t_a, t_b))
    an = sp.simplify(an)
    print(f"  an = {an}")

    # Coeficiente bn
    bn = (2 / T) * sp.integrate(f_expr * sp.sin(n * w0 * t_var), (t_var, t_a, t_b))
    bn = sp.simplify(bn)
    print(f"  bn = {bn}")

    # Expresión analítica
    print("\n• Expresión trigonométrica de la serie:")
    print(f"  f(t) = {a0} + Sum[ ({an})*cos(n*{w0}*t) + ({bn})*sin(n*{w0}*t), {{n, 1, inf}} ]")

    # -------------------------------------------------------------------------
    # 2. CÁLCULO DE ARMÓNICAS (Forma Amplitud-Fase: C_n y phi_n)
    # -------------------------------------------------------------------------
    # Forma compacta: f(t) = a0 + sum( C_n * cos(n*w0*t - phi_n) )
    # Donde: C_n = sqrt(an^2 + bn^2),  phi_n = atan2(bn, an)
    print(f"\n2. TABLA DE ARMÓNICAS (Primeras {num_armonicas} armónicas):")
    print(f"{'n':<4} | {'a_n':<12} | {'b_n':<12} | {'Amplitud C_n':<15} | {'Fase phi_n (rad)':<18} | {'Fase phi_n (deg)':<18}")
    print("-" * 88)

    armonicas = []
    for i in range(1, num_armonicas + 1):
        try:
            an_val = float(an.subs(n, i).evalf())
        except Exception:
            an_val = 0.0

        try:
            bn_val = float(bn.subs(n, i).evalf())
        except Exception:
            bn_val = 0.0

        cn_val = np.hypot(an_val, bn_val)
        phi_rad = np.arctan2(bn_val, an_val)
        phi_deg = np.degrees(phi_rad)

        armonicas.append({
            'n': i,
            'an': an_val,
            'bn': bn_val,
            'Cn': cn_val,
            'phi_rad': phi_rad,
            'phi_deg': phi_deg
        })

        print(f"{i:<4} | {an_val:<12.5f} | {bn_val:<12.5f} | {cn_val:<15.5f} | {phi_rad:<18.5f} | {phi_deg:<18.2f}°")

    # -------------------------------------------------------------------------
    # 3. RECONSTRUCCIÓN Y GRAFICACIÓN
    # -------------------------------------------------------------------------
    t_a_num = float(sp.sympify(t_a).evalf())
    t_b_num = float(sp.sympify(t_b).evalf())
    T_num = float(sp.sympify(T).evalf())
    w0_num = float(sp.sympify(w0).evalf())
    a0_num = float(sp.sympify(a0).evalf())

    # Generar vector de tiempo para 3 periodos
    t_vec = np.linspace(t_a_num - T_num, t_b_num + T_num, 1200)

    # Función original periódica
    f_lambdified = sp.lambdify(t_var, f_expr, modules=['numpy'])
    t_mod = (t_vec - t_a_num) % T_num + t_a_num
    f_orig = f_lambdified(t_mod)

    # Evaluación de la serie
    def fourier_eval(t_arr, N_terms):
        f_sum = np.full_like(t_arr, a0_num, dtype=float)
        for i in range(1, N_terms + 1):
            an_i = armonicas[i-1]['an'] if i <= len(armonicas) else float(an.subs(n, i).evalf())
            bn_i = armonicas[i-1]['bn'] if i <= len(armonicas) else float(bn.subs(n, i).evalf())
            f_sum += an_i * np.cos(i * w0_num * t_arr) + bn_i * np.sin(i * w0_num * t_arr)
        return f_sum

    # Crear la figura con 3 subgráficas
    fig = plt.figure(figsize=(12, 9))
    fig.suptitle('Análisis de Serie de Fourier y Espectro de Armónicas', fontsize=14, fontweight='bold')

    # Gráfica 1: Reconstrucción de la Señal
    ax1 = plt.subplot(2, 1, 1)
    ax1.plot(t_vec, f_orig, 'k--', label='Función Original f(t)', alpha=0.6, linewidth=2)
    
    terminos_graficar = [1, 3, 5, min(10, num_armonicas)]
    colores = ['#e41a1c', '#377eb8', '#4daf4a', '#984ea3']
    for idx, N in enumerate(terminos_graficar):
        f_app = fourier_eval(t_vec, N)
        ax1.plot(t_vec, f_app, label=f'Fourier (N={N} armónicas)', color=colores[idx % len(colores)], linewidth=1.5)

    ax1.set_title('Aproximación por Series de Fourier')
    ax1.set_xlabel('Tiempo (t)')
    ax1.set_ylabel('f(t)')
    ax1.grid(True, linestyle=':', alpha=0.7)
    ax1.legend(loc='upper right')

    # Gráfica 2: Espectro de Amplitud (C_n vs n)
    ax2 = plt.subplot(2, 2, 3)
    ns = [item['n'] for item in armonicas]
    cns = [item['Cn'] for item in armonicas]
    
    ax2.stem(ns, cns, linefmt='b-', markerfmt='bo', basefmt='r-')
    ax2.set_title('Espectro de Amplitud (C_n vs n)')
    ax2.set_xlabel('Número de Armónica (n)')
    ax2.set_ylabel('Amplitud C_n')
    ax2.set_xticks(ns)
    ax2.grid(True, linestyle=':', alpha=0.7)

    # Gráfica 3: Espectro de Fase (phi_n vs n en grados)
    ax3 = plt.subplot(2, 2, 4)
    phis = [item['phi_deg'] for item in armonicas]
    
    ax3.stem(ns, phis, linefmt='g-', markerfmt='go', basefmt='r-')
    ax3.set_title('Espectro de Fase (phi_n en grados vs n)')
    ax3.set_xlabel('Número de Armónica (n)')
    ax3.set_ylabel('Fase phi_n (°)')
    ax3.set_xticks(ns)
    ax3.grid(True, linestyle=':', alpha=0.7)

    plt.tight_layout(rect=[0, 0, 1, 0.96])
    plt.show()


if __name__ == "__main__":
    t = sp.Symbol('t', real=True)

    # Ejemplo del cuaderno de referencia: Rectificador de media onda en [0, 2*pi]
    f_ejemplo = sp.Piecewise(
        (sp.sin(t), (t >= 0) & (t < sp.pi)),
        (0, (t >= sp.pi) & (t < 2 * sp.pi))
    )
    
    # Ejecutar análisis para 10 armónicas
    calcular_fourier(f_expr=f_ejemplo, t_var=t, t_a=0, t_b=2*sp.pi, num_armonicas=10)