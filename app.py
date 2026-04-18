from flask import Flask, request, jsonify, render_template_string
import asyncio
from bot import solve_ixl

app = Flask(__name__)

# Updated Theme: Black, Neon Green, and Electric Blue
HTML_PAGE = """
<!DOCTYPE html>
<html>
<head>
    <title>ixl-flow | Dashboard</title>
    <style>
        body { background-color: #050505; color: white; font-family: 'Segoe UI', sans-serif; display: flex; justify-content: center; align-items: center; height: 100vh; margin: 0; }
        .card { background: #0d0d0d; padding: 50px; border-radius: 20px; text-align: center; box-shadow: 0 0 30px rgba(0, 255, 127, 0.1); width: 380px; border: 1px solid #1a1a1a; }
        h1 { font-size: 28px; font-weight: 800; margin-bottom: 10px; letter-spacing: -1px; }
        h1 span { color: #00ff7f; text-shadow: 0 0 10px rgba(0, 255, 127, 0.5); }
        p { color: #666; font-size: 14px; margin-bottom: 30px; letter-spacing: 0.5px; }
        .input-group { text-align: left; margin-bottom: 15px; }
        label { font-size: 12px; color: #00ccff; text-transform: uppercase; font-weight: bold; margin-left: 5px; }
        input { width: 100%; padding: 14px; margin-top: 5px; border-radius: 10px; border: 1px solid #1a1a1a; background: #141414; color: white; box-sizing: border-box; outline: none; transition: 0.3s; }
        input:focus { border-color: #00ccff; box-shadow: 0 0 10px rgba(0, 204, 255, 0.2); }
        button { width: 100%; padding: 15px; border-radius: 30px; border: none; background: linear-gradient(90deg, #00ff7f, #00ccff); color: #000; font-weight: bold; font-size: 16px; cursor: pointer; margin-top: 20px; transition: 0.3s; text-transform: uppercase; letter-spacing: 1px; }
        button:hover { transform: translateY(-2px); box-shadow: 0 5px 20px rgba(0, 255, 127, 0.4); opacity: 0.9; }
        .footer { margin-top: 20px; font-size: 11px; color: #333; }
    </style>
</head>
<body>
    <div class="card">
        <h1>Welcome to <span>ixl-flow</span></h1>
        <p>Ready to sync with IXL</p>
        <form action="/run" method="POST">
            <div class="input-group">
                <label>Username</label>
                <input type="text" name="username" placeholder="IXL Username" required>
            </div>
            <div class="input-group">
                <label>Password</label>
                <input type="password" name="password" placeholder="IXL Password" required>
            </div>
            <button type="submit">Connect IXL Dashboard</button>
        </form>
        <div class="footer">Server Status: Online | Encryption: Active</div>
    </div>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(HTML_PAGE)

@app.route('/run', methods=['POST'])
def run_bot():
    username = request.form.get('username')
    password = request.form.get('password')
    # Defaulting to the main dashboard since you want to handle skills manually
    skill_url = "https://www.ixl.com/dashboard" 

    try:
        # This triggers the login process in bot.py
        asyncio.run(solve_ixl(username, password, skill_url))
        return "<h1 style='color: #00ff7f; background: #000; font-family: sans-serif; text-align: center; padding: 50px;'>Success! Account Synced to Flow Dashboard.</h1>"
    except Exception as e:
        return f"<h1 style='color: #00ccff; background: #000; font-family: sans-serif; text-align: center; padding: 50px;'>Connection Error: {str(e)}</h1>"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=10000)
