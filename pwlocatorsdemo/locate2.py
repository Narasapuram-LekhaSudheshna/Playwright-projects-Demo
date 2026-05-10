from playwright.sync_api import Page

def test_page_loacte(page: Page):
     page.goto("https://way2automation.com/")
     title = page.title()
     print(title)
     assert "Way2Automation" in title
     page.wait_for_timeout(5000)

