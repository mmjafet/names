import matplotlib.pyplot as plt

def dibujar_messi_con_balones():
    fig, ax = plt.subplots(figsize=(10, 6))
    
    # Configuración general
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 6)
    ax.axis("off")  # Ocultar los ejes
    
    def dibujar_balon(x, y, color="black"):
        """Dibuja un balón en una posición (x, y)"""
        circle = plt.Circle((x, y), 0.3, color=color, fill=True)
        ax.add_artist(circle)
    
    # Dibujar "M"
    dibujar_balon(1, 5, "blue")
    dibujar_balon(1, 4, "blue")
    dibujar_balon(2, 5, "blue")
    dibujar_balon(3, 4, "blue")
    dibujar_balon(3, 5, "blue")
    
    # Dibujar "E"
    dibujar_balon(4, 5, "green")
    dibujar_balon(4, 4.5, "green")
    dibujar_balon(4, 4, "green")
    dibujar_balon(5, 5, "green")
    dibujar_balon(5, 4, "green")
    dibujar_balon(5, 4.5, "green")
    
    # Dibujar "S"
    dibujar_balon(6, 5, "red")
    dibujar_balon(6, 4.5, "red")
    dibujar_balon(6, 4, "red")
    dibujar_balon(7, 5, "red")
    dibujar_balon(7, 4, "red")
    
    # Dibujar "S"
    dibujar_balon(8, 5, "purple")
    dibujar_balon(8, 4.5, "purple")
    dibujar_balon(8, 4, "purple")
    dibujar_balon(9, 5, "purple")
    dibujar_balon(9, 4, "purple")
    
    # Dibujar "I"
    dibujar_balon(10, 5, "orange")
    dibujar_balon(10, 4, "orange")
    
    # Mostrar el dibujo
    plt.title("Nombre: Messi (con balones)", fontsize=16)
    plt.show()

# Llamar a la función
dibujar_messi_con_balones()
