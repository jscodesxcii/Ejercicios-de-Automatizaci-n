from playwright.sync_api import Page, expect

class SignupPage:
    def __init__(self, page: Page):
        self.page = page
        # 1. Elementos para página "Enter Account Information"
        self.account_info_title = page.get_by_text("Enter Account Information")
        self.mr_radio = page.locator("input#id_gender1")
        self.password_input = page.locator("input#password")
        self.days_dropdown = page.locator("select#days")
        self.months_dropdown = page.locator("select#months")
        self.years_dropdown = page.locator("select#years")
        self.newsletter_checkbox = page.locator("input#newsletter")
        self.offers_checkbox = page.locator("input#optin")

        # 2. Elementos para sección de dirección
        self.first_name_input = page.locator("input#first_name")
        self.last_name_input = page.locator("input#last_name")
        self.company_input = page.locator("input#company")
        self.address1_input = page.locator("input#address1")
        self.address2_input = page.locator("input#address2")
        self.country_dropdown = page.locator("select#country")
        self.state_input = page.locator("input#state")
        self.city_input = page.locator("input#city")
        self.zipcode_input = page.locator("input#zipcode")
        self.mobile_number_input = page.locator("input#mobile_number")
        self.create_account_button = page.locator("button[data-qa='create-account']")

    def verify_account_information_page(self):
        """
        3. Verificar que la página "Enter Account Information" esté visible
        """
        expect(self.account_info_title).to_be_visible(timeout=5000)

    def fill_account_information(self, user_data: dict, birth_data: dict):
        """
        4. Completar información personal: título, contraseña, fecha de nacimiento y checkboxes
        """
        self.mr_radio.check()
        self.password_input.fill(user_data["password"])
        self.days_dropdown.select_option(birth_data["day"])
        self.months_dropdown.select_option(birth_data["month"])
        self.years_dropdown.select_option(birth_data["year"])

        if user_data["newsletter"]:
            self.newsletter_checkbox.check()
        if user_data["offers"]:
            self.offers_checkbox.check()

    def fill_address_information(self, user_data: dict):
        """
        5. Completar información de dirección con datos generados
        """
        self.first_name_input.fill(user_data["name"])
        self.last_name_input.fill(user_data["lastname"])
        self.company_input.fill(user_data["company"])
        self.address1_input.fill(user_data["address1"])
        self.address2_input.fill(user_data["address2"])
        self.country_dropdown.select_option(user_data["country"])
        self.state_input.fill(user_data["state"])
        self.city_input.fill(user_data["city"])
        self.zipcode_input.fill(user_data["zipcode"])
        self.mobile_number_input.fill(user_data["mobile_number"])

    def click_create_account(self):
        """
        6. Hacer click en el botón 'Create Account'
        """
        self.create_account_button.click()

    def click_continue(self):
        """
        7. Hacer click en el botón 'Continue' luego de crear cuenta o eliminar cuenta
        """
        self.page.locator("a[data-qa='continue-button']").click()
