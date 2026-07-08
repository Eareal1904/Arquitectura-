import matplotlib.pyplot as plt
# Importamos las funciones específicas desde el paquete que creamos
from utils.projectile_functions import calcular_trayectoria, calcular_con_resistencia

def main():
    print("--- SIMULACIÓN DEL LANZAMIENTO DEL COHETE ---")
    
    # 1. Parámetros iniciales
    v0 = 50.0       # Velocidad inicial en m/s
    angulo = 45.0   # Ángulo de lanzamiento en grados
    masa = 3.4      # Masa del cohete en kg
    c = 0.005       # Coeficiente de resistencia del aire
    
    print(f"Lanzando a {v0} m/s con un ángulo de {angulo}°...")

    # 2. Llamada a las funciones de nuestro módulo 'utils'
    x_ideal, y_ideal = calcular_trayectoria(v0, angulo)
    x_real, y_real = calcular_con_resistencia(v0, angulo, c, masa)
    
    # 3. Generación de la gráfica requerida por el taller
    plt.figure(figsize=(10, 5))
    plt.plot(x_ideal, y_ideal, label="Trayectoria Ideal (Sin arrastre)", linestyle="--")
    plt.plot(x_real, y_real, label="Trayectoria Real (Con resistencia)", color="red")
    
    plt.title("Análisis del Movimiento de Proyectiles - Taller Python")
    plt.xlabel("Distancia Horizontal (m)")
    plt.ylabel("Altura (m)")
    plt.grid(True)
    plt.legend()
    
    # Guardamos la gráfica como imagen para poder enlazarla en el reporte Org
    plt.savefig("trayectoria_cohete.png")
    print("¡Simulación completada con éxito! Gráfica guardada como 'trayectoria_cohete.png'.")

if __name__ == "__main__":
    main()
