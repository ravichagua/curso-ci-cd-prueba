def suma(a, b):
    """Calcula la suma de dos números 1."""
    return a + b

def resta(a, b):
    """Calcula la resta de dos números."""
    return a - b

def obtener_mensaje_bienvenida(nombre="Usuario"):
    """Retorna un mensaje de bienvenida personalizado."""
    return f"¡Hola, {nombre}! Bienvenido a la aplicación."

if __name__ == "__main__":
    print(obtener_mensaje_bienvenida("DevOps Team"))
    
    resultado_suma = suma(10, 5)
    resultado_resta = resta(10, 5)
    
    print(f"Resultado Suma (10 + 5): {resultado_suma}")
    print(f"Resultado Resta (10 - 5): {resultado_resta}")
