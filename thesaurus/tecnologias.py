import pandas as pd
from tabulate import tabulate

# Definir los datos basados en la imagen
data = {
    "Tecnología": [
        "IA/ML", "Rust", "JavaScript y sus marcos de trabajo", 
        "Go", "Kotlin", "Cadena de bloques", 
        "Python", "WebAssembly"
    ],
    "Porcentaje": [
        "14%", "13%", "11%", 
        "9%", "8%", "6%", 
        "6%", "6%"
    ]
}

# Crear el DataFrame
df = pd.DataFrame(data)

# Mostrar el DataFrame de forma tabulada usando tabulate
print(tabulate(df, headers='keys', tablefmt='pretty'))
