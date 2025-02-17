import asyncio
from playwright.async_api import async_playwright

'''
Проверка заполнение полностью правильными данными
'''
async def test_valid_creat():
    try:
        async with async_playwright() as p:
                browser = await p.firefox.launch()
                page = await browser.new_page()
                await page.wait_for_timeout(2000)
                await page.goto('http://tech-avito-intern.jumpingcrab.com/advertisements/')
                await page.locator("xpath=//button[text()='Создать']").click()
                await page.locator("label:has-text('Название') + input").fill('neeeet')
                await page.locator("label:has-text('Цена') + input").fill('111')
                await page.locator("label:has-text('Описание') + input").fill('Описание')
                await page.locator("label:has-text('Ссылка на изображение') + input").fill('https://example.com/image.jpg')
                await page.click(".chakra-button.css-u6bxse")
                await browser.close()
                message = 'Test valid creat: \033[32mСomplete\033[0m'
    except:
        message = 'Test valid creat: \x1b[31;1mFalled\x1b[0m'
    return message

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    print(loop.run_until_complete(test_valid_creat()))