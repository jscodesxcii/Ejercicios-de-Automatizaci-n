from faker import Faker
import random

fake = Faker()

def generate_user_data():
    """
    1. Generar datos dinámicos para un usuario, incluyendo contraseña, nombre, email, etc.
    """
    password = fake.password(length=10)
    return {
        "name": fake.first_name(),
        "lastname": fake.last_name(),
        "email": fake.unique.email(),
        "password": password,
        "newsletter": random.choice([True, False]),
        "offers": random.choice([True, False]),
        "company": fake.company(),
        "address1": fake.street_address(),
        "address2": fake.secondary_address(),
        "country": "Canada",  # Puedes ajustar el país si quieres
        "state": fake.state(),
        "city": fake.city(),
        "zipcode": fake.postcode(),
        "mobile_number": fake.phone_number(),
    }

def generate_birth_date():
    """
    2. Generar fecha de nacimiento válida (18 a 80 años)
    """
    birth_date = fake.date_of_birth(minimum_age=18, maximum_age=80)
    return {
        "day": str(birth_date.day),
        "month": str(birth_date.month),
        "year": str(birth_date.year),
    }
