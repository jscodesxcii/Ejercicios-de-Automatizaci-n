"""
Clase base básica para Page Object Model
======================================
"""
import time
from playwright.sync_api import Page, expect
from config.settings import Config, Selectors


class BasePage:
    """Clase base con métodos comunes básicos"""
    
    def __init__(self, page: Page):
        self.page = page
        self.config = Config()
        
    def navigate_to(self, url: str = None):
        """Navegar a una URL"""
        target_url = url or self.config.BASE_URL
        self.page.goto(target_url)
        self.wait_for_page_load()

        # Maximizar la ventana del navegador
        #self.page.evaluate("window.moveTo(0, 0)")
        #self.page.evaluate("window.resizeTo(screen.width, screen.height)")

        time.sleep(2)
        
    def wait_for_page_load(self):
        """Esperar a que la página cargue"""
        self.page.wait_for_load_state("networkidle")
        
    def click_element(self, selector: str):
        """Hacer click en un elemento"""
        self.page.click(selector)
        time.sleep(1)
        
    def fill_input(self, selector: str, text: str):
        """Llenar un campo de input"""
        self.page.fill(selector, text)
        time.sleep(1)
        
    def is_text_visible(self, text: str) -> bool:
        """Verificar si un texto es visible"""
        try:
            self.page.wait_for_selector(f"text={text}", timeout=5000)
            return True
        except:
            return False
            
    # Métodos específicos del sitio
    def verify_home_page_visible(self):
        """Verificar que estamos en la página principal"""
        expect(self.page.locator("img[alt*='Website for automation practice']")).to_be_visible()
        time.sleep(1)
        
    def click_signup_login(self):
        """Hacer click en Signup/Login"""
        self.click_element(Selectors.SIGNUP_LOGIN_BUTTON)
        
    def click_delete_account(self):
        """Hacer click en Delete Account"""
        self.click_element(Selectors.DELETE_ACCOUNT_BUTTON)
        
    def verify_logged_in_user(self, username: str):
        """Verificar que el usuario está logueado"""
        logged_in_text = f"Logged in as {username}"
        expect(self.page.locator(f"text={logged_in_text}")).to_be_visible()
        time.sleep(1)
        
    def verify_account_created(self):
        """Verificar que la cuenta fue creada"""
        expect(self.page.locator(Selectors.ACCOUNT_CREATED_TEXT)).to_be_visible()
        time.sleep(2)
        
    def verify_account_deleted(self):
        """Verificar que la cuenta fue eliminada"""
        expect(self.page.locator(Selectors.ACCOUNT_DELETED_TEXT)).to_be_visible()
        time.sleep(2)