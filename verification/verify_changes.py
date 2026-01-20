from playwright.sync_api import sync_playwright
import os

def test_index_page(page):
    # Load index.html directly
    page.goto(f"file://{os.path.abspath('index.html')}")

    # Wait for the settings button and click it to check available models
    page.get_by_role("button", name="設定").click()

    # Check if the select element has the correct option
    select = page.locator("select")

    # Verify the selected model is openai/gpt-oss-120b:free
    # We can check the value of the select element
    assert select.input_value() == "openai/gpt-oss-120b:free"

    # Take a screenshot of the settings modal
    page.screenshot(path="verification/index_settings.png")

def test_creator_page(page):
    # Load creator.html directly
    page.goto(f"file://{os.path.abspath('creator.html')}")

    # Take a screenshot of the creator page
    # Since the change is mainly in the API call logic, visually we just check if the page loads fine
    # and maybe check the console if we could, but visual check is just "it didn't break layout"
    page.screenshot(path="verification/creator_page.png")

if __name__ == "__main__":
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        try:
            test_index_page(page)
            test_creator_page(page)
            print("Verification scripts ran successfully.")
        except Exception as e:
            print(f"Error: {e}")
        finally:
            browser.close()
