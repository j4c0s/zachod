import os
from playwright.sync_api import sync_playwright

def generate_screenshots():
    os.makedirs("/home/jules/verification", exist_ok=True)
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        current_dir = os.path.dirname(os.path.abspath(__file__))

        pages = {
            "index": "index.html",
            "companion": "companion.html",
            "repeater": "repeater.html",
            "roomserver": "roomserver.html",
            "regiony": "regiony.html",
            "sf6": "sf6-testy.html"
        }

        for name, filename in pages.items():
            path = f"file://{os.path.join(current_dir, filename)}"
            print(f"Navigating to {name}: {path}")
            page.goto(path)
            page.set_viewport_size({"width": 1000, "height": 1800})
            screenshot_path = f"/home/jules/verification/{name}_page_v3.png"
            page.screenshot(path=screenshot_path, full_page=True)
            print(f"Captured {screenshot_path}")

        browser.close()

if __name__ == "__main__":
    generate_screenshots()
