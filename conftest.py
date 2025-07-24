"""
Configuración básica de pytest
=============================
"""
import os
import pytest
from playwright.sync_api import Browser, Page
from config.settings import Config


@pytest.fixture(scope="session")
def browser_type_launch_args(browser_type_launch_args):
    """Argumentos para lanzar el navegador"""
    return {
        **browser_type_launch_args,
        "args": [
            "--start-maximized",
            "--disable-web-security",
        ]
        #"channel": "chrome"  # Usar Chrome específicamente
    }

@pytest.fixture(scope="function")
def page(browser: Browser):
    """Fixture que proporciona una página nueva para cada test"""
    context = browser.new_context(
        no_viewport=True
    )
    page = context.new_page()
    
    # ← AGREGAR ESTA SECCIÓN PARA BLOQUEAR ADS
    # Bloquear requests de anuncios conocidos
    def block_ads(route, request):
        """Bloquea requests de publicidad"""
        ad_domains = [
            "googlesyndication.com",
            "googleadservices.com", 
            "doubleclick.net",
            "googletagmanager.com",
            "google-analytics.com",
            "facebook.com/tr",
            "ads.yahoo.com",
            "adsystem.com",
            "amazon-adsystem.com",
            "adscdn.com",
            "adsbox.com"
        ]
        
        # Si la URL contiene dominios de anuncios, bloquearla
        if any(ad_domain in request.url for ad_domain in ad_domains):
            print(f"Bloqueando anuncio: {request.url}")
            route.abort()
        else:
            route.continue_()
    
    # Aplicar el bloqueador a todas las requests
    page.route("**/*", block_ads)
    
    # Configurar timeouts
    page.set_default_timeout(Config.DEFAULT_TIMEOUT)
    page.set_default_navigation_timeout(Config.NAVIGATION_TIMEOUT)
    
    yield page
    
    # Cleanup
    context.close()

@pytest.fixture(autouse=True)
def setup_test_environment():
    """Setup que se ejecuta antes de cada test"""
    # Crear directorios si no existen
    
    os.makedirs("reports/screenshots", exist_ok=True)
    
    yield