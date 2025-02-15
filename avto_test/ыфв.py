import asyncio
from playwright.async_api import async_playwright
'''
Проверка валидации строк ввода цена и ввода случайных символов в url
'''
async def test_valid_negativ_price():
    try:
        async with async_playwright() as p:
                browser = await p.firefox.launch()
                page = await browser.new_page()
                await page.wait_for_timeout(2000)
                await page.goto('http://tech-avito-intern.jumpingcrab.com/advertisements/')
                await page.locator("xpath=//button[text()='Создать']").click()
                await page.locator("label:has-text('Название') + input").fill('neeeet0')
                await page.locator("label:has-text('Цена') + input").fill(-111)
                await page.locator("label:has-text('Описание') + input").fill('Описание')
                await page.locator("label:has-text('Ссылка на изображение') + input").fill('neeee')
                await page.click(".chakra-button.css-u6bxse")

                await page.locator("xpath=//button[text()='Создать']").click()
                await page.locator("label:has-text('Название') + input").fill('neeeet3')
                await page.locator("label:has-text('Цена') + input").fill('-0')
                await page.locator("label:has-text('Описание') + input").fill('Описание')
                await page.locator("label:has-text('Ссылка на изображение') + input").fill('neeee')
                await page.click(".chakra-button.css-u6bxse")

                await page.locator("xpath=//button[text()='Создать']").click()
                await page.locator("label:has-text('Название') + input").fill('neeeet4')
                await page.locator("label:has-text('Цена') + input").fill('0')
                await page.locator("label:has-text('Описание') + input").fill('Описание')
                await page.locator("label:has-text('Ссылка на изображение') + input").fill('neeee')
                await page.click(".chakra-button.css-u6bxse")

                await page.locator("xpath=//button[text()='Создать']").click()
                await page.locator("label:has-text('Название') + input").fill('neeeet4')
                await page.locator("label:has-text('Цена') + input").fill('999999999999999999999999999999999999999999999999999999999999999999999999999999990')
                await page.locator("label:has-text('Описание') + input").fill('Описание')
                await page.locator("label:has-text('Ссылка на изображение') + input").fill('neeee')
                await page.click(".chakra-button.css-u6bxse")
                
                await browser.close()
                message = 'Test valid price: \033[32mСomplete\033[0m'
    except:
        message = 'Test valid price: \x1b[31;1mFalled\x1b[0m'
    return message

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    print(loop.run_until_complete(test_valid_negativ_price()))