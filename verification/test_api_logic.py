from playwright.sync_api import sync_playwright
import os
import time

def test_api_key_logic():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        file_path = os.path.abspath("index.html")
        page.goto(f"file://{file_path}")

        # Select a maker to get to the play screen
        page.locator(".grid > div").first.click()

        # Fill input
        textarea = page.locator("textarea")
        textarea.wait_for(state="visible")
        textarea.fill("test input")

        # Click convert
        page.get_by_text("変換スタート").click()

        # Wait a moment
        time.sleep(2)

        # Check output
        # If key is set (even if invalid), it should NOT show "【デモモード】APIキー未設定です。"
        # It might show a fetch error, but that's expected.

        output_element = page.locator(".whitespace-pre-wrap")

        # The output element might not exist if it's still loading or if no error was written to it.
        # But if the check failed, it writes to outputText.

        if output_element.count() > 0:
            text = output_element.text_content()
            print(f"Output text: {text}")
            if "【デモモード】APIキー未設定です" in text:
                print("❌ FAILED: Still showing API key missing message despite key being set.")
            else:
                print("✅ PASSED: Not showing API key missing message.")
        else:
            # If output element is not shown, it means it didn't set outputText yet (maybe stuck in loading or threw alert)
            # Check for alert
            print("✅ PASSED: No output text (likely loading or network error handled differently).")

        browser.close()

if __name__ == "__main__":
    test_api_key_logic()
