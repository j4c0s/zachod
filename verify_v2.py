import os
from playwright.sync_api import sync_playwright

def generate_screenshots():
    os.makedirs("/home/jules/verification", exist_ok=True)
    with sync_playwright() as p:
        # Launch headless browser
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        # Load local index.html
        current_dir = os.path.dirname(os.path.abspath(__file__))
        index_path = f"file://{os.path.join(current_dir, 'index.html')}"
        sf6_path = f"file://{os.path.join(current_dir, 'sf6-testy.html')}"

        print(f"Navigating to index: {index_path}")
        page.goto(index_path)
        page.set_viewport_size({"width": 1000, "height": 2200})
        page.screenshot(path="/home/jules/verification/index_page_v2.png", full_page=True)
        print("Captured index_page_v2.png")

        print(f"Navigating to sf6: {sf6_path}")
        page.goto(sf6_path)
        page.set_viewport_size({"width": 1000, "height": 1800})
        page.screenshot(path="/home/jules/verification/sf6_page_v2.png", full_page=True)
        print("Captured sf6_page_v2.png")

        browser.close()

if __name__ == "__main__":
    generate_screenshots()
