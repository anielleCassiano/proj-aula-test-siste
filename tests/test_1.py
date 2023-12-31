import pytest
import time

from pages.LoginPages import LoginPages

class Test1:

    @pytest.mark.parametrize('all_browser', ['chrome', 'firefox'])
    def test_click_login_btn(self, run_all_browser):
        login_page = run_all_browser
        login_page.click_login_btn()
        assert login_page.is_URL_login(), "Página mudou!"
        assert login_page.has_login_error_message(), 'Mensagem de erro não encontrada!'
