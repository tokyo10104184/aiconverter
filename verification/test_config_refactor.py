from playwright.sync_api import sync_playwright
import os
import time
import subprocess
import sys
import signal

def test_config_refactor():
    # Start HTTP server
    # using a random port to avoid conflicts, or standard 8000
    port = 8000
    server_process = subprocess.Popen(
        [sys.executable, "-m", "http.server", str(port)],
        cwd=os.getcwd(),
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )

    print(f"Started HTTP server on port {port} with PID {server_process.pid}")
    time.sleep(2) # Give it time to start

    try:
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True)

            # --- Test index.html ---
            page = browser.new_page()
            url_index = f"http://localhost:{port}/index.html"
            print(f"Navigating to {url_index}")

            # Catch console errors to detect module loading failures
            page.on("console", lambda msg: print(f"Console: {msg.text}"))
            page.on("pageerror", lambda err: print(f"PageError: {err}"))

            page.goto(url_index)

            # Open Settings
            try:
                page.locator("button[title='設定']").click()
                time.sleep(1)
                options = page.locator("select option").all_text_contents()
                print(f"Found models in index.html: {options}")

                assert len(options) == 1, "Expected 1 model"
                assert "deepseek-r1t2-chimera:free" in options[0], "Expected deepseek model"
                print("✅ index.html loaded config.js correctly.")

                # Take screenshot
                page.screenshot(path="verification/verification_refactor.png")
                print("✅ Screenshot saved to verification/verification_refactor.png")

            except Exception as e:
                print(f"❌ Failed to verify index.html: {e}")
                raise e
            finally:
                page.close()

            # --- Test creator.html ---
            page = browser.new_page()
            url_creator = f"http://localhost:{port}/creator.html"
            print(f"Navigating to {url_creator}")

            page.goto(url_creator)

            # If config.js fails to load, Vue app won't mount, so #app content might be empty or static
            # Check if we can type in the emoji input (part of Vue data)
            try:
                page.locator("input[type='text']").first.wait_for(state="visible", timeout=5000)
                print("✅ creator.html loaded (input visible).")
            except Exception as e:
                print(f"❌ Failed to verify creator.html: {e}")
                raise e
            finally:
                page.close()

            browser.close()

    finally:
        # Kill server
        print("Stopping HTTP server...")
        server_process.terminate()
        server_process.wait()

if __name__ == "__main__":
    test_config_refactor()
