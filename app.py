from flask import Flask, request, jsonify, render_template_string
import asyncio
from bot import solve_ixl

app = Flask(__name__)

# Dashboard design: Black and Pink (mret style)
HTML_PAGE = """
<!DOCTYPE html>
<html>
<head>
    <title>mret | Dashboard</title>
    <style>
        body { background-color: #0b0a0c; color: white; font-family: 'Segoe UI', sans-serif; display: flex; justify-content: center; align-items: center; height: 100vh; margin: 0; }
        .card { background: #141217; padding: 50px; border-radius: 20px; text-align: center; box-shadow: 0 15px 35px rgba(0,0,0,0.7); width: 380px; border: 1px solid #252229; }
        h1 { font-size: 28px; font-weight: 800; margin-bottom: 10px; }
        h1 span { color: #ff2d8d; }
        p { color: #888; font-size: 14px; margin-bottom: 30px; letter-spacing: 0.5px; }
        .input-group { text-align: left; margin-bottom: 15px; }
        label { font-size: 12px; color: #ff2d8d; text-transform: uppercase; font-weight: bold; margin-left: 5px; }
        input { width: 100%; padding: 14px; margin-top: 5px; border-radius: 10px; border: 1px solid #252229; background: #1c1a21; color: white; box-sizing: border-box; outline: none; transition: 0.3s; }
        input:focus { border-color: #ff2d8d; box-shadow: 0 0 10px rgba(255, 45, 141, 0.2); }
        button { width: 100%; padding: 15px; border-radius: 30px; border: none; background: #ff2d8d; color: white; font-weight: bold; font-size: 16px; cursor: pointer; margin-top: 20px; transition: 0.3s; text-transform: uppercase; letter-spacing: 1px; }
        button:hover { background: #d41b71; transform: translateY(-2px); box-shadow: 0 5px 15px rgba(255, 45, 141, 0.4); }
        .footer { margin-top: 20px; font-size: 11px; color: #444; }
    </style>
</head>
<body>
    <div class="card">
        <h1>Welcome to <span>mret</span></h1>
        <p>Your IXL account is ready to link</p>
        <form action="/run" method="POST">
            <div class="input-group">
                <label>Username</label>
                <input type="text" name="username" placeholder="Enter IXL username" required>
            </div>
            <div class="input-group">
                <label>Password</label>
                <input type="password" name="password" placeholder="Enter IXL password" required>
            </div>
            <button type="submit">Link IXL Dashboard</button>
        </form>
        <div class="footer">Connected to mret servers</div>
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
    
    # Since we removed the URL box, we'll pass a placeholder or handle it in the bot
    skill_url = "https://www.ixl.com/dashboard" 

    try:
        asyncio.run(solve_ixl(username, password, skill_url))
        return "<h1>Success! Account Linked to mret.</h1>"
    except Exception as e:
        return f"<h1>Error: {str(e)}</h1>"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=10000)
