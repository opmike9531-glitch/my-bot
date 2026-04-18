from flask import Flask, request, jsonify, render_template_string
import asyncio
from bot import solve_ixl

app = Flask(__name__)

# The Dashboard with the "Drag to Bookmarks" button
HTML_PAGE = """
<!DOCTYPE html>
<html>
<head>
    <title>ixl-flow | Sync</title>
    <style>
        body { background-color: #050505; color: white; font-family: 'Segoe UI', sans-serif; display: flex; justify-content: center; align-items: center; height: 100vh; margin: 0; }
        .card { background: #0d0d0d; padding: 40px; border-radius: 20px; text-align: center; box-shadow: 0 0 30px rgba(0, 255, 127, 0.1); width: 400px; border: 1px solid #1a1a1a; }
        h1 span { color: #00ff7f; text-shadow: 0 0 10px rgba(0, 255, 127, 0.5); }
        .step { background: #141414; padding: 15px; border-radius: 10px; margin: 10px 0; text-align: left; border-left: 4px solid #00ff7f; font-size: 14px; }
        .btn-glow { background: linear-gradient(90deg, #00ff7f, #00ccff); color: #000; padding: 12px 20px; border-radius: 30px; font-weight: bold; text-decoration: none; display: inline-block; margin-top: 15px; text-transform: uppercase; letter-spacing: 1px; }
    </style>
</head>
<body>
    <div class="card">
        <h1>Sync <span>ixl-flow</span></h1>
        <p style="color: #666;">Connect your session to the dashboard</p>
        <div class="step">
            <strong>1.</strong> Log in to IXL in a new tab.
        </div>
        <div class="step">
            <strong>2.</strong> Drag the button below to your Bookmarks Bar.
        </div>
        <a class="btn-glow" href="javascript:(function(){ window.location.href = 'https://ixl-bot-v2.onrender.com/login?session=' + btoa(window.location.href); })();">IXL SYNC</a>
    </div>
</body>
</html>
"""

# The "mret-style" Login Page
LOGIN_PAGE = """
<!DOCTYPE html>
<html>
<head>
    <title>ixl-flow | Login</title>
    <style>
        body { background-color: #050505; color: white; font-family: 'Segoe UI', sans-serif; display: flex; justify-content: center; align-items: center; height: 100vh; margin: 0; }
        .login-card { background: #0d0d0d; padding: 50px; border-radius: 20px; text-align: center; width: 350px; border: 1px solid #252229; }
        h2 { color: #00ff7f; }
        input { width: 100%; padding: 12px; margin: 10px 0; border-radius: 8px; border: 1px solid #1a1a1a; background: #141414; color: white; }
        button { width: 100%; padding: 12px; border-radius: 25px; border: none; background: #00ccff; color: black; font-weight: bold; cursor: pointer; }
    </style>
</head>
<body>
    <div class="login-card">
        <h2>Link Account</h2>
        <p style="font-size: 12px; color: #888;">Session detected. Enter password to link.</p>
        <form action="/run" method="POST">
            <input type="password" name="password" placeholder="Confirm IXL Password" required>
            <button type="submit">Check Password</button>
        </form>
    </div>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(HTML_PAGE)

@app.route('/login')
def login_screen():
    return render_template_string(LOGIN_PAGE)

@app.route('/run', methods=['POST'])
def run_bot():
    # Logic to start the bot
    return "<h1>Syncing Dashboard...</h1>"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=10000)
