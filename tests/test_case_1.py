"""
Test Case 1: Register User - COMPLETO
===================================
Este archivo contiene el Test Case 1 completo con todos los 18 pasos
del proceso de registro de usuario en automationexercise.com
"""

# Importamos las librerías necesarias
import pytest                                    # Framework de testing
from playwright.sync_api import Page             # Para interactuar con el navegador
from pages.base_page import BasePage            # Página base con métodos comunes
from pages.login_page import LoginPage          # Página de login/signup
from pages.signup_page import SignupPage        # Página de información de cuenta
from utils.data_generator import generate_user_data, generate_birth_date  # Generador de datos


class TestCase1Complete:
    """
    Clase que contiene el Test Case 1 completo.
    
    ¿Qué hace este test?
    - Registra un usuario completamente desde cero
    - Llena todos los formularios necesarios
    - Verifica que el proceso funciona end-to-end
    - Limpia los datos al final (elimina la cuenta creada)
    """
    
    @pytest.mark.smoke           # Marcador: test crítico
    @pytest.mark.authentication  # Marcador: test de autenticación
    def test_case_1_register_user_complete(self, page: Page):
        """
        Test Case 1: Register User - Proceso completo
        
        Args:
            page (Page): Instancia de página de Playwright (viene del fixture)
        
        Pasos del test (según automationexercise.com):
        1. Launch browser
        2. Navigate to url 'http://automationexercise.com'
        3. Verify that home page is visible successfully
        4. Click on 'Signup / Login' button
        5. Verify 'New User Signup!' is visible
        6. Enter name and email address
        7. Click 'Signup' button
        8. Verify that 'ENTER ACCOUNT INFORMATION' is visible
        9. Fill details: Title, Name, Email, Password, Date of birth
        10. Select checkbox 'Sign up for our newsletter!'
        11. Select checkbox 'Receive special offers from our partners!'
        12. Fill details: First name, Last name, Company, Address, Address2, Country, State, City, Zipcode, Mobile Number
        13. Click 'Create Account button'
        14. Verify that 'ACCOUNT CREATED!' is visible
        15. Click 'Continue' button
        16. Verify that 'Logged in as username' is visible
        17. Click 'Delete Account' button
        18. Verify that 'ACCOUNT DELETED!' is visible and click 'Continue' button
        """
        
        # ========================
        # PREPARACIÓN DE DATOS
        # ========================
        
        # Generamos datos únicos para este test
        # Esto asegura que cada ejecución use datos diferentes
        user_data = generate_user_data()    # Datos completos del usuario
        birth_data = generate_birth_date()  # Fecha de nacimiento aleatoria
        
        print("\n" + "="*60)
        print("INICIANDO TEST CASE 1: REGISTER USER COMPLETO")
        print("="*60)
        print(f"Email de prueba: {user_data['email']}")
        print(f"Nombre de prueba: {user_data['name']}")
        print(f"Ciudad de prueba: {user_data['city']}, {user_data['state']}")
        print(f"Fecha nacimiento: {birth_data['day']}/{birth_data['month']}/{birth_data['year']}")
        print("="*60)
        
        # ========================
        # INICIALIZACIÓN DE PÁGINAS
        # ========================
        
        # Creamos instancias de nuestras páginas (Page Object Pattern)
        base_page = BasePage(page)      # Funcionalidades comunes
        login_page = LoginPage(page)    # Página de login/signup
        signup_page = SignupPage(page)  # Página de información de cuenta
        
        # Pausa opcional para ver el inicio
        # input("\nPresiona ENTER para comenzar el test...")
        
        # ========================
        # PASOS 1-3: NAVEGACIÓN INICIAL
        # ========================
        
        print("\nPASOS 1-3: Navegación y verificación inicial")
        print("-" * 50)
        
        # Paso 1-2: Launch browser y Navigate to URL
        # (El navegador ya está abierto por Playwright)
        print("Navegando a la página principal...")
        base_page.navigate_to()  # Va a automationexercise.com
        
        # Paso 3: Verify that home page is visible successfully
        print("Verificando que la página principal es visible...")
        base_page.verify_home_page_visible()  # Busca el logo del sitio
        
        print("Página principal cargada correctamente")
        
        # ========================
        # PASOS 4-5: ACCESO AL SIGNUP
        # ========================
        
        print("\nPASOS 4-5: Acceso a la sección de registro")
        print("-" * 50)
        
        # Paso 4: Click on 'Signup / Login' button
        print("Haciendo click en 'Signup / Login'...")
        base_page.click_signup_login()  # Click en el enlace del header
        
        # Paso 5: Verify 'New User Signup!' is visible
        print("Verificando que la sección 'New User Signup!' es visible...")
        login_page.verify_signup_section_visible()  # Verifica el texto en la página
        
        print("Sección de signup accesible")
        
        # ========================
        # PASOS 6-7: SIGNUP INICIAL
        # ========================
        
        print("\nPASOS 6-7: Registro inicial (nombre y email)")
        print("-" * 50)
        
        # Paso 6: Enter name and email address
        # Paso 7: Click 'Signup' button
        print(f"Registrando usuario: {user_data['name']} con email: {user_data['email']}")
        login_page.signup_user(user_data['name'], user_data['email'])
        
        print("Datos iniciales de signup enviados")
        
        # ========================
        # PASO 8: VERIFICACIÓN DE PÁGINA DE INFORMACIÓN
        # ========================
        
        print("\nPASO 8: Verificación de página de información de cuenta")
        print("-" * 50)
        
        # Paso 8: Verify that 'ENTER ACCOUNT INFORMATION' is visible
        print("Verificando que llegamos a 'ENTER ACCOUNT INFORMATION'...")
        signup_page.verify_account_information_page()
        
        print("Página de información de cuenta cargada")
        
        # ========================
        # PASOS 9-11: INFORMACIÓN DE CUENTA
        # ========================
        
        print("\nPASOS 9-11: Llenado de información de cuenta")
        print("-" * 50)
        
        # Paso 9: Fill details: Title, Name, Email, Password, Date of birth
        # Paso 10: Select checkbox 'Sign up for our newsletter!'
        # Paso 11: Select checkbox 'Receive special offers from our partners!'
        print("Llenando información personal y preferencias...")
        signup_page.fill_account_information(user_data, birth_data)
        
        print("Información de cuenta completada")
        
        # ========================
        # PASO 12: INFORMACIÓN DE DIRECCIÓN
        # ========================
        
        print("\nPASO 12: Llenado de información de dirección")
        print("-" * 50)
        
        # Paso 12: Fill details: First name, Last name, Company, Address, 
        #          Address2, Country, State, City, Zipcode, Mobile Number
        print("Llenando información de dirección y contacto...")
        signup_page.fill_address_information(user_data)
        
        print("Información de dirección completada")
        
        # ========================
        # PASO 13: CREACIÓN DE CUENTA
        # ========================
        
        print("\nPASO 13: Creación de cuenta")
        print("-" * 50)
        
        # Paso 13: Click 'Create Account button'
        print("Creando la cuenta...")
        signup_page.click_create_account()
        
        print("Solicitud de creación de cuenta enviada")
        
        # ========================
        # PASO 14: VERIFICACIÓN DE CUENTA CREADA
        # ========================
        
        print("\nPASO 14: Verificación de cuenta creada")
        print("-" * 50)
        
        # Paso 14: Verify that 'ACCOUNT CREATED!' is visible
        print("Verificando mensaje 'ACCOUNT CREATED!'...")
        base_page.verify_account_created()
        
        print("¡Cuenta creada exitosamente!")
        
        # ========================
        # PASO 15: CONTINUAR DESPUÉS DE CREAR CUENTA
        # ========================
        
        print("\nPASO 15: Continuar después de crear cuenta")
        print("-" * 50)
        
        # Paso 15: Click 'Continue' button
        print("Haciendo click en 'Continue'...")
        signup_page.click_continue()
        
        print("Continuando al dashboard del usuario")
        
        # ========================
        # PASO 16: VERIFICACIÓN DE LOGIN AUTOMÁTICO
        # ========================
        
        print("\n PASO 16: Verificación de login automático")
        print("-" * 50)
        
        # Paso 16: Verify that 'Logged in as username' is visible
        print(f"Verificando que el usuario '{user_data['name']}' está logueado...")
        base_page.verify_logged_in_user(user_data['name'])
        
        print("Usuario logueado automáticamente después del registro")
        
        # ========================
        # PASO 17: ELIMINACIÓN DE CUENTA (CLEANUP)
        # ========================
        
        print("\nPASO 17: Eliminación de cuenta de prueba")
        print("-" * 50)
        
        # Paso 17: Click 'Delete Account' button
        print("Eliminando la cuenta de prueba...")
        base_page.click_delete_account()
        
        print("Solicitud de eliminación enviada")
        
        # ========================
        # PASO 18: VERIFICACIÓN DE CUENTA ELIMINADA
        # ========================
        
        print("\n PASO 18: Verificación de cuenta eliminada")
        print("-" * 50)
        
        # Paso 18: Verify that 'ACCOUNT DELETED!' is visible and click 'Continue'
        print("Verificando mensaje 'ACCOUNT DELETED!'...")
        base_page.verify_account_deleted()
        
        print("Haciendo click en 'Continue' final...")
        signup_page.click_continue()
        
        # ========================
        # FINALIZACIÓN DEL TEST
        # ========================
        
        print("\n" + "="*60)
        print("TEST CASE 1 COMPLETADO EXITOSAMENTE")
        print("="*60)
        print("✅ Usuario registrado correctamente")
        print("✅ Proceso end-to-end verificado")
        print("✅ Cuenta de prueba eliminada (cleanup)")
        print("✅ Todos los 18 pasos ejecutados sin errores")
        print("="*60)
        
        # Pausa final opcional para ver el resultado
        # input("\nTest finalizado. Presiona ENTER para cerrar...")
