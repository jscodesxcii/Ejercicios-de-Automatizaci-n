import pytest
import time
from playwright.sync_api import Page
from pages.base_page import BasePage
from pages.login_page import LoginPage
from helpers import TestHelpers

class TestCase2LoginCorrect:

    @pytest.mark.authentication
    def test_case_2_register_then_login(self, page: Page):
        """
        1. Registrar usuario sin eliminar cuenta
        2. Cerrar sesión
        3. Hacer login con usuario recién creado
        4. Verificar login exitoso
        """
        # 1. Registrar usuario sin eliminar cuenta para usarlo luego en login
        user_data = TestHelpers.register_user(page, delete_account=False)

        # 2. Cerrar sesión haciendo click en logout
        page.locator("a[href='/logout']").click()

        # 3. Instanciar páginas para login
        base_page = BasePage(page)
        login_page = LoginPage(page)

        # 4. Volver a la página de login
        base_page.click_signup_login()

        # 5. Completar login con email y password
        login_page.login_user(user_data["email"], user_data["password"])

        # 6. Verificar login exitoso
        login_page.verify_login_success(user_data["name"])

        time.sleep(5)

        print("Test Case 2 completado exitosamente.")
