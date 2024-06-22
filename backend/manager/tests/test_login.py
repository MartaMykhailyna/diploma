import pytest
from playwright.sync_api import sync_playwright

# Функція, що виконує тест
# def test_placeholder_attribute():
#     with sync_playwright() as p:
#         browser = p.chromium.launch()
#         page = browser.new_page()

#         # Відкриваємо сторінку
#         page.goto("http://127.0.0.1:7000/authorization/login/")

#         # Знаходимо елемент та отримуємо його атрибут
#         message_input = page.locator("input#id_email_or_username").fill("samuliakk")
#         # placeholder_value = message_input.get_attribute("placeholder")
#         # message_input.fill("samuliakk")
#         password_input = page.locator("input#id_password").fill("380963052959")
#         # password_input.fill("380963052959")
#         btn_login = page.locator("input[type=submit]")
#         # Виводимо значення атрибуту в консоль
#         # print(message_input.get_attribute("placeholder"))

#         # Закриваємо браузер
#         browser.close()

# # Виконання тесту