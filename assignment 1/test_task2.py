import pytest
from playwright.sync_api import Page, expect


@pytest.mark.smoke
def test_google(page: Page):
    page.goto("https://www.example.com")
    expect(page).to_have_title("Example Domain")
    expect(page.locator("h1")).to_have_text("Example Domain")

    expect(page.locator("body")).to_contain_text(
        "This domain is for use in documentation examples without needing permission. Avoid use in operations."
    )
    actual_title = page.title()
    assert actual_title != "Wrong Page Title"

