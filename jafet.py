import matplotlib.pyplot as plt

def dibujar_jafet():
    fig, ax = plt.subplots(figsize=(8, 6))
    
    # Configuración general
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 6)
    ax.axis("off")  # Ocultar los ejes
    
    # Dibujar "J"
    ax.plot([1, 1, 2], [5.5, 4, 4], color="blue", linewidth=3)
    ax.plot([2, 2], [5.5, 5], color="blue", linewidth=3)
    
    # Dibujar "A"
    ax.plot([3, 3.5, 4], [4, 5.5, 4], color="red", linewidth=3)
    ax.plot([3.25, 3.75], [4.75, 4.75], color="red", linewidth=3)
    
    # Dibujar "F"
    ax.plot([5, 5, 6], [4, 5.5, 5.5], color="green", linewidth=3)
    ax.plot([5, 6], [4.75, 4.75], color="green", linewidth=3)
    
    # Dibujar "E"
    ax.plot([7, 7, 8, 7, 8, 7], [5.5, 4, 4, 4.75, 4.75, 5.5], color="purple", linewidth=3)
    
    # Dibujar "T"
    ax.plot([9, 10], [5.5, 5.5], color="orange", linewidth=3)
    ax.plot([9.5, 9.5], [5.5, 4], color="orange", linewidth=3)
    
    # Mostrar el dibujo
    plt.title("Nombre: Jafet", fontsize=16)
    plt.show()

# Llamar a la función
dibujar_jafet()
