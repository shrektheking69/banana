class SideBar(AbstractPage):
    media_collection_settings_page_button = ElementLocator(By.CSS_SELECTOR, "a[data-testid='media-settings']")
    monitoring_page_button = ElementLocator(By.CSS_SELECTOR, "a[data-testid='monitoring-page-button']")
    sidebar_close_button = ElementLocator(By.XPATH, "//button[@data-testid='sidebar-close-button']")
    monitoring_button = ElementLocator(By.XPATH, '//a[@data-testid="monitoring"]')

    def __init__(self, page: Page):
        super().__init__(page)
