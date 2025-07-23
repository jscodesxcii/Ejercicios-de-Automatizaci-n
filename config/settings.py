"""
Configuración básica del proyecto
===============================
"""

class Config:
    """Configuración principal del proyecto"""
    
    # URL del sitio a testear
    BASE_URL = "https://automationexercise.com"
    
    # Timeouts en milisegundos
    DEFAULT_TIMEOUT = 30000
    NAVIGATION_TIMEOUT = 30000
    
    # Datos de prueba
    TEST_EMAIL_DOMAIN = "@testautomation.com"
    DEFAULT_PASSWORD = "TestPassword123!"


class Selectors:
    """Selectores básicos que usaremos"""
    
    # Header navigation
    SIGNUP_LOGIN_BUTTON = "a[href='/login']"
    LOGOUT_BUTTON = "a[href='/logout']"
    DELETE_ACCOUNT_BUTTON = "a[href='/delete_account']"
    
    # Messages
    LOGGED_IN_USER_TEXT = "text=Logged in as"
    ACCOUNT_CREATED_TEXT = "text=Account Created!"
    ACCOUNT_DELETED_TEXT = "text=Account Deleted!"