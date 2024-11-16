import matplotlib.pyplot as plt

def dibujar_suseth():
    fig, ax = plt.subplots(figsize=(8, 6))
    
    # Configuración general
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 6)
    ax.axis("off")  # Ocultar los ejes
    
    # Dibujar "S"
    s_x = [1, 1.5, 2, 2.5, 1.5, 1]
    s_y = [5, 5.5, 5, 4.5, 4, 4.5]
    ax.plot(s_x, s_y, color="blue", linewidth=3)
    
    # Dibujar "U"
    u_x = [3, 3, 4, 4]
    u_y = [5.5, 4, 4, 5.5]
    ax.plot(u_x, u_y, color="red", linewidth=3)
    
    # Dibujar "S"
    ax.plot([5, 5.5, 6, 6.5, 5.5, 5], [5, 5.5, 5, 4.5, 4, 4.5], color="green", linewidth=3)
    
    # Dibujar "E"
    ax.plot([7, 7, 8, 7, 8, 7], [5.5, 4, 4, 4.75, 4.75, 5.5], color="purple", linewidth=3)
    
    # Dibujar "T"
    ax.plot([9, 10], [5.5, 5.5], color="orange", linewidth=3)
    ax.plot([9.5, 9.5], [5.5, 4], color="orange", linewidth=3)
    
    # Dibujar "H"
    ax.plot([11, 11], [5.5, 4], color="brown", linewidth=3)
    ax.plot([12, 12], [5.5, 4], color="brown", linewidth=3)
    ax.plot([11, 12], [4.75, 4.75], color="brown", linewidth=3)
    
    # Mostrar el dibujo
    plt.title("Nombre: Suseth", fontsize=16)
    plt.show()

# Llamar a la función
dibujar_suseth()
