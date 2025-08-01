from pages.base_page import BasePage
from pages.login_page import LoginPage
from pages.signup_page import SignupPage
from utils.data_generator import generate_user_data, generate_birth_date
from playwright.sync_api import Page

class TestHelpers:

    @staticmethod
    def register_user(page: Page, delete_account: bool = True):
        """
        1. Registro completo de usuario automatizado.
        2. Parámetro delete_account: si es True, elimina la cuenta al final (Test Case 1).
           Si es False, no elimina la cuenta (Test Case 2).
        3. Devuelve el diccionario con datos del usuario creado para usar después.
        """
        # 1. Generar datos dinámicos
        user_data = generate_user_data()
        birth_data = generate_birth_date()

        # 2. Instanciar páginas
        base_page = BasePage(page)
        login_page = LoginPage(page)
        signup_page = SignupPage(page)

        # 3. Navegar a home y verificar
        base_page.navigate_to()
        base_page.verify_home_page_visible()

        # 4. Ir a Signup/Login
        base_page.click_signup_login()
        login_page.verify_signup_section_visible()

        # 5. Completar nombre y email para signup
        login_page.signup_user(user_data["name"], user_data["email"])

        # 6. Verificar que cargue la página de info cuenta
        signup_page.verify_account_information_page()

        # 7. Completar información personal y fecha de nacimiento
        signup_page.fill_account_information(user_data, birth_data)

        # 8. Completar dirección
        signup_page.fill_address_information(user_data)

        # 9. Crear cuenta
        signup_page.click_create_account()

        # 10. Verificar cuenta creada
        base_page.verify_account_created()

        # 11. Click en continuar
        signup_page.click_continue()

        # 12. Verificar que esté logueado
        base_page.verify_logged_in_user(user_data["name"])

        # 13. Si se indica eliminar cuenta, hacerlo
        if delete_account:
            base_page.click_delete_account()
            base_page.verify_account_deleted()
            signup_page.click_continue()

        # 14. Retornar datos de usuario para uso posterior (login, etc.)
        return user_data
