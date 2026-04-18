from flask import Flask, request, jsonify, render_template_string
import asyncio
from bot import solve_ixl

app = Flask(__name__)

# This is the "Link Your IXL Account" Page Design
HTML_PAGE = """
<!DOCTYPE html>
<html>
<head>
    <title>Link IXL</title>
    <style>
        body { background-color: #120d16; color: white; font-family: sans-serif; display: flex; justify-content: center; align-items: center; height: 100vh; margin: 0; }
        .card { background: #1e1624; padding: 40px; border-radius: 15px; text-align: center; box-shadow: 0 10px 30px rgba(0,0,0,0.5); width: 350px; }
        h2 { color: #ff4da6; margin-bottom: 5px; }
        p { color: #aaa; font-size: 14px; margin-bottom: 25px; }
        input { width: 100%; padding: 12px; margin: 10px 0; border-radius: 8px; border: none; background: #2d2336; color: white; box-sizing: border-box; }
        button { width: 100%; padding: 12px; border-radius: 25px; border: none; background: #ff4da6; color: white; font-weight: bold; cursor: pointer; margin-top: 15px; }
        button:hover { background: #e63e95; }
    </style>
</head>
<body>
    <div class="card">
        <h2>link your IXL account</h2>
        <p>Enter your IXL credentials to connect</p>
        <form action="/run" method="POST">
            <input type="text" name="username" placeholder="IXL Username" required>
            <input type="password" name="password" placeholder="IXL Password" required>
            <input type="text" name="skill_url" placeholder="Paste Skill URL here" required>
            <button type="submit">link account</button>
        </form>
    </div>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(HTML_PAGE)

@app.route('/run', methods=['POST'])
def run_bot():
    # This captures the info from the boxes on the website
    username = request.form.get('username')
    password = request.form.get('password')
    skill_url = request.form.get('skill_url')

    try:
        # Runs the bot.py logic
        asyncio.run(solve_ixl(username, password, skill_url))
        return "<h1>Success! Bot is working in the background.</h1>"
    except Exception as e:
        return f"<h1>Error: {str(e)}</h1>"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=10000)
