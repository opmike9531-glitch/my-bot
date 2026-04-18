from flask import Flask, render_template_string, request
from playwright.sync_api import sync_playwright
import time

app = Flask(__name__)

# This is the HTML (the "Face" of the website)
HTML_PAGE = '''
<!DOCTYPE html>
<html>
<head>
    <title>IXL Bot Dashboard</title>
    <style>
        body { font-family: sans-serif; text-align: center; padding: 50px; background: #f4f4f9; }
        .card { background: white; padding: 30px; border-radius: 15px; display: inline-block; box-shadow: 0 4px 10px rgba(0,0,0,0.1); }
        input { display: block; margin: 10px auto; padding: 10px; width: 250px; border-radius: 5px; border: 1px solid #ccc; }
        button { background: #007bff; color: white; border: none; padding: 10px 20px; border-radius: 5px; cursor: pointer; }
    </style>
</head>
<body>
    <div class="card">
        <h1>🤖 IXL Helper Bot</h1>
        <form action="/run" method="post">
            <input type="text" name="user" placeholder="06 Number" required>
            <input type="password" name="pass" placeholder="Password" required>
            <input type="text" name="skill" placeholder="Skill Code (e.g. V7F)" required>
            <button type="submit">Start Bot</button>
        </form>
    </div>
</body>
</html>
'''

@app.route('/')
def home():
    return render_template_string(HTML_PAGE)

@app.route('/run', methods=['POST'])
def run_bot_web():
    # Getting the info you typed into the boxes
    username = request.form.get('user')
    password = request.form.get('pass')
    skill = request.form.get('skill')
    
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        
        # Log In
        page.goto("https://www.ixl.com/signin")
        page.locator('input#siusername').fill(username)
        page.locator('input#sipassword').fill(password)
        page.keyboard.press("Enter")
        time.sleep(5)
        
        # Go to Skill
        page.goto(f"https://www.ixl.com/math/skill-plans/{skill}")
        time.sleep(3)
        title = page.title()
        browser.close()
        
    return f"<h2>Mission Success!</h2><p>The bot reached: {title}</p><a href='/'>Go Back</a>"

if __name__ == '__main__':
    # Codespaces uses port 5000
    app.run(host='0.0.0.0', port=5000)
