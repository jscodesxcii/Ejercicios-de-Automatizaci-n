"""
Page Object para la página de Account Information (Signup completo)
================================================================
Este archivo maneja todo el formulario largo de registro de usuario
que aparece después de hacer el signup inicial.
"""

# Importamos las librerías necesarias
from playwright.sync_api import Page, expect  # Para interactuar con el navegador
from pages.base_page import BasePage          # Heredamos de la clase base
import time                                   # Para pausas adicionales


class SignupPage(BasePage):
    """
    Clase que representa la página de Account Information.
    
    ¿Qué hace esta página?
    - Aparece después del signup inicial (nombre + email)
    - Contiene un formulario largo con datos personales y dirección
    - Es donde completamos todo el registro del usuario
    """
    
    def __init__(self, page: Page):
        """
        Constructor de la clase.
        
        Args:
            page: La instancia de página de Playwright
        """
        # Llamamos al constructor de la clase padre
        super().__init__(page)
        
        # SELECTORES DE INFORMACIÓN PERSONAL
        self.title_mr_radio = "#id_gender1"        # Radio button "Mr."
        self.title_mrs_radio = "#id_gender2"       # Radio button "Mrs."
        self.password_input = "#password"          # Campo contraseña
        
        # SELECTORES DE FECHA DE NACIMIENTO
        self.birth_day_select = "#days"            # Dropdown día
        self.birth_month_select = "#months"        # Dropdown mes  
        self.birth_year_select = "#years"          # Dropdown año
        
        # SELECTORES DE CHECKBOXES
        self.newsletter_checkbox = "#newsletter"   # Checkbox newsletter
        self.offers_checkbox = "#optin"           # Checkbox ofertas especiales
        
        # SELECTORES DE INFORMACIÓN DE DIRECCIÓN
        self.first_name_input = "#first_name"     # Nombre
        self.last_name_input = "#last_name"       # Apellido
        self.company_input = "#company"           # Empresa
        self.address_input = "#address1"          # Dirección principal
        self.address2_input = "#address2"         # Dirección secundaria
        self.country_select = "#country"          # Dropdown país
        self.state_input = "#state"               # Estado/Provincia
        self.city_input = "#city"                 # Ciudad
        self.zipcode_input = "#zipcode"           # Código postal
        self.mobile_number_input = "#mobile_number" # Número móvil
        
        # SELECTORES DE BOTONES
        self.create_account_button = "[data-qa='create-account']"  # Botón crear cuenta
        self.continue_button = "[data-qa='continue-button']"       # Botón continuar
    
    def verify_account_information_page(self):
        """
        Verifica que estamos en la página de información de cuenta.
        
        ¿Qué verifica?
        - Que aparece el título "Enter Account Information"
        - Que llegamos a la página correcta después del signup
        """
        print("Verificando que estamos en la página 'Enter Account Information'...")
        
        # Esperamos a que aparezca el título de la página
        expect(self.page.locator("text=Enter Account Information")).to_be_visible()
        
        print("Página de información de cuenta confirmada")
        time.sleep(1)  # Pausa para ver la página
    
    def select_title_mr(self):
        """
        Selecciona el radio button "Mr." para el título.
        """
        print("Seleccionando título 'Mr.'...")
        self.click_element(self.title_mr_radio)
        print("Título 'Mr.' seleccionado")
    
    def select_title_mrs(self):
        """
        Selecciona el radio button "Mrs." para el título.
        """
        print("Seleccionando título 'Mrs.'...")
        self.click_element(self.title_mrs_radio)
        print("Título 'Mrs.' seleccionado")
    
    def fill_password(self, password: str):
        """
        Llena el campo de contraseña.
        
        Args:
            password (str): La contraseña a usar
        
        Nota: El nombre y email ya están pre-llenados desde el paso anterior
        """
        print(f"Ingresando contraseña...")
        self.fill_input(self.password_input, password)
        print("Contraseña ingresada")
    
    def select_birth_date(self, day: str, month: str, year: str):
        """
        Selecciona la fecha de nacimiento en los dropdowns.
        
        Args:
            day (str): Día de nacimiento (ej: "15")
            month (str): Mes de nacimiento (ej: "January") 
            year (str): Año de nacimiento (ej: "1990")
        
        ¿Por qué strings?
        - Los dropdowns HTML usan valores como texto
        - Faker genera los meses como nombres en inglés
        """
        print(f"Seleccionando fecha de nacimiento: {day}/{month}/{year}")
        
        # page.select_option() selecciona una opción en un dropdown
        self.page.select_option(self.birth_day_select, day)
        print(f"   ✓ Día seleccionado: {day}")
        
        self.page.select_option(self.birth_month_select, month)  
        print(f"   ✓ Mes seleccionado: {month}")
        
        self.page.select_option(self.birth_year_select, year)
        print(f"   ✓ Año seleccionado: {year}")
        
        time.sleep(1)  # Pausa para ver las selecciones
    
    def check_newsletter_subscription(self):
        """
        Marca el checkbox para suscribirse al newsletter.
        """
        print("Marcando suscripción al newsletter...")
        self.click_element(self.newsletter_checkbox)
        print("Newsletter marcado")
    
    def check_special_offers(self):
        """
        Marca el checkbox para recibir ofertas especiales.
        """
        print("Marcando recepción de ofertas especiales...")
        self.click_element(self.offers_checkbox)
        print("Ofertas especiales marcadas")
    
    def fill_account_information(self, user_data: dict, birth_data: dict):
        """
        Llena toda la sección de información de cuenta.
        
        Args:
            user_data (dict): Datos del usuario generados por data_generator
            birth_data (dict): Fecha de nacimiento generada por data_generator
        
        ¿Qué incluye?
        - Selección de título (Mr/Mrs)
        - Contraseña
        - Fecha de nacimiento  
        - Suscripciones (newsletter y ofertas)
        """
        print("Llenando información de cuenta...")
        
        # 1. Seleccionar título (por defecto Mr.)
        self.select_title_mr()
        
        # 2. Llenar contraseña
        self.fill_password(user_data['password'])
        
        # 3. Seleccionar fecha de nacimiento
        self.select_birth_date(
            birth_data['day'],
            birth_data['month'], 
            birth_data['year']
        )
        
        # 4. Marcar checkboxes
        self.check_newsletter_subscription()
        self.check_special_offers()
        
        print("Información de cuenta completada")
        time.sleep(2)  # Pausa para revisar los datos
    
    def fill_address_information(self, user_data: dict):
        """
        Llena toda la sección de información de dirección.
        
        Args:
            user_data (dict): Datos del usuario con información de dirección
        
        ¿Qué incluye?
        - Información personal (nombre, apellido, empresa)
        - Dirección completa (calle, ciudad, estado, código postal)
        - Información de contacto (teléfono)
        """
        print("Llenando información de dirección...")
        
        # INFORMACIÓN PERSONAL
        print("Llenando datos personales...")
        self.fill_input(self.first_name_input, user_data['first_name'])
        self.fill_input(self.last_name_input, user_data['last_name'])
        self.fill_input(self.company_input, user_data['company'])
        
        # DIRECCIÓN
        print("Llenando dirección...")
        self.fill_input(self.address_input, user_data['address'])
        self.fill_input(self.address2_input, user_data['address2'])
        
        # UBICACIÓN
        print("Seleccionando ubicación...")
        self.page.select_option(self.country_select, user_data['country'])
        self.fill_input(self.state_input, user_data['state'])
        self.fill_input(self.city_input, user_data['city'])
        self.fill_input(self.zipcode_input, user_data['zipcode'])
        
        # CONTACTO
        print("Agregando información de contacto...")
        self.fill_input(self.mobile_number_input, user_data['mobile_number'])
        
        print("Información de dirección completada")
        time.sleep(2)  # Pausa para revisar la información
    
    def click_create_account(self):
        """
        Hace click en el botón "Create Account".
        
        Este es el botón final que envía todo el formulario.
        """
        print("Haciendo click en 'Create Account'...")
        self.click_element(self.create_account_button)
        print("Botón 'Create Account' presionado")
        
        # Pausa más larga porque este proceso puede tardar
        time.sleep(3)
    
    def click_continue(self):
        """
        Hace click en el botón "Continue".
        
        Este botón aparece después de crear la cuenta exitosamente.
        """
        print("Haciendo click en 'Continue'...")
        self.click_element(self.continue_button)
        print("Botón 'Continue' presionado")
        time.sleep(2)
    
    def complete_full_registration(self, user_data: dict, birth_data: dict):
        """
        Método conveniente que completa todo el proceso de registro.
        
        Args:
            user_data (dict): Datos del usuario
            birth_data (dict): Fecha de nacimiento
        
        ¿Qué hace?
        - Combina todos los pasos en un solo método
        - Útil para tests que quieren el proceso completo
        - Maneja todo desde información de cuenta hasta crear cuenta
        """
        print("Iniciando proceso completo de registro...")
        
        # 1. Verificar que estamos en la página correcta
        self.verify_account_information_page()
        
        # 2. Llenar información de cuenta
        self.fill_account_information(user_data, birth_data)
        
        # 3. Llenar información de dirección
        self.fill_address_information(user_data)
        
        # 4. Crear la cuenta
        self.click_create_account()
        
        print("Proceso completo de registro finalizado")