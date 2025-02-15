import asyncio
from playwright.async_api import async_playwright
'''
Проверка валидации строк ввода цены и подтверждение того, что неправильными данные не могут быт внесены
'''
async def test_nonvalid_price():
    try:
        async with async_playwright() as p:
                browser = await p.firefox.launch()
                page = await browser.new_page()
                await page.wait_for_timeout(2000)
                await page.goto('http://tech-avito-intern.jumpingcrab.com/advertisements/')
                await page.locator("xpath=//button[text()='Создать']").click()
                await page.locator("label:has-text('Название') + input").fill('neeeet0')
                await page.locator("label:has-text('Цена') + input").fill('-111')
                await page.locator("label:has-text('Описание') + input").fill('Описание')
                await page.locator("label:has-text('Ссылка на изображение') + input").fill('https://example.com/image.jpg')
                await page.click(".chakra-button.css-u6bxse")

                span_locator = page.locator("div.chakra-form__error-message.css-502kp3")
                span_text = await span_locator.text_content()
                assert span_text == 'Поле обязательно для заполнения.'
                
                await browser.close()
                message = 'Test valid price: \033[32mСomplete\033[0m'
    except:
        message = 'Test valid price: \x1b[31;1mFalled\x1b[0m'
    return message

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    print(loop.run_until_complete(test_nonvalid_price()))