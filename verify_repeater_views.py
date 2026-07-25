import os
from playwright.sync_api import sync_playwright

def verify_repeater_views():
    os.makedirs("/home/jules/verification", exist_ok=True)
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)

        # 1. Desktop View
        page = browser.new_page()
        page.set_viewport_size({"width": 1000, "height": 2200})

        current_dir = os.path.dirname(os.path.abspath(__file__))
        path = f"file://{os.path.join(current_dir, 'repeater.html')}"

        print("Navigating to repeater.html (Desktop Full View)...")
        page.goto(path)

        # Capture full view
        page.screenshot(path="/home/jules/verification/repeater_desktop_full.png", full_page=True)
        print("Captured /home/jules/verification/repeater_desktop_full.png")

        # Click on simple view toggle
        print("Switching to simplified checklist view...")
        page.click("#btn-view-simple")

        # Capture simple checklist view
        page.screenshot(path="/home/jules/verification/repeater_desktop_simple.png", full_page=True)
        print("Captured /home/jules/verification/repeater_desktop_simple.png")

        # 2. Mobile View
        mobile_page = browser.new_page()
        mobile_page.set_viewport_size({"width": 375, "height": 812})

        print("Navigating to repeater.html (Mobile Full View)...")
        mobile_page.goto(path)

        # Capture mobile full view
        mobile_page.screenshot(path="/home/jules/verification/repeater_mobile_full.png", full_page=True)
        print("Captured /home/jules/verification/repeater_mobile_full.png")

        # Click simple view toggle
        print("Switching to mobile simplified checklist view...")
        mobile_page.click("#btn-view-simple")

        # Capture mobile simple checklist view
        mobile_page.screenshot(path="/home/jules/verification/repeater_mobile_simple.png", full_page=True)
        print("Captured /home/jules/verification/repeater_mobile_simple.png")

        browser.close()

if __name__ == "__main__":
    verify_repeater_views()
