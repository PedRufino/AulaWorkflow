def calcular(peso, altura):
    """Calcula o IMC a partir do peso (kg) e altura (m)."""
    return round(peso / (altura ** 2), 2)