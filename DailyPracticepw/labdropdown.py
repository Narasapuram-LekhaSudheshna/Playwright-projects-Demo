
from playwright.sync_api import Page,expect

def test_dropdown(page:Page):
    page.goto("https://www.bstackdemo.com/")
    dropdown=page.locator("Select")
    expect(dropdown).to_be_visible()
    expect(dropdown).to_be_enabled()
    dropdown.select_option(label="Lowest to highest")
    page.wait_for_timeout(3000)
    # price=page.locator("#val").all_text_contents()
    # name=page.locator("#products-found").all_text_contents()
    price_elements = page.locator("div.val")
    name_elements = page.locator("p.shelf-item__title")
    prices = price_elements.all_text_contents()
    names = name_elements.all_text_contents()

    # print("Printing Product Names along with their Prices.......")
    # for i in range(len(names)):
    #     print(f"{names[i]} : {prices[i]}")
    #
    # # Print lowest and highest priced products
    # print(f"Lowest Priced Product: {names[0]} : {prices[0]}")
    # print(f"Highest Priced Product: {names[-1]} : {prices[-1]}")
    #


