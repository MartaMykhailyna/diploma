import pytest
from playwright.sync_api import sync_playwright, expect

# Функція, що виконує тест
def test_placeholder_attribute():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()

        # Відкриваємо сторінку
        page.goto("http://127.0.0.1:7000/app/analytics_admin/")

        # Знаходимо елемент та отримуємо його атрибут
        sidebar_btn=page.locator('.fa-bars').click()

        # Очікування для елементу aside видимості 
        expect(page.locator('#aside')).to_be_visible()

        # Закриваємо браузер
        browser.close()