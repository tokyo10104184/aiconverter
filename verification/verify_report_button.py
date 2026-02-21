from playwright.sync_api import sync_playwright
import sys

def run(playwright):
    browser = playwright.chromium.launch(headless=True)
    page = browser.new_page()
    try:
        page.goto("http://localhost:8080/index.html")

        # Find the dummy maker and click it
        page.get_by_text("Test Maker").click()

        # Wait for the play view
        page.wait_for_timeout(1000)

        # Verify the report button is visible (it should be because it's not official ID)
        report_btn = page.get_by_title("このメーカーを通報")
        if report_btn.is_visible():
            print("Report button is visible.")
        else:
            print("Report button is NOT visible.")
            sys.exit(1)

        # Take screenshot of the actions area
        # We can locate the parent container of the buttons
        actions_div = report_btn.locator("..") # parent div
        actions_div.screenshot(path="verification/verification.png")

    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)
    finally:
        browser.close()

with sync_playwright() as playwright:
    run(playwright)
