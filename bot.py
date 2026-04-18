import asyncio
from playwright.async_api import async_playwright

async def solve_ixl(username, password, skill_url):
    async with async_playwright() as p:
        # headless=True is the most important part for Render!
        browser = await p.chromium.launch(headless=True, args=["--no-sandbox"])
        context = await browser.new_context()
        page = await context.new_page()

        try:
            print(f"Logging in as {username}...")
            await page.goto("https://www.ixl.com/signin")
            await page.fill("#siusername", username)
            await page.fill("#sipassword", password)
            await page.click("#sindiv > form > div.submit-button-container > button")
            
            # Wait for login to finish
            await page.wait_for_timeout(3000)

            print(f"Heading to skill: {skill_url}")
            await page.goto(skill_url)

            # Example loop to solve problems
            for i in range(10):  # Adjust number of problems as needed
                print(f"Solving problem {i+1}...")
                # This part depends on the specific IXL skill layout
                # Usually you'd look for the question text and input box
                await page.wait_for_timeout(2000) 
                
            print("Session complete!")
        except Exception as e:
            print(f"An error occurred: {e}")
        finally:
            await browser.close()

# This is for testing or internal calls
if __name__ == "__main__":
    # You can put test credentials here if running locally
    pass
