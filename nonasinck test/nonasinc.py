'''
скрипт без использования асинк авайит для личного пользования
'''
from playwright.sync_api import sync_playwright


def test_create_ad():
    with sync_playwright() as p:
        # Запуск браузера Firefox
        browser = p.firefox.launch(headless=False)  # headless=False для визуального отображения
        page = browser.new_page()

        # Переход на сайт
        page.goto("http://tech-avito-intern.jumpingcrab.com/advertisements/")
        page.wait_for_timeout(2000)

        # Нажать на кнопку с дроп дауном
        page.locator("button.chakra-button.chakra-menu__menu-button.css-98wh1e").click()

        # Выбрать из выпавшего пункта button с id menu-list-:r5:-menuitem-:ra:
        page.locator("button:has-text('25')").click()

        while True:
            try:
                page.locator("button:has-text('Следующая')").click()
            except Exception as e:
                print(f"Ошибка: {e}")
                break


        # Нажатие на кнопку вызова контекстного меню
        # page.locator("xpath=//button[text()='Создать']").click()
        # page.locator("label:has-text('Название') + input").fill('neeeet')
        # page.locator("label:has-text('Цена') + input").type('asd')
        # # input_field = page.locator("label:has-text('Цена') + input")
        # # input_field.fill('asd')
        # # assert input_field.input_value() == ''

        # page.locator("label:has-text('Описание') + input").fill('Описание')
        # page.locator("label:has-text('Ссылка на изображение') + input").fill('https://example.com/image.jpg')
        # page.click(".chakra-button.css-u6bxse")

        # span_locator = page.locator("div.chakra-form__error-message.css-502kp3")
        # span_text = span_locator.text_content()
        # assert span_text == 'Поле обязательно для заполнения.'

        # Пауза для визуальной проверки (можно убрать)
        # page.wait_for_timeout(2000)

        # Закрытие браузера
        browser.close()

# Запуск теста
if __name__ == "__main__":
    test_create_ad()
