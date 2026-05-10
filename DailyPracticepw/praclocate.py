import pytest
from playwright.sync_api import Playwright,expect,Page

def test_locate(page: Page):
    page.goto("https://testautomationpractice.blogspot.com/")
    page.get_by_role("button", name="START").click()
    page.locator("#name").fill("Lekha")
    page.locator("#email").fill("kishore@gmail.com")
    page.locator("#phone").fill("989765322")
    page.get_by_text("Alerts & Popups")
    page.get_by_label("Female").click()
    page.get_by_label("Wednesday").click()
    page.get_by_label("Country").select_option("India")
    page.get_by_label("Color").select_option("Yellow")
    page.get_by_role("button", name="Simple Alert").click()
    page.get_by_role("button", name="Confirmation Alert").click()
    page.get_by_role("button", name="Prompt Alert").click()
    page.get_by_label("Sorted List").select_option("Cheetah")
    page.get_by_role("button", name="Point Me").hover()
    mobiles=page.get_by_role("link", name="Mobiles")
    expect(mobiles).to_be_visible()
    mobiles.click()
    page.wait_for_timeout(6000)
