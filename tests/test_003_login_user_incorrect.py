import pytest
import time
from playwright.sync_api import Page, expect
from pages.base_page import BasePage
from pages.login_page import LoginPage

class TestCase3LoginIncorrect:

    @pytest.mark.authentication
    def test_case_3_login_user_incorrect(self, page: Page):
        """
        Test Case 3: Login User with incorrect email and password
        ===========================================================
        Este test valida que el sistema muestre un mensaje de error 
        al intentar iniciar sesión con credenciales incorrectas.
        """

        # 1. Instanciar las páginas necesarias
        base_page = BasePage(page)
        login_page = LoginPage(page)

        # 2. Navegar a la página principal
        base_page.navigate_to()

        # 3. Verificar que la home page esté visible
        base_page.verify_home_page_visible()

        # 4. Hacer click en el enlace 'Signup / Login' para ir a la página de login
        base_page.click_signup_login()

        # 5. Verificar que la sección 'Login to your account' esté visible
        # Aquí verificamos que el campo de email login está visible para asegurarnos que estamos en la página correcta
        expect(page.locator("input[data-qa='login-email']")).to_be_visible(timeout=5000)

        # 6. Completar el formulario con email y contraseña inválidos
        invalid_email = "incorrect@example.com"
        invalid_password = "wrongpassword123"

        login_page.login_user(invalid_email, invalid_password)

        # 7. Verificar que se muestre el mensaje de error esperado
        error_locator = page.locator("p[style='color: red;']")  # Selector para el mensaje de error visible
        expect(error_locator).to_be_visible(timeout=5000)
        error_text = error_locator.inner_text()
        assert error_text == "Your email or password is incorrect!", \
            f"Expected error message not shown, got: '{error_text}'"
        
        time.sleep(5)

        print("Test Case 3 completado exitosamente.")
