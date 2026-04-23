from playwright.sync_api import Page, expect


def test_verifyPageUrl(page:Page):
    page.goto("https://omayo.blogspot.com/")
    expect(page).to_have_url("https://omayo.blogspot.com/")

def test_verifyTitle(page:Page):
    page.goto("https://omayo.blogspot.com/")
    expect(page).to_have_title("omayo(QAFox.com)")



