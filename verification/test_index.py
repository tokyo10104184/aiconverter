from playwright.sync_api import sync_playwright
import os
import time

def test_index_page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        # Load the index.html file directly
        file_path = os.path.abspath("index.html")
        page.goto(f"file://{file_path}")

        # Wait for content to load. The makers are loaded from Firebase, which might fail or take time.
        # But the official makers are hardcoded in data()

        # 1. Verify Age Restriction Removal (Footer)
        footer_text = page.locator("footer").text_content()
        assert "18歳以上" not in footer_text, "Footer warning was not removed!"
        print("✅ Footer warning removed.")

        # 2. Verify Terms of Service Updates
        page.get_by_text("利用規約").click()
        page.wait_for_selector(".modal-overlay")

        modal_content = page.locator(".modal-overlay").text_content()
        assert "第2条（利用資格）" not in modal_content, "Article 2 (Eligibility) still exists!"
        assert "第2条（禁止事項）" in modal_content, "Article 2 should be 'Prohibitions' now!"
        print("✅ Terms of Service updated correctly.")

        page.locator(".modal-overlay button.text-2xl").click()

        # 3. Verify Text Conversion UI Access
        # To access the textarea, we need to select a maker first!
        # The 'home' view is default. We need to click a maker to go to 'play' view.

        # Click the first official maker
        page.locator(".grid > div").first.click()

        # Now wait for textarea
        textarea = page.locator("textarea")
        textarea.wait_for(state="visible")

        # Now we can fill
        textarea.fill("こんにちは")
        page.get_by_text("変換スタート").click()

        # Wait a bit for potential alert or processing
        time.sleep(2)

        page.screenshot(path="verification/verification_index.png")
        print("✅ Screenshot taken.")

        browser.close()

if __name__ == "__main__":
    test_index_page()
