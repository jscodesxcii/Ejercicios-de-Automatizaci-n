from playwright.sync_api import Page, expect

class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        # 1. Elementos para sección Signup
        self.signup_title = page.get_by_text("New User Signup!")
        self.signup_name_input = page.locator("input[data-qa='signup-name']")
        self.signup_email_input = page.locator("input[data-qa='signup-email']")
        self.signup_button = page.locator("button[data-qa='signup-button']")

        # 2. Elementos para login
        self.login_email_input = page.locator("input[data-qa='login-email']")
        self.login_password_input = page.locator("input[data-qa='login-password']")
        self.login_button = page.locator("button[data-qa='login-button']")

    def verify_signup_section_visible(self):
        """
        3. Verificar que la sección 'New User Signup!' esté visible
        """
        expect(self.signup_title).to_be_visible(timeout=5000)

    def signup_user(self, name: str, email: str):
        """
        4. Completar campos de nombre y email para signup y hacer click en Signup
        """
        self.signup_name_input.fill(name)
        self.signup_email_input.fill(email)
        self.signup_button.click()

    def login_user(self, email: str, password: str):
        """
        5. Completar campos de email y password para login y hacer click en Login
        """
        self.login_email_input.fill(email)
        self.login_password_input.fill(password)
        self.login_button.click()

    def verify_login_success(self, username: str):
        """
        6. Verificar que el texto "Logged in as {username}" esté visible, confirmando login exitoso
        """
        expect(self.page.locator(f"text=Logged in as {username}")).to_be_visible(timeout=5000)
