import numpy as np
import matplotlib.pyplot as plt

def chessboard(square_size, rows, cols):
    # Kreiraj jedan crno-bijeli kvadrat
    black = np.zeros((square_size, square_size), dtype=np.uint8)
    white = np.ones((square_size, square_size), dtype=np.uint8) * 255
    
    # Kreiraj jedan red izmjeničnih crnih i bijelih kvadrata
    row1 = np.hstack([black, white] * (cols // 2))
    row2 = np.hstack([white, black] * (cols // 2))
    
    # Vertikalno ponavljanje redova kako bi se dobila šahovska ploča
    chessboard = np.vstack([row1, row2] * (rows // 2))
    
    return chessboard

# Postavke veličine ploče
square_size = 25  # Veličina jednog kvadrata u pikselima
rows, cols = 8, 8  # Broj kvadrata po visini i širini

# Generiranje slike šahovske ploče
img = chessboard(square_size, rows, cols)

# Prikaz slike s oznakama osi
plt.imshow(img, cmap='gray', vmin=0, vmax=255)

# Postavi oznake na osi prema veličini kvadrata
plt.xticks(np.arange(0, cols * square_size, square_size))
plt.yticks(np.arange(0, rows * square_size, square_size))

# Dodaj opise osi
plt.xlabel("Širina (piksela)")
plt.ylabel("Visina (piksela)")

plt.show()
