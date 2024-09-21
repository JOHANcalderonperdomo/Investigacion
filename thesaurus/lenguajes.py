import pandas as pd
from tabulate import tabulate

# Definir los datos
data = {
    "Posición": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    "Ranking PYPL de septiembre de 2023": [
        "Python", "Java", "JavaScript", "C#", "C/C++", 
        "PHP", "R", "TypeScript", "Swift", "Objective-C"
    ],
    "Encuesta a programadores de Stack Overflow 2023": [
        "JavaScript", "HTML/CSS", "Python", "SQL", "TypeScript", 
        "Bash/Shell", "Java", "C#", "C++", "C"
    ]
}

# Crear el DataFrame
df = pd.DataFrame(data)

# Configurar pandas para que muestre las tablas correctamente en la consola
pd.set_option('display.max_columns', None)
pd.set_option('display.expand_frame_repr', False)
pd.set_option('display.max_colwidth', None)

# Mostrar el DataFrame en consola de forma tabulada usando tabulate
print(tabulate(df, headers='keys', tablefmt='pretty'))

# Si estás en un entorno interactivo como Jupyter, simplemente usa:
# df
