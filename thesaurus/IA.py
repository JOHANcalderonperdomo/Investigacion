import pandas as pd
from tabulate import tabulate

# Datos de las IA más utilizadas por programadores en 2024
data = {
    "AI Tool": ["GitHub Copilot", "Tabnine", "Codex", "DeepCode", "Replit Ghostwriter"],
    "Usage": ["Auto-completion and suggestions", "Code completion", "Code generation", "Static code analysis", "Auto-completion and suggestions"],
    "Company": ["GitHub/Microsoft", "Tabnine", "OpenAI", "Snyk", "Replit"],
    "Features": [
        "Context-aware code suggestions, integrated with GitHub",
        "AI-assisted code completion for various languages",
        "Generates code based on natural language prompts",
        "Finds vulnerabilities and suggests fixes",
        "Real-time code suggestions, integrated with Replit IDE"
    ]
}

# Crear DataFrame
df = pd.DataFrame(data)

# Mostrar tabla usando tabulate
table = tabulate(df, headers="keys", tablefmt="grid")
print(table)
