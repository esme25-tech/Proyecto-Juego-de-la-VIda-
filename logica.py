import numpy as np

# Tamaño del tablero
ROWS = 25
COLS = 25

def crear_tablero_vacio():
    """Crea un tablero lleno de ceros (células muertas)."""
    return np.zeros((ROWS, COLS), dtype=int)

def crear_tablero_aleatorio():
    """Crea un tablero con células vivas y muertas al azar."""
    return np.random.choice([0, 1], size=(ROWS, COLS), p=[0.8, 0.2])

def contar_vecinos(grid, x, y):
    """Cuenta los vecinos vivos (tablero toroidal)."""
    total = 0
    for i in [-1, 0, 1]:
        for j in [-1, 0, 1]:
            if i == 0 and j == 0:
                continue
            # Hacemos el tablero toroidal
            col = (x + i) % COLS
            row = (y + j) % ROWS
            total += grid[row, col]
    return total

def siguiente_generacion(grid):
    """Aplica las reglas de Conway para evolucionar el tablero."""
    nuevo_grid = np.zeros((ROWS, COLS), dtype=int)
    for row in range(ROWS):
        for col in range(COLS):
            vecinos = contar_vecinos(grid, col, row)
            if grid[row, col] == 1:
                if vecinos == 2 or vecinos == 3:
                    nuevo_grid[row, col] = 1
            else:
                if vecinos == 3:
                    nuevo_grid[row, col] = 1
    return nuevo_grid