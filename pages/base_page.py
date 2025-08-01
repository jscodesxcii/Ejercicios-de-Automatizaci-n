from playwright.sync_api import Page

class BasePage:
    def __init__(self, page: Page):
        self.page = page

    def navigate_to(self, url: str = "https://automationexercise.com/"):
        """
        1. Navegar a la URL principal del sitio
        """
        self.page.goto(url)

    def verify_home_page_visible(self):
        """
        2. Verificar que el slider de la home page esté visible
        """
        assert self.page.locator("#slider").is_visible(), "Home page slider no visible"

    def click_signup_login(self):
        """
        3. Hacer click en el enlace 'Signup / Login'
        """
        self.page.locator("a[href='/login']").click()

    def verify_account_created(self):
        """
        4. Verificar que el texto 'Account Created!' aparezca luego de registrar cuenta
        """
        text = self.page.locator("h2[data-qa='account-created']").inner_text()
        assert text == "Account Created!", f"Expected 'Account Created!' but got '{text}'"

    def verify_logged_in_user(self, username: str):
        """
        5. Verificar que el usuario logueado aparezca en la pantalla con el texto "Logged in as {username}"
        """
        assert self.page.locator(f"text=Logged in as {username}").is_visible(), "Logged in user not visible"

    def click_delete_account(self):
        """
        6. Hacer click en el enlace 'Delete Account' para eliminar cuenta
        """
        self.page.locator("a[href='/delete_account']").click()

    def verify_account_deleted(self):
        """
        7. Verificar que el texto 'Account Deleted!' aparezca luego de eliminar la cuenta
        """
        text = self.page.locator("h2[data-qa='account-deleted']").inner_text()
        assert text == "Account Deleted!", f"Expected 'Account Deleted!' but got '{text}'"
