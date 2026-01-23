from playwright.sync_api import sync_playwright
import os
import time

def test_models_and_creator():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)

        # Test 1: Check models in index.html
        page = browser.new_page()
        file_path_index = os.path.abspath("index.html")
        page.goto(f"file://{file_path_index}")

        # Open Settings
        page.locator("button[title='設定']").click()
        time.sleep(1)

        # Check select options
        options = page.locator("select option").all_text_contents()
        print(f"Found models: {options}")
        assert len(options) == 1, f"Expected 1 model, found {len(options)}"
        assert "deepseek-r1t2-chimera:free" in options[0], "Expected deepseek-r1t2-chimera:free"

        print("✅ index.html models verified.")
        page.close()

        # Test 2: Check creator.html
        page = browser.new_page()
        file_path_creator = os.path.abspath("creator.html")
        page.goto(f"file://{file_path_creator}")

        # Fill input
        page.locator("input[placeholder='テスト用テキスト...']").fill("Hello")

        # Click Run Test
        page.get_by_text("テスト実行").click()

        # Check for demo message
        # Wait a bit for the async logic
        time.sleep(2)

        result_text = page.locator(".whitespace-pre-wrap").text_content()
        print(f"Creator test result: {result_text}")
        assert "【デモ】APIキー未設定" in result_text or "APIキー未設定" in result_text, "Expected demo message in creator"

        print("✅ creator.html verified.")
        browser.close()

if __name__ == "__main__":
    test_models_and_creator()
