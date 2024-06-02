class ChatsPage():
  
    download_chat_button = ElementLocator(By.CSS_SELECTOR, "[data-testid='download-single-chat']")
    popup_confirm_button = ElementLocator(By.XPATH, "//button[text()='Export Device']")
    chat_new_indication = ElementLocator(By.XPATH, "//div[@data-testid='New-chip']/span")
    chat_name = ElementLocator(By.CSS_SELECTOR, "span[data-testid='chat-name']")
    scrollable_chat = ElementLocator(By.XPATH, "//div[@data-testid='chat-scrollable']/div")
    chats_list = ElementLocator(By.XPATH, "//div[@data-testid='chat_list']")
    chat_menu_button = ElementLocator(By.CSS_SELECTOR, "//button[@data-testid='menu-button']")
    lockdown_icon = ElementLocator(By.XPATH, "//div[@data-testid='lockdown-icon']")
    phone_number = ElementLocator(By.CSS_SELECTOR, "span[data-testid='chat-phone']")

    def __init__(self):
      pass
