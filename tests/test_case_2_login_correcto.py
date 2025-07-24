"""
Test Case 2: Login User with correct email and password
====================================================
Este test verifica que un usuario puede hacer login correctamente
con credenciales válidas.
"""

# Importamos las librerías necesarias
import pytest                                    # Framework de testing
from playwright.sync_api import Page             # Para interactuar con el navegador
from pages.base_page import BasePage            # Página base con métodos comunes
from pages.login_page import LoginPage          # Página de login/signup
from pages.signup_page import SignupPage        # Página de información de cuenta
from utils.data_generator import generate_user_data, generate_birth_date  # Generador de datos


class TestCase2Login:
    """
    Clase que contiene el Test Case 2: Login con credenciales correctas.
    
    Estrategia del test:
    1. Crear un usuario nuevo (para tener credenciales válidas)
    2. Hacer logout del usuario creado
    3. Hacer login con las credenciales del usuario creado
    4. Verificar que el login fue exitoso
    5. Limpiar (eliminar la cuenta de prueba)
    """
    
    @pytest.mark.smoke           # Marcador: test crítico
    @pytest.mark.authentication  # Marcador: test de autenticación
    def test_case_2_login_user_with_correct_credentials(self, page: Page):
        """
        Test Case 2: Login User with correct email and password
        
        Args:
            page (Page): Instancia de página de Playwright
        
        Pasos del test:
        1. Launch browser
        2. Navigate to url 'http://automationexercise.com'
        3. Verify that home page is visible successfully
        4. Click on 'Signup / Login' button
        5. Verify 'Login to your account' is visible
        6. Enter correct email address and password
        7. Click 'login' button
        8. Verify that 'Logged in as username' is visible
        9. Delete Account (cleanup)
        10. Verify that 'ACCOUNT DELETED!' is visible
        """
        
        # ========================
        # PREPARACIÓN: CREAR USUARIO DE PRUEBA
        # ========================
        
        # Generar datos únicos para este test
        user_data = generate_user_data()
        birth_data = generate_birth_date()
        
        print("\n" + "="*60)
        print("INICIANDO TEST CASE 2: LOGIN CON CREDENCIALES CORRECTAS")
        print("="*60)
        print(f"Email de prueba: {user_data['email']}")
        print(f"Nombre de prueba: {user_data['name']}")
        print(f"Password: {user_data['password']}")
        print("="*60)
        
        # Inicializar páginas
        base_page = BasePage(page)
        login_page = LoginPage(page)
        signup_page = SignupPage(page)
        
        print("\nPRE-REQUISITO: Creando usuario de prueba...")
        print("-" * 50)
        
        # Crear usuario primero (similar al Test Case 1 pero más rápido)
        base_page.navigate_to()
        base_page.click_signup_login()
        login_page.signup_user(user_data['name'], user_data['email'])
        signup_page.complete_full_registration(user_data, birth_data)
        base_page.verify_account_created()
        signup_page.click_continue()
        base_page.verify_logged_in_user(user_data['name'])
        
        # Hacer logout para poder probar el login
        print("Haciendo logout para probar el login...")
        base_page.click_logout()
        
        print("Usuario de prueba creado y logout realizado")
        
        # ========================
        # INICIO DEL TEST CASE 2 REAL
        # ========================
        
        print("\nCOMENZANDO TEST CASE 2 OFICIAL")
        print("=" * 50)
        
        # Pasos 1-3: Navigate and verify home page
        print("\nPASOS 1-3: Navegación inicial")
        print("-" * 30)
        
        print("Navegando a la página principal...")
        base_page.navigate_to()
        
        print("Verificando que la página principal es visible...")
        base_page.verify_home_page_visible()
        
        # Paso 4: Click on 'Signup / Login' button
        print("\nPASO 4: Acceso a login")
        print("-" * 30)
        
        print("Haciendo click en 'Signup / Login'...")
        base_page.click_signup_login()
        
        # Paso 5: Verify 'Login to your account' is visible
        print("\nPASO 5: Verificación de sección de login")
        print("-" * 30)
        
        print("Verificando que 'Login to your account' es visible...")
        login_page.verify_login_section_visible()
        
        # Pasos 6-7: Enter credentials and click login
        print("\nPASOS 6-7: Proceso de login")
        print("-" * 30)
        
        print(f"Haciendo login con email: {user_data['email']}")
        login_page.login_user(user_data['email'], user_data['password'])
        
        # Paso 8: Verify that 'Logged in as username' is visible
        print("\nPASO 8: Verificación de login exitoso")
        print("-" * 30)
        
        print(f"Verificando que '{user_data['name']}' está logueado...")
        base_page.verify_logged_in_user(user_data['name'])
        
        # ========================
        # CLEANUP: ELIMINAR CUENTA DE PRUEBA
        # ========================
        
        print("\nPASOS 9-10: Cleanup - Eliminar cuenta de prueba")
        print("-" * 30)
        
        print("Eliminando cuenta de prueba...")
        base_page.click_delete_account()
        
        print("Verificando que la cuenta fue eliminada...")
        base_page.verify_account_deleted()
        
        # ========================
        # FINALIZACIÓN DEL TEST
        # ========================
        
        print("\n" + "="*60)
        print("TEST CASE 2 COMPLETADO EXITOSAMENTE")
        print("="*60)
        print("Usuario creado correctamente")
        print("Login realizado exitosamente")
        print("Verificaciones pasaron correctamente")
        print("Cuenta de prueba eliminada (cleanup)")
        print("Todos los pasos ejecutados sin errores")
        print("="*60)