from pages.ProductsPages import ProductsPage

class Test2:

    def test_login(self, setup):
        login_page = setup
        login_page.efetuar_login()
        products_page = ProductsPage(driver=login_page.driver)
        assert products_page.is_url_products(), 'URL mudou'
        assert products_page.has_products_title(), 'Titulo da pagina diferente da página'
        assert products_page.validate_products_in_page, 'Lista de Produtos incorreta'
        assert products_page.has_menu_button(), 'Botão de Menu não encontrado'







