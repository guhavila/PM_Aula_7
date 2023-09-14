import numpy as np

# Função para calcular as coordenadas de A a partir dos ângulos e comprimento das hastes
def calcular_coordenadas(angulo1, angulo2, comprimento_a, comprimento_b):
    # Converte os ângulos de graus para radianos
    angulo1 = np.radians(angulo1)
    angulo2 = np.radians(angulo2)
    
    # Calcula as coordenadas de A usando a lei dos cossenos
    x_A = comprimento_a * np.cos(angulo1) + comprimento_b * np.cos(angulo1 + angulo2)
    y_A = comprimento_a * np.sin(angulo1) + comprimento_b * np.sin(angulo1 + angulo2)
    
    return x_A, y_A

# Ângulos em graus
angulo1 = 90.0
angulo2 = 90.0

# Comprimento das hastes
comprimento_a = 15.0
comprimento_b = 30.0

# Calcula as coordenadas de A
x_A, y_A = calcular_coordenadas(angulo1, angulo2, comprimento_a, comprimento_b)

print(f"Coordenada x de A: {x_A}")
print(f"Coordenada y de A: {y_A}")
