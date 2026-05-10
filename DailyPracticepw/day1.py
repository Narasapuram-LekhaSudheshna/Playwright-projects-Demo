import pytest
from playwright.sync_api import Page,expect

def test_day1(page: Page):
    page.goto("https://testautomationpractice.blogspot.com/")
    page.locator("#name").fill("ReshikaLishitha")
    page.locator("#phone").fill("986758898")
    page.locator("#email").fill("nikki@gmail.com")
    expect(page.get_by_role("button", name="START")).to_be_visible()
    page.get_by_role("button", name="Prompt Alert").click()
    page.get_by_role("button", name="Confirmation Alert").click()
    page.get_by_label("Female").click()
    page.get_by_label("Monday").click()
    page.get_by_label("Country").select_option("Brazil")
    page.get_by_label("colors").select_option("Green")
    page.get_by_text("Automation Testing Practice").is_visible()
    page.wait_for_timeout(5000)
