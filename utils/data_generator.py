"""
Generador de datos de prueba
==========================
Este archivo contiene funciones para generar datos únicos 
para usar en nuestros tests automatizados.
"""

# Importamos las librerías que necesitamos
from faker import Faker  # Para generar datos falsos pero realistas
import time             # Para trabajar con timestamps
from config.settings import Config  # Para usar la configuración del proyecto

# Creamos una instancia de Faker para generar datos en inglés
fake = Faker()


def generate_timestamp():
    """
    Genera un timestamp único basado en el tiempo actual.
    
    Returns:
        str: Timestamp único como string (ej: "1699123456")
    
    ¿Por qué lo usamos?
    - Para hacer que cada email sea único en cada ejecución del test
    - Evita conflictos cuando ejecutamos tests múltiples veces
    """
    # time.time() devuelve el tiempo actual en segundos desde 1970
    # int() convierte el decimal a entero
    # str() convierte el número a texto
    return str(int(time.time()))


def generate_user_data():
    """
    Genera todos los datos necesarios para registrar un usuario completo.
    
    Returns:
        dict: Diccionario con todos los datos del usuario
    
    ¿Qué datos genera?
    - Información personal (nombre, email, contraseña)
    - Información de dirección (ciudad, estado, código postal, etc.)
    """
    # Generamos un timestamp único para este usuario
    timestamp = generate_timestamp()
    
    # Retornamos un diccionario con todos los datos necesarios
    return {
        # DATOS PERSONALES
        'name': fake.first_name(),           # Genera nombre como "John"
        'email': f"testuser_{timestamp}@testautomation.com",  # Email único
        'password': Config.DEFAULT_PASSWORD,  # Contraseña desde configuración
        
        # DATOS DE NOMBRE COMPLETO
        'first_name': fake.first_name(),     # Nombre: "Maria"
        'last_name': fake.last_name(),       # Apellido: "Garcia"
        
        # DATOS DE EMPRESA Y DIRECCIÓN
        'company': fake.company(),           # Empresa: "Tech Solutions Inc"
        'address': fake.street_address(),    # Dirección: "123 Main St"
        'address2': fake.secondary_address(), # Dirección 2: "Apt 4B"
        
        # DATOS DE UBICACIÓN
        'country': 'United States',          # País fijo (el sitio lo requiere)
        'state': fake.state(),               # Estado: "California"
        'city': fake.city(),                 # Ciudad: "Los Angeles"
        'zipcode': fake.zipcode(),           # Código postal: "90210"
        
        # DATOS DE CONTACTO
        'mobile_number': fake.phone_number() # Teléfono: "(555) 123-4567"
    }


def generate_birth_date():
    """
    Genera una fecha de nacimiento aleatoria para el formulario.
    
    Returns:
        dict: Diccionario con día, mes y año de nacimiento
    
    ¿Por qué separado?
    - El formulario del sitio tiene selectores separados para día, mes, año
    - Necesitamos datos en formato específico para cada campo
    """
    import random  # Para generar números aleatorios
    
    return {
        'day': str(random.randint(1, 28)),    # Día: "15" (1-28 para evitar problemas)
        'month': fake.month_name(),           # Mes: "January"
        'year': str(random.randint(1980, 2000))  # Año: "1995"
    }


def generate_simple_user():
    """
    Genera datos básicos de usuario para tests simples.
    
    Returns:
        dict: Solo nombre y email para casos básicos
    
    ¿Cuándo lo usamos?
    - Para tests que solo necesitan signup básico
    - Para tests más rápidos que no llenan todo el formulario
    """
    timestamp = generate_timestamp()
    
    return {
        'name': fake.first_name(),
        'email': f"simple_{timestamp}@testautomation.com"
    }


# Función de utilidad para debugging
def print_user_data():
    """
    Función helper para ver qué datos genera.
    Útil para debugging durante desarrollo.
    """
    print("=== DATOS GENERADOS ===")
    user = generate_user_data()
    birth = generate_birth_date()
    
    print(f"Nombre: {user['name']}")
    print(f"Email: {user['email']}")
    print(f"Ciudad: {user['city']}, {user['state']}")
    print(f"Fecha nacimiento: {birth['day']}/{birth['month']}/{birth['year']}")
    print("=====================")


# Si ejecutamos este archivo directamente, muestra datos de ejemplo
if __name__ == "__main__":
    print_user_data()