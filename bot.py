from playwright.sync_api import sync_playwright
import time

def run_bot():
    with sync_playwright() as p:
        print("🚀 Robot is online...")
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        # 1. LOG IN (Using the working method)
        print("🌐 Logging into IXL...")
        page.goto("https://www.ixl.com/signin", wait_until="networkidle")
        page.locator('input#siusername').fill("0617110718@browardcps") # <--- USERNAME
        page.locator('input#sipassword').fill("1234well1*")   # <--- PASSWORD
        page.keyboard.press("Enter")
        
        time.sleep(10)
        print(f"✅ Dashboard reached: {page.title()}")

        # 2. FIND THE SKILL
        # Replace 'V7F' with whatever skill you need to do!
        skill_code = "V7F" 
        print(f"🔍 Searching for skill: {skill_code}")
        
        # Click the search bar and type the code
        page.locator('input.nav-search-input').fill(skill_code)
        page.keyboard.press("Enter")
        
        # Wait for the search results and click the first one
        time.sleep(5)
        print("🖱️ Clicking the skill...")
        page.click('.search-result-link')
        
        # 3. GET THE QUESTION
        time.sleep(5)
        print(f"📖 Now on skill: {page.title()}")
        
        # Take a screenshot so we can see the math problem!
        page.screenshot(path="question.png")
        print("📸 Screenshot of the question saved as 'question.png'.")

        browser.close()

if __name__ == "__main__":
    run_bot()
