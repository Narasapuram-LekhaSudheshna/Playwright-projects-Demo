import playwright
from playwright.sync_api import Page,expect


def test_verify_practiceloc(page: Page):
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    page.get_by_placeholder("Username").fill("Admin")
    page.get_by_placeholder("Password").fill("admin123")
    page.wait_for_timeout(3000)
