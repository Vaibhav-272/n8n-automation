import pytest
from playwright.sync_api import sync_playwright, expect

@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        yield browser
        browser.close()

@pytest.fixture(scope="function")
def page(browser):
    context = browser.new_context()
    page = context.new_page()
    yield page
    context.close()

def test_trial_alert_and_navigation_links(page):
    page.goto("http://localhost:3000/", wait_until="networkidle")
    page.wait_for_load_state("domcontentloaded")

    # Check trial alert
    trial_alert = page.locator("#freeTrialEndingAlert")
    expect(trial_alert).to_be_visible(timeout=10000)
    expect(trial_alert).to_contain_text("Your free trial ends")

    # Define sidebar links
    expected_links = [
        {"selector": "#sidebarLink", "label": "Dashboard", "required": True},
        {"selector": "#sidebarLinkproperty", "label": "Property", "required": True},
        {"selector": "#sidebarLinkbank", "label": "Bank", "required": True},
        {"selector": "#sidebarLinkreports", "label": "Reports", "required": True},
        {"selector": "#sidebarLinktransactions", "label": "Transactions", "required": True},
        {"selector": "#sidebarLinkaudit-trail", "label": "Audit Checks", "required": True},
        {"selector": "#sidebarLinkdocumentation", "label": "Documentation", "required": False},
        {"selector": "#sidebarLinkcollaboration", "label": "Collaboration", "required": False},
        {"selector": "#sidebarLinkdepreciation", "label": "Depreciation", "required": False}
    ]

    for link in expected_links:
        locator = page.locator(link["selector"])
        if link["required"]:
            expect(locator).to_be_visible(timeout=5000)
            expect(locator).to_contain_text(link["label"])
        else:
            try:
                if locator.is_visible():
                    expect(locator).to_contain_text(link["label"])
            except:
                pass

    # Basic check that page body is visible
    expect(page.locator("body")).to_be_visible()

def test_responsive_layout(page):
    page.goto("http://localhost:3000/")
    page.set_viewport_size({"width": 1920, "height": 1080})
    expect(page.locator("#sidebarLink")).to_be_visible()

    page.set_viewport_size({"width": 768, "height": 1024})
    # Optionally add mobile-specific UI tests here
