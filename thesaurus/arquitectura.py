import pandas as pd
from tabulate import tabulate

# Definir los datos
data = {
    "Arquitectura": [
        "Microservicios", 
        "Serverless", 
        "Monolítica", 
        "Event-Driven", 
        "Arquitectura de Capas"
    ],
    "Porcentaje de Uso Estimado (%)": [
        "40%", 
        "30%", 
        "15%", 
        "10%", 
        "5%"
    ]
}

# Crear el DataFrame
df = pd.DataFrame(data)

# Mostrar el DataFrame de forma tabulada usando tabulate
print(tabulate(df, headers='keys', tablefmt='pretty'))
