import numpy as np

def calcular_trayectoria(v0, angulo, g=9.81):
    """
    Calcula las posiciones X e Y de un proyectil sin resistencia del aire.
    """
    theta = np.radians(angulo)
    # Tiempo de vuelo estimado
    t_vuelo = (2 * v0 * np.sin(theta)) / g
    t = np.linspace(0, t_vuelo, 100)
    
    # Ecuaciones de posición
    x = v0 * np.cos(theta) * t
    y = v0 * np.sin(theta) * t - 0.5 * g * t**2
    
    return x, y

def calcular_con_resistencia(v0, angulo, c, m, dt=0.01):
    """
    Calcula la trayectoria usando el método de Euler con resistencia del aire (F = -c*v).
    """
    theta = np.radians(angulo)
    vx = v0 * np.cos(theta)
    vy = v0 * np.sin(theta)
    x, y = [0.0], [0.0]
    
    while y[-1] >= 0:
        v = np.sqrt(vx**2 + vy**2)
        # Aceleraciones con arrastre
        ax = -(c / m) * v * vx
        ay = -9.81 - (c / m) * v * vy
        
        # Actualización de posiciones y velocidades (Euler)
        vx += ax * dt
        vy += ay * dt
        x.append(x[-1] + vx * dt)
        y.append(y[-1] + vy * dt)
        
    return np.array(x), np.array(y)
