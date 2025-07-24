"""
Page Object para la página de Login y Signup
==========================================
Este archivo contiene la clase LoginPage que maneja todas las 
interacciones con la página de login/signup de automationexercise.com
"""

# Importamos las librerías necesarias
import time
from playwright.sync_api import Page, expect  # Para interactuar con el navegador
from pages.base_page import BasePage          # Heredamos de la clase base


class LoginPage(BasePage):
    """
    Clase que representa la página de Login/Signup.
    
    ¿Qué hace esta clase?
    - Maneja todas las acciones en la página de login/signup
    - Proporciona métodos para llenar formularios
    - Verifica que los elementos estén visibles
    - Encapsula los selectores (no los repetimos en los tests)
    """
    
    def __init__(self, page: Page):
        """
        Constructor de la clase.
        
        Args:
            page: La instancia de página de Playwright
        """
        # Llamamos al constructor de la clase padre (BasePage)
        super().__init__(page)
        
        # SELECTORES DE LA SECCIÓN SIGNUP
        # Estos son los identificadores únicos de cada elemento en la página
        self.signup_name_input = "[data-qa='signup-name']"      # Campo nombre signup
        self.signup_email_input = "[data-qa='signup-email']"    # Campo email signup  
        self.signup_button = "[data-qa='signup-button']"        # Botón signup
        
        # SELECTORES DE LA SECCIÓN LOGIN
        self.login_email_input = "[data-qa='login-email']"      # Campo email login
        self.login_password_input = "[data-qa='login-password']" # Campo password login
        self.login_button = "[data-qa='login-button']"          # Botón login
        
        # SELECTORES DE MENSAJES DE ERROR
        self.login_error_message = "text=Your email or password is incorrect!"
        self.signup_error_message = "text=Email Address already exist!"
    
    def verify_signup_section_visible(self):
        """
        Verifica que la sección de signup sea visible en la página.
        
        ¿Qué hace?
        - Busca el texto "New User Signup!" en la página
        - Si no lo encuentra, el test falla
        - Asegura que estamos en la página correcta
        """
        print("Verificando que la sección 'New User Signup!' es visible...")
        
        # expect() es de Playwright y verifica que algo sea cierto
        # Si falla, automáticamente hace fallar el test
        expect(self.page.locator("text=New User Signup!")).to_be_visible()
        
        print("Sección de signup confirmada como visible")
    
    def verify_login_section_visible(self):
        """
        Verifica que la sección de login sea visible en la página.
        
        Similar a verify_signup_section_visible pero para login.
        """
        print("Verificando que la sección 'Login to your account' es visible...")
        expect(self.page.locator("text=Login to your account")).to_be_visible()
        print("Sección de login confirmada como visible")
    
    def fill_signup_form(self, name: str, email: str):
        """
        Llena el formulario de signup con los datos proporcionados.
        
        Args:
            name (str): Nombre del usuario a registrar
            email (str): Email del usuario a registrar
        
        ¿Qué hace?
        - Limpia y llena el campo de nombre
        - Limpia y llena el campo de email
        - No hace click en submit (eso lo hace otro método)
        """
        print(f"Llenando formulario de signup:")
        print(f"   - Nombre: {name}")
        print(f"   - Email: {email}")
        
        # Usamos el método fill_input de la clase padre (BasePage)
        # Este método ya incluye pausas y prints para debugging
        self.fill_input(self.signup_name_input, name)
        self.fill_input(self.signup_email_input, email)
        
        print("Formulario de signup completado")
    
    def click_signup_button(self):
        """
        Hace click en el botón de Signup.
        
        ¿Por qué método separado?
        - Separamos llenar formulario de enviarlo
        - Permite mayor flexibilidad en los tests
        - Podemos verificar datos antes de enviar
        """
        print("Haciendo click en el botón 'Signup'...")
        
        # Usamos click_element de BasePage que incluye pausas y highlighting
        self.click_element(self.signup_button)
        
        print("Botón Signup presionado")
    
    def signup_user(self, name: str, email: str):
        """
        Proceso completo de signup de usuario.
        
        Args:
            name (str): Nombre del usuario
            email (str): Email del usuario
        
        ¿Qué hace?
        - Combina llenar formulario + hacer click
        - Método conveniente para usar en tests
        - Un solo método para el flujo completo de signup
        """
        print(f"Iniciando proceso de signup para: {name}")
        
        # Llamamos a los métodos individuales en orden
        self.fill_signup_form(name, email)  # Primero llenamos
        self.click_signup_button()          # Después enviamos
        
        print("Proceso de signup completado")
    
    def fill_login_form(self, email: str, password: str):
        """
        Llena el formulario de login con credenciales.
        
        Args:
            email (str): Email del usuario
            password (str): Contraseña del usuario
        """
        print(f"Llenando formulario de login para: {email}")
        
        self.fill_input(self.login_email_input, email)
        self.fill_input(self.login_password_input, password)
        
        print("Formulario de login completado")
    
    def click_login_button(self):
        """
        Hace click en el botón de Login.
        """
        print("Haciendo click en el botón 'Login'...")
        self.click_element(self.login_button)
        print("Botón Login presionado")
    
    def login_user(self, email: str, password: str):
        """
        Proceso completo de login de usuario.
        
        Args:
            email (str): Email del usuario
            password (str): Contraseña del usuario
        """
        print(f"Iniciando proceso de login para: {email}")
        
        self.fill_login_form(email, password)
        self.click_login_button()
        
        print("Proceso de login completado")
    
    def verify_login_error(self):
        """
        Verifica que aparezca el mensaje de error de login.
        
        ¿Cuándo se usa?
        - En tests negativos (credenciales incorrectas)
        - Para verificar que el sistema valida correctamente
        """
        print("Verificando mensaje de error de login...")
        expect(self.page.locator(self.login_error_message)).to_be_visible()
        print("Mensaje de error confirmado")
    
    def verify_signup_error(self):
        """
        Verifica que aparezca el mensaje de error de signup.
        
        ¿Cuándo se usa?
        - Cuando intentamos registrar email que ya existe
        - Para tests de validación de duplicados
        """
        print("Verificando mensaje de error de signup...")
        expect(self.page.locator(self.signup_error_message)).to_be_visible()
        print("Mensaje de error confirmado")


    """<<<Metodos agregados para el TEST CASE 2>>>"""


    def fill_login_form(self, email: str, password: str):
        """
        Llena el formulario de login con credenciales.
        
        Args:
            email (str): Email del usuario
            password (str): Contraseña del usuario
        """
        print(f"Llenando formulario de login para: {email}")
        
        # Usar los métodos heredados de BasePage
        self.fill_input(self.login_email_input, email)
        self.fill_input(self.login_password_input, password)
        
        print("Formulario de login completado")
    
    def click_login_button(self):
        """
        Hace click en el botón de Login.
        """
        print("Haciendo click en el botón 'Login'...")
        self.click_element(self.login_button)
        print("Botón Login presionado")
        time.sleep(2)  # Pausa para ver el resultado
    
    def login_user(self, email: str, password: str):
        """
        Proceso completo de login de usuario.
        
        Args:
            email (str): Email del usuario
            password (str): Contraseña del usuario
            
        Este método combina llenar el formulario y hacer click en login.
        """
        print(f"Iniciando proceso de login para: {email}")
        
        # Llamar a los métodos individuales
        self.fill_login_form(email, password)
        self.click_login_button()
        
        print("Proceso de login completado")
    
    def verify_login_error(self):
        """
        Verifica que aparezca el mensaje de error de login.
        
        ¿Cuándo se usa?
        - En tests negativos (credenciales incorrectas)
        - Para verificar que el sistema valida correctamente
        """
        print("Verificando mensaje de error de login...")
        expect(self.page.locator(self.login_error_message)).to_be_visible()
        print("Mensaje de error confirmado")