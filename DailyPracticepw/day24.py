import pytest
from playwright.sync_api import expect,Page
from playwright.sync_api import Page

def test_day24(page: Page):

    page.goto("https://www.flipkart.com/")
    page.locator("span:has-text('Login')").fill("9620301001")
    page.wait_for_timeout(5000)


    search_box=page.locator("input[name='q']")
    search_box.fill(value="smart")
    page.wait_for_timeout(5000)