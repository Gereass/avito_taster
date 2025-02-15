import asyncio
from playwright.async_api import async_playwright
''' 
Скрипт для проверки пролистывания объявлений путём нажатия 100000 раз на кнопку "Следующая"
'''
async def test_nonvalid_price():
    try:
        async with async_playwright() as p:
            browser = await p.firefox.launch()
            page = await browser.new_page()
            await page.goto('http://tech-avito-intern.jumpingcrab.com/advertisements/')
            await page.locator("button.chakra-button.chakra-menu__menu-button.css-98wh1e").click()
            await page.locator("button:has-text('25')").click()

            for _ in range(100000):
                await page.locator("button:has-text('Следующая')").click()
                await page.wait_for_timeout(100)  

            browser.close()
            message = 'Test valid price: \033[32mСomplete\033[0m'
    except:
        message = 'Test valid price: \x1b[31;1mFalled\x1b[0m'
    return message

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    print(loop.run_until_complete(test_nonvalid_price()))