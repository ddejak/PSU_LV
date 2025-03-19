import numpy as np
import matplotlib.pyplot as plt

def chessboard(square_size, rows, cols):
    black = np.zeros((square_size, square_size), dtype=np.uint8)
    white = np.ones((square_size, square_size), dtype=np.uint8) * 255
    
    row1 = np.hstack([black, white] * (cols // 2))
    row2 = np.hstack([white, black] * (cols // 2))
    
    chessboard = np.vstack([row1, row2] * (rows // 2))
    
    return chessboard

square_size = 25 
rows, cols = 8, 8

img = chessboard(square_size, rows, cols)

plt.imshow(img, cmap='gray', vmin=0, vmax=255)

plt.xticks(np.arange(0, cols * square_size, square_size))
plt.yticks(np.arange(0, rows * square_size, square_size))

plt.xlabel("Širina (piksela)")
plt.ylabel("Visina (piksela)")

plt.show()
