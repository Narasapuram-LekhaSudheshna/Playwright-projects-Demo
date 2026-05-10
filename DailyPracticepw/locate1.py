import pytest
from playwright.sync_api import Playwright,expect,Page
def test_locate1(page: Page):
    page.goto("https://testautomationpractice.blogspot.com/")
    page.locator("#field2").fill("Hi Buddy")
    page.locator("#datepicker").fill("05/27/1995")
    page.locator("#txtDate").evaluate("element => element.removeAttribute('readonly')")
    page.locator("#txtDate").fill("12/14/2016")
    page.locator("#start-date").fill("1993-09-30")
    page.locator("#end-date").fill("2016-12-31")
    page.wait_for_timeout(7000)  