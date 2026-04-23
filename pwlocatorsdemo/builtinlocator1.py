import pytest

from playwright.sync_api import Page,expect



# page.get_by_alt_text, page.get_by_text,page.get_by_alt_text,page.get_by_label,page.get_by_placeholder,page.get_by_title


def test_verify_pwlocators(page:Page):
    page.goto("https://www.facebook.com/")
    # logo=page.get_by_alt_text("Log in to Facebook")   # page.get_by_alt_text
    # expect(logo).to_be_visible()

    # expect(page.get_by_text("Fcaebook")).to_be_visible()    #full text
    #
    # expect(page.get_by_text("Face")).to_be_visible()        #partial text
    # expect(page.get_by_text("book")).to_be_visible()      #reg expression
    # page.wait_for_timeout(5000)

    page.goto("https://www.facebook.com/")
    expect(page.get_by_role("heading",name="Log in to Facebook")).to_be_visible()

    #page.get_by_label()
    page.goto("https://www.facebook.com/")
    page.locator("#email").fill("test@gmail.com")
