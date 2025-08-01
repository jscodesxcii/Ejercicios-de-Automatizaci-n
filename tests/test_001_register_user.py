import pytest
import time
from helpers import TestHelpers
from playwright.sync_api import Page

class TestCase1Complete:

    @pytest.mark.smoke
    @pytest.mark.authentication
    def test_case_1_register_user_complete(self, page: Page):
        """
        1. Ejecutar registro completo y eliminar la cuenta (Test Case 1 original)
        """
        TestHelpers.register_user(page, delete_account=True)

        time.sleep(5)
        print("Test Case 1 completado exitosamente.")
